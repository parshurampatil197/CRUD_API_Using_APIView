from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models.models import Student
from.serializers import StudentSerializer


class StudentView(APIView):

    def get(self, request, id=None):
        if id:
            queryset = Student.objects.get(id=id)
            serializers = StudentSerializer(queryset)
            return Response(serializers.data)

        queryset = Student.objects.all()
        serializers = StudentSerializer(queryset, many=True)
        return Response(serializers.data)

    def post(self, request):
        serialzer = StudentSerializer(data=request.data)

        if serialzer.is_valid(raise_exception=True):
            serialzer.save()
            return Response({"message": "success", "data": serialzer.data}, status=status.HTTP_201_CREATED)
        return Response({"message": "error", "data": serialzer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        record = Student.objects.get(id=id)
        serializer = StudentSerializer(record, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors)

    def delete(self, request, id=None):
        record = get_object_or_404(Student, id=id)
        record.delete()
        return Response({"message": "success", "data":"record deleted"}, status=status.HTTP_202_ACCEPTED)
