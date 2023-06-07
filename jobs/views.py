from django.forms import model_to_dict
from rest_framework.views import APIView, Request, Response, status
from .models import Job
from .exceptions import NotAcceptApplicationsError


class JobView(APIView):
    def post(self, request: Request) -> Response:
        created_job = Job.objects.create(**request.data)
        created_job.save()
        job = model_to_dict(created_job)
        return Response(job, status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        jobs = Job.objects.all()
        jobs_dict = []
        for job in jobs:
            jobs_dict.append(model_to_dict(job))
        # ou
        # jobs_dict = [model_to_dict(job) for job in jobs] List comprenhesion
        return Response(jobs_dict)


class JobDetailView(APIView):
    def get(self, request: Request, job_id: int) -> Response:
        job = Job.objects.get(id=job_id)
        job_dict = model_to_dict(job)
        return Response(job_dict)

    def patch(self, request: Request, job_id: int) -> Response:
        job = Job.objects.get(id=job_id)
        for key, value in request.data.items():
            setattr(job, key, value)
        job.save()
        job_dict = model_to_dict(job)
        return Response(job_dict)


class ApplicationsJobViews(APIView):
    def post(self, request: Request, job_id: int) -> Response:
        job = Job.objects.get(id=job_id)

        if job.accepting_applicsations:
            if not job.received_applications:
                job.received_applications = 1
            else:
                job.received_applications += 1
                job.save()

            return Response(
                {"message": "Candidatura recebida com sucesso"}, status.HTTP_201_CREATED
            )
        # return Response(
        #     {"message": "Não aceita a candidatura!"}, status.HTTP_400_BAD_REQUEST
        # )

        raise NotAcceptApplicationsError({"message": "Não aceita a candidatura!"})
