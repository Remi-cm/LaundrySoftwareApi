from rest_framework import serializers
from . import models

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'sex', 'address', 'gpsLat', 'gpsLng', 'avatarUrl', 'is_client', 'phone', 'country', 'town', 'cni_number', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = models.UserProfile(
            email = validated_data['email'],
            name = validated_data['name'],
            sex = validated_data['sex'],
            address = validated_data['address'],
            gpsLat = validated_data['gpsLat'],
            gpsLng = validated_data['gpsLng'],
            avatarUrl = validated_data['avatarUrl'],
            is_client = validated_data['is_client'],
            phone = validated_data['phone'],
            country = validated_data['country'],
            town = validated_data['town'],
            cni_number = validated_data['cni_number'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class AgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'phone', 'is_client', 'address', 'gpsLat', 'gpsLng', 'avatarUrl', 'country', 'town', 'cni_number', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        '''
        user = models.UserProfile(
            email = validated_data['email'],
            name = validated_data['name'],
            phone = validated_data['phone'],
            is_client = validated_data['is_client'],
            cni_number = validated_data['cni_number'],
            address = validated_data['address'],
            gpsLat = validated_data['gpsLat'],
            gpsLng = validated_data['gpsLng'],
            avatarUrl = validated_data['avatarUrl'],
            country = validated_data['country'],
            town = validated_data['town'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
        '''
        return models.UserProfile.objects.create_agency(**validated_data)

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'phone', 'is_client', 'sex', 'address', 'gpsLat', 'gpsLng', 'avatarUrl', 'country', 'town', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return models.UserProfile.objects.create_client(**validated_data)



class ShipperSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Shipper
        fields = ('id', 'agent', 'cni_number', 'phone', 'name', 'email', 'address', 'created_on')
        extra_kwargs = {'agent' : {'read_only': True}}

class ShipperNestedSerializer(serializers.ModelSerializer):
    agent = AgencySerializer()
    class Meta:
        model = models.Shipper
        fields = ('id', 'agent', 'cni_number', 'phone', 'name', 'email', 'address', 'created_on')
        extra_kwargs = {'agent' : {'read_only': True}}


class LaundrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Laundry
        fields = ('id', 'shipper', 'client', 'agency', 'description', 'time_submitted', 'time_expected', 'imgUrl', 'status', 'onDelivery', 'price_estimated')

class LaundryListSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    shipper = ShipperSerializer();
    class Meta:
        model = models.Laundry
        fields = ('id', 'shipper', 'client', 'agency', 'description', 'time_submitted', 'time_expected', 'imgUrl', 'status', 'onDelivery', 'price_estimated')
        extra_kwargs = {'client' : {'read_only': True}, 'shipper' : {'read_only': True}, 'agency' : {'read_only': True} }


class ClotheSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Clothe
        fields = ('id', 'name', 'price')
        extra_kwargs = {'id' : {'read_only': True}}

class OrderLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderLine
        fields = ('id', 'laundry', 'clothe', 'color', 'description', 'quantity', 'price', 'laundry_key')
        extra_kwargs = {'id' : {'read_only': True}}

class OrderLineDetailSerializer(serializers.ModelSerializer):
    laundry = LaundryListSerializer()
    clothe = ClotheSerializer()
    class Meta:
        model = models.OrderLine
        fields = ('id', 'laundry', 'clothe', 'color', 'description', 'quantity', 'price', 'laundry_key')
        extra_kwargs = {'id' : {'read_only': True}}

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = ('id', 'laundry', 'reference', 'amount', 'payment_method', 'date')

class OrderDetailSerializer(serializers.ModelSerializer):
    laundry = LaundryListSerializer()
    class Meta:
        model = models.Order
        fields = ('id', 'laundry', 'reference', 'amount', 'payment_method', 'date')
        extra_kwargs = {'laundry' : {'read_only': True}}