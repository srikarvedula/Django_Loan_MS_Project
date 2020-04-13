from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .model_loan_table_lookup import LoanTableLookup
from .serializers import LoanTableLookupSerializer


@api_view(['GET', 'POST'])
def ws_test(request):
    if request.method == "GET":
        return Response({"data": "GET Example"}, status=status.HTTP_200_OK)
    elif request.method == "POST":
        return Response({"data": "POST Example."}, status=status.HTTP_200_OK)
    else:
        data = {"Error": {"status": 400,"message": "Request Error"}}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def all_projects(request):
    if request.method == 'GET':
        projects = LoanTableLookup.objects.all()
        serializer = LoanTableLookupSerializer(projects, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LoanTableLookupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def single_project(request, in_proj_id):
    try:
        project = LoanTableLookup.objects.get(proj_id=in_proj_id)
    except LoanTableLookup.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LoanTableLookupSerializer(project, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LoanTableLookupSerializer(project, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)