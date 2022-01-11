from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from . import serializers
from . import models
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, UpdateAPIView


class UserObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.UserTokenObtainPairSerializer


class AccountCreateView(CreateAPIView, UpdateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        """ Method for create user and user's profile. """

        data = request.data.copy()
        user_serializer_obj = self.serializer_class(data=data)
        user_serializer_obj.is_valid(raise_exception=True)
        user_serializer_obj.save()
        return Response({"success": "Successfully created", "data": data},
                        status=status.HTTP_201_CREATED)


class AccountUpdateView(UpdateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (AllowAny,)
    # lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        """ Method for update user's profile picture and what_you_like_doing field """
        
        try:
            data = request.data.copy()
            instance = self.get_object()
        except models.CustomUser.DoesNotExist:
            return Response({"error": "User doesn't exist"},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            user_serializer_obj = serializers.UserProfileSerializer(instance.profile, data=data, partial=True)
            user_serializer_obj.is_valid(raise_exception=True)
            user_serializer_obj.save()
            return Response({"success": "Successfully created", "data": user_serializer_obj.data},
                            status=status.HTTP_200_OK)

