from django.shortcuts import render

# Create your views here.
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


def student_detail(request, pk):
    stu = Student.objects.get(id=pk)
    print(f"Data from Db {stu}")  # Complex Data :- Student model object

    # convert stydent object to python native
    serializer = StudentSerializer(stu)
    print(f"Data after serialization {serializer.data}")

    # convert json data which will be consumed by front-end framework

    json_data = JSONRenderer().render(serializer.data)
    print(f"Json data going to client {json_data}")
    return HttpResponse(
        json_data, content_type='application/json'
    )
