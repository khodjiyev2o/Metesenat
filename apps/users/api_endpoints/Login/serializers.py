from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from django.contrib.auth import authenticate
from apps.users.models import User


class LoginByEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        if email and password:
            user = authenticate(email=email, password=password)

            if user:
                if not user.is_active:
                    raise serializers.ValidationError('User account is disabled.')
                else:

                    return {
                        'token': user.tokens
                    }
            else:
                raise serializers.ValidationError('Parol yoki email notugri')
        else:
            raise serializers.ValidationError('Must include "email" and "password" fields.')