from rest_framework.response import Response
from rest_framework.generics import ListAPIView, UpdateAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView

from article.models import Donation
from article.serializers import DonationSerializer
from .models import AccountType, AccountRole
from .serializers import AccountTypeSerializer, UserSecondarySerializer, AccountRoleSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated

User = get_user_model()


class AccountTypeSerializerAPIListView(ListAPIView):
    queryset = AccountType.objects.all()
    serializer_class = AccountTypeSerializer
    lookup_field = 'pk'
    permission_classes = (IsAuthenticatedOrReadOnly,)


class BlacklistRefreshView(APIView):
    def post(self, request):
        token = RefreshToken(request.data.get('refresh'))
        token.blacklist()
        return Response("Success")


class ProfileUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSecondarySerializer
    lookup_field = 'pk'
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class ProfileDetailAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSecondarySerializer
    lookup_field = 'pk'
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class UserProfileDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSecondarySerializer
    lookup_field = 'pk'
    permission_classes = (IsAuthenticated,)


class AccountRoleListView(ListAPIView):
    queryset = AccountRole.objects.all()
    serializer_class = AccountRoleSerializer
    lookup_field = 'pk'