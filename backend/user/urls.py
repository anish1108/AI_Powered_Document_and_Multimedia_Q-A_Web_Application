
from django.urls import path
from .views import FileUploadView, AskQuestionView, SummaryView
urlpatterns = [
    
     path('upload/', FileUploadView.as_view()),
     path("ask/", AskQuestionView.as_view()),
     path("summary/", SummaryView.as_view()),

]
