from rest_framework import serializers
from .models.models import Student


class StudentSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=255, required=True)
    last_name = serializers.CharField(max_length=255, required=True)
    address = serializers.CharField(max_length=255, required=True)
    roll_number = serializers.IntegerField( required=True)
    mobile = serializers.CharField(max_length=14, required=True)

    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Students` instance, given the validated data.
        """
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.address = validated_data.get('address', instance.address)
        instance.roll_number = validated_data.get('roll_number', instance.roll_number)
        instance.mobile = validated_data.get('mobile', instance.mobile)

        instance.save()
        return instance
