from rest_framework import serializers
from .models import Document, PrintJob
from orders.models import DeliveryAddress, PickupLocation
from accounts.models import User

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'
        read_only_fields = ('user', 'original_filename', 'file_type', 'uploaded_at')

class DeliveryAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryAddress
        fields = '__all__'
        read_only_fields = ('user',)

class PickupLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PickupLocation
        fields = '__all__'

class PrintJobSerializer(serializers.ModelSerializer):
    documents = DocumentSerializer(many=True, read_only=True)
    delivery_address = DeliveryAddressSerializer(read_only=True)
    pickup_location = PickupLocationSerializer(read_only=True)
    
    class Meta:
        model = PrintJob
        fields = '__all__'
        read_only_fields = ('user', 'status', 'created_at', 'updated_at', 'payment_completed')

class PrintJobCreateSerializer(serializers.ModelSerializer):
    documents = serializers.PrimaryKeyRelatedField(
        many=True, 
        queryset=Document.objects.all(),
        required=True
    )
    delivery_address_id = serializers.PrimaryKeyRelatedField(
        queryset=DeliveryAddress.objects.all(),
        source='delivery_address',
        required=False,
        allow_null=True
    )
    pickup_location_id = serializers.PrimaryKeyRelatedField(
        queryset=PickupLocation.objects.all(),
        source='pickup_location',
        required=False,
        allow_null=True
    )
    
    class Meta:
        model = PrintJob
        fields = [
            'documents', 
            'delivery_method',
            'delivery_address_id',
            'pickup_location_id',
            'payment_method'
        ]
    
    def validate(self, data):
        delivery_method = data.get('delivery_method')
        
        if delivery_method == 'delivery' and not data.get('delivery_address'):
            raise serializers.ValidationError("Delivery address is required for delivery method.")
        
        if delivery_method == 'pickup' and not data.get('pickup_location'):
            raise serializers.ValidationError("Pickup location is required for pickup method.")
        
        return data