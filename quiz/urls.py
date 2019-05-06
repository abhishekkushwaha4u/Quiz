from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views,functions

urlpatterns = [
    path('questions/',views.multiple_choice_new.as_view()),
    path('add-questions/',views.add_question),
    path('quiz/',views.quiz_page),
    path('answer/',views.answer),
    path('random/',functions.random_questions),
    path('random-answer/',functions.customized_response),
]
