from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from . import models
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.serializers import ValidationError as RestValidationError
from rest_framework import status


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'username_or_email'

    def validate(self, attrs):
        password = attrs.get('password')
        user_obj = models.CustomUser.objects.filter(
            email=attrs.get('username_or_email')) or models.CustomUser.objects.filter(
            username=attrs.get('username_or_email'))
        if user_obj:
            credentials = {
                'email': user_obj[0].email,
                'password': password
            }
            if all(credentials.values()):
                user = authenticate(**credentials)
                if user:
                    refresh = self.get_token(user)
                    data = {
                        'success': True,
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                        'email': user.email,
                    }
                    return data
                else:
                    msg = 'Unable to login with provided credentials.'
                    raise RestValidationError(code=status.HTTP_400_BAD_REQUEST, detail=msg)

            else:
                msg = f'Must include "{self.username_field}" and "password".'
                msg = msg.format(username_field=self.username_field)
                raise RestValidationError(code=status.HTTP_400_BAD_REQUEST, detail=msg)
        else:
            msg = 'Account with this email/username does not exists'
            raise RestValidationError(code=status.HTTP_400_BAD_REQUEST, detail=msg)

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['email'] = user.email
        return token


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = '__all__'


class AsianIdentitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AsianIdentity
        fields = '__all__'


class WhatDoYouLikeDoingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WhatDoYouLikeDoing
        exclude = ['created_at', "updated_at"]


class AlmostDoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AlmostDone
        exclude = ['created_at', "updated_at"]


class GetSomeDetailsSerializer(serializers.ModelSerializer):
    asian = AsianIdentitySerializer()

    class Meta:
        model = models.GetSomeDetails
        fields = '__all__'

    def create(self, validated_data):
        asian_obj = validated_data.pop('asian')
        get_some_details = models.GetSomeDetails(**validated_data)
        get_some_details.save()
        asian_obj.update({"get_some_details": get_some_details})
        models.AsianIdentity.objects.create(**asian_obj)
        return get_some_details


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = models.CustomUser
        fields = ['email', 'first_name', 'last_name', 'profile', 'id', 'password']

    def create(self, validated_data):
        profile_obj = validated_data.pop('profile')
        user = models.CustomUser.objects.create_user(**validated_data)
        profile_obj.update({"user": user})
        models.Profile.objects.create(**profile_obj)
        return user
