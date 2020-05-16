from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import Hospitals
from rest_framework import status 
from rest_framework.parsers import JSONParser
from django.db.models.functions import Concat
from django.db.models import Value
from hospital.serializer import HospitalsSerializer
from rest_framework.response import Response 
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.


class HospitalName(APIView):
    def get(self, request, format= None):
        state = request.GET.get('state')
        city = request.GET.get('city')
        category = request.GET.get('category')
        if city is not None and state is not None:
            if category is None: 
                queryset = Hospitals.objects.filter(state = state,city=city)
                serializer = HospitalsSerializer(queryset, many=True)
                return Response(serializer.data, status = status.HTTP_200_OK)
            else: 
                queryset = Hospitals.objects.filter(state = state,city=city,category=category)
                serializer = HospitalsSerializer(queryset, many=True)
                return Response(serializer.data, status = status.HTTP_200_OK)
        if city is not None:
            if category is None:
                queryset = Hospitals.objects.filter(city = city)
                serializer = HospitalsSerializer(queryset, many=True)
                return Response(serializer.data, status = status.HTTP_200_OK)
            else: 
                queryset = Hospitals.objects.filter(city = city, category = category)
                serializer = HospitalsSerializer(queryset, many=True)
                return Response(serializer.data, status = status.HTTP_200_OK)
        if state is not None:
            if category is None: 
                queryset = Hospitals.objects.filter(state = state)
                serializer = HospitalsSerializer(queryset, many=True)
                return Response(serializer.data, status = status.HTTP_200_OK)
            else:
                queryset = Hospitals.objects.filter(state = state, category = category)
                serializer = HospitalsSerializer(queryset, many=True)
                return Response(serializer.data, status = status.HTTP_200_OK)
        
