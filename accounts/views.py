from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated
from . import serializers
from . import models
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.views import APIView
import boto3
from botocore.exceptions import NoCredentialsError
from accounts.custom_storage import MediaStorage
import os


class UserObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.UserTokenObtainPairSerializer


class AccountCreateView(CreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        """ Method for create user and user's profile. """

        data = request.data.copy()
        user_serializer_obj = self.serializer_class(data=data)
        user_serializer_obj.is_valid(raise_exception=True)
        user_serializer_obj.save()
        data['id'] = user_serializer_obj.instance.id
        return Response({"success": "Successfully created", "data": data},
                        status=status.HTTP_201_CREATED)


class RetrieveAccountView(RetrieveAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.RetrieveUserSerializer
    permission_classes = (IsAuthenticated,)


class AccountUpdateView(UpdateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        """ Method for update user's profile picture and what_you_like_doing field """
        
        try:
            data = request.data.copy()
            instance = self.get_object()
        except models.CustomUser.DoesNotExist:
            return Response({"error": "User doesn't exist"},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            if data.get('email'):
                if models.CustomUser.objects.filter(email=data.get('email')).exists():
                    return Response({"error": "User with this email is already exists"},
                                status=status.HTTP_400_BAD_REQUEST)
                instance.email = data.get('email')
            if data.get('current_password') and data.get('new_password'): 
                current_password = data.get('current_password')
                new_password = data.get('new_password')
                if instance.check_password(new_password):
                    return Response({"error": "New password should be different from current password"},
                                status=status.HTTP_400_BAD_REQUEST)
                instance.set_password(new_password)
            if data.get('first_name'):
                instance.first_name = data.get('first_name')

            if data.get('last_name'):
                instance.last_name = data.get('last_name')
            instance.save()
            return Response({"success": "Successfully created", "data": data},
                            status=status.HTTP_200_OK)


class BasicProfileCreateView(CreateAPIView):
    queryset = models.BasicProfile.objects.all()
    serializer_class = serializers.BasicProfileSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        """ Method for create user and user's profile. """

        data = request.data.copy()
        user_serializer_obj = self.serializer_class(data=data)
        user_serializer_obj.is_valid(raise_exception=True)
        user_serializer_obj.save()
        data['id'] = user_serializer_obj.instance.id
        return Response({"success": "Successfully created", "data": data},
                        status=status.HTTP_201_CREATED)


class RetrieveBasicProfile(RetrieveAPIView):
    queryset = models.BasicProfile.objects.all()
    serializer_class = serializers.BasicProfileSerializer
    permission_classes = (AllowAny,)


class UploadProfilePictureCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, requests):
        try:
            file_obj = requests.data.get('file', '')

            # do your validation here e.g. file size/type check

            # organize a path for the file in bucket
            file_directory_within_bucket = 'users_profile_pictures/{user_id}'.format(user_id=str(requests.user.id))

            # synthesize a full file path; note that we included the filename
            file_path_within_bucket = os.path.join(
                file_directory_within_bucket,
                file_obj.name
            )

            media_storage = MediaStorage()
            media_storage.save(file_path_within_bucket, file_obj)
            file_url = media_storage.url(file_path_within_bucket)

            return Response({
                'profile_image_url': file_url,
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)