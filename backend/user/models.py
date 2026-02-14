from django.db import models


class UploadedFile(models.Model):
    file = models.FileField(upload_to="uploads/")
    file_type = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name


class Transcript(models.Model):
    uploaded_file = models.OneToOneField(
        UploadedFile,
        on_delete=models.CASCADE,
        related_name="transcript"
    )

  
    full_text = models.TextField()


    summary = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transcript for file {self.uploaded_file.id}"
