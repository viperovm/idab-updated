from django.urls import path
from .views import EventBidView, ProgramBidView, PlanBidView, EducationBidView

urlpatterns = [
    path("eventbids/", EventBidView.as_view()),
    path("programbids/", ProgramBidView.as_view()),
    path("planbids/", PlanBidView.as_view()),
    path("educationbids/", EducationBidView.as_view()),
]