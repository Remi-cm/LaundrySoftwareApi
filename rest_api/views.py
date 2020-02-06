from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from . import serializers
from . import models
from . import permissions

# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile, IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')

class AgencyViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AgencySerializer
    queryset = models.UserProfile.objects.filter(is_client = 0)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('is_client')

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClientSerializer
    queryset = models.UserProfile.objects.filter(is_client = 1)
    permission_classes = (permissions.UpdateOwnProfile, IsAdminUser,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('is_client')

class ShipperViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ShipperSerializer
    queryset = models.Shipper.objects.all()
    def perform_create(self, serializer):
        serializer.save(agent=self.request.user)

class ShipperNestedViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ShipperNestedSerializer
    queryset = models.Shipper.objects.all()


class LaundryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.LaundrySerializer
    #queryset = models.Laundry.objects.all()
    def get_queryset(self):
        queryset = models.Laundry.objects.all()
        agency = self.request.query_params.get('agency', None)
        status = self.request.query_params.get('status', None)
        if agency is not None:
            return queryset.filter(agency=agency)
        if status is not None:
            return queryset.filter(status=status)
        return queryset

class LaundryListViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.LaundryListSerializer
    def get_queryset(self):
        queryset = models.Laundry.objects.all()
        status = self.request.query_params.get('status', None)
        if status is not None:
            return queryset.filter(status=status)
        return queryset

class ClotheViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ClotheSerializer
    queryset = models.Clothe.objects.all()

class OrderLineViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    serializer_class = serializers.OrderLineSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('laundry',)
    #queryset = models.OrderLine.objects.filter(laundry=9)
    def get_queryset(self):
        queryset = models.OrderLine.objects.all()
        laundry = self.request.query_params.get('laundry', None)
        if laundry is not None:
            return queryset.filter(laundry=laundry)
        return queryset
        #return models.OrderLine.objects.filter(laundry=self.kwargs["laundry"])

class OrderLineDetailViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.OrderLineDetailSerializer
    queryset = models.OrderLine.objects.all()
    def get_queryset(self):
        queryset = models.OrderLine.objects.all()
        laundry = self.request.query_params.get('laundry', None)
        if laundry is not None:
            return queryset.filter(laundry_key=laundry)
        return queryset

class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.OrderSerializer
    queryset = models.Order.objects.all()

class OrderDetailViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.OrderDetailSerializer
    queryset = models.Order.objects.all()


class CurrentUserView(APIView):
    def get(self, request):
        serializer = serializers.UserProfileSerializer(request.user)
        return Response({
              'email': user.email, 
               })

    def get_object(self):
        return self.request.user

    def list(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class LoginViewSet(viewsets.ViewSet):
    serializer_class = AuthTokenSerializer
    def create(self, request):
        return ObtainAuthToken().post(request)