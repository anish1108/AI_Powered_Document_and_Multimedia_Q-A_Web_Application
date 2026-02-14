from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import UploadedFile, Transcript
from .services.file_processor import detect_file_type, extract_pdf_text
from .services.transcription_service import transcribe_audio
from .services.qa_service import answer_question
from .services.summary_service import summarize_text
from .api_base import ApiBaseView




@method_decorator(csrf_exempt, name="dispatch")
class FileUploadView(ApiBaseView):

    def post(self, request):

        uploaded_file = request.FILES.get("file")

        if not uploaded_file:
            return JsonResponse({"error": "No file provided"}, status=400)

       
        file_obj = UploadedFile.objects.create(
            file=uploaded_file,
            file_type=uploaded_file.content_type
        )

        file_path = file_obj.file.path

      
        file_kind = detect_file_type(file_path)
        print('file kind is '+ file_kind)

       
        if file_kind == "pdf":

            text = extract_pdf_text(file_path)

            if not text.strip():
                return JsonResponse(
                    {"error": "PDF contains no readable text"},
                    status=400
                )

            transcript_obj = Transcript.objects.create(
                uploaded_file=file_obj,
                full_text=text
            )

            return JsonResponse({
                "message": "PDF processed successfully",
                "transcript_id": transcript_obj.id,
                "file_url": file_obj.file.url
            })

        
        if file_kind in ["audio", "video"]:

            dg_response = transcribe_audio(file_path)

            results = dg_response["results"]
            alternative = results["channels"][0]["alternatives"][0]

            full_text = alternative["transcript"]

            transcript_obj = Transcript.objects.create(
                uploaded_file=file_obj,
                full_text=full_text
            )

            return JsonResponse({
                "message": "Transcription completed",
                "transcript_id": transcript_obj.id,
                "file_url": file_obj.file.url
            })

        return JsonResponse({
            "id": file_obj.id,
            "detected_type": "unknown"
        })




@method_decorator(csrf_exempt, name="dispatch")
class AskQuestionView(ApiBaseView):

    def post(self, request):

        transcript_id = request.POST.get("transcript_id")
        question = request.POST.get("question")

        if not transcript_id or transcript_id == "undefined":
            return JsonResponse(
                {"error": "Invalid transcript_id"},
                status=400
            )

        if not question:
            return JsonResponse(
                {"error": "Question is required"},
                status=400
            )

        try:
            transcript_id = int(transcript_id)
        except ValueError:
            return JsonResponse(
                {"error": "transcript_id must be integer"},
                status=400
            )

        result = answer_question(transcript_id, question)

        return JsonResponse(result)



@method_decorator(csrf_exempt, name="dispatch")
class SummaryView(ApiBaseView):

    def post(self, request):

        transcript_id = request.POST.get("transcript_id")

        if not transcript_id:
            return JsonResponse(
                {"error": "transcript_id required"},
                status=400
            )

        transcript = Transcript.objects.get(id=transcript_id)

        summary = summarize_text(transcript.full_text)

        return JsonResponse({
            "summary": summary
        })
