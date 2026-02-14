from groq import Groq
from django.conf import settings
from ..models import Transcript



client = Groq(api_key=settings.GROQ_API_KEY)


def answer_question(transcript_id, question):


    transcript = Transcript.objects.get(id=transcript_id)


    context = transcript.full_text[:12000]


    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  
        messages=[
            {
                "role": "system",
                "content": "Answer ONLY using the provided transcript."
            },
            {
                "role": "user",
                "content": f"""
Transcript:
{context}

Question:
{question}
"""
            }
        ],
        temperature=0.3,
    )
    return {
        "answer": completion.choices[0].message.content
    }
