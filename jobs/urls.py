from django.urls import path
from .views import JobDetailView, JobView, ApplicationsJobViews

urlpatterns = [
    path("jobs/", JobView.as_view()),
    path("jobs/<int:job_id>/", JobDetailView.as_view()),
    path("jobs/<int:job_id>/apply/", ApplicationsJobViews.as_view()),
]
