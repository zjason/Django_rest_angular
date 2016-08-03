from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from models import houseinfo
from serializers import HouseinfoSerializer
from django.http import HttpResponse
from django.template import loader
from rest_framework.generics import DestroyAPIView

# Create your views here.
# list all house or create a new one
# class houseList(APIView):
#     def get(self, request):
#         houses = houseinfo.objects.all()
#         serializer = HouseinfoSerializer(houses, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = HouseinfoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def index(request):
    template = loader.get_template('../templates/APItest.html')
    return HttpResponse(template.render())

@api_view(['GET', 'POST'])
def house_list(request):
    if request.method == 'GET':
        houses = houseinfo.objects.all()
        serializer = HouseinfoSerializer(houses, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = HouseinfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT', 'DELETE'])
def house_detail(request, pk):
    try:
        house = houseinfo.objects.get(pk=pk)
    except houseinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HouseinfoSerializer(house)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = HouseinfoSerializer(house, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        house.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def house_query(request, condition):
    try:
        if condition is None:
            query_result = houseinfo.objects.all()
        else:
            query_result = houseinfo.objects.filter(price__lt=condition).order_by('price')
    except houseinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HouseinfoSerializer(query_result, many=True)
        return Response(serializer.data)