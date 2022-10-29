from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import AccountType

User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'name', 'password')


class AccountTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountType
        fields = ('account_type',)


class UserSecondarySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'address', 'profile_picture')

        def update(self, instance, validated_data):
            first_name = validated_data.pop('first_name', None)
            last_name = validated_data.pop('last_name', None)
            email = validated_data.pop('email', None)
            phone = validated_data.pop('phone', None)
            profile_picture = validated_data.pop('profile_picture', None)
            address = validated_data.pop('address', None)
            return super().update(instance, validated_data)
