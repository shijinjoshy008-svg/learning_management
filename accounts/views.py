from django.shortcuts import render
from rest_framework.views import APIView
from accounts.serializers import UserSerializer,TrainerprofileSerializer,StudentprofileSerializer
from accounts.models import User,TrainerProfile,StudentProfile
from rest_framework.response import Response
# Create your views here.

class UserCreateView(APIView):
    def post(self,request):
        form_data=request.data
        serializer_instance=UserSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            instance=User.objects.create_superuser(role="admin",**cleaned_data)
            serializer_instance=UserSerializer(instance)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class StudentcreateView(APIView):
    def post(self,request):
        form_data=request.data
        serializer_instance=StudentprofileSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            instance=StudentProfile.objects.create_user(role="student",**cleaned_data)
            serializer_instance=StudentprofileSerializer(instance)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class TrainercreateView(APIView):
    def post(self,request):
        form_data=request.data
        serializer_instance=TrainerprofileSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            instance=TrainerProfile.objects.create_user(role="trainer",**cleaned_data)
            serializer_instance=TrainerprofileSerializer(instance)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

# Create your views here.
