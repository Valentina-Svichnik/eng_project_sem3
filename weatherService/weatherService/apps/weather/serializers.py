from rest_framework import serializers

class WeatherSerializer(serializers.Serializer):
    id_district = serializers.CharField(max_length=100)
    name_precipitation = serializers.CharField(max_length=100)
    icon_precipitation = serializers.CharField(max_length=100)
    name_cloud = serializers.CharField(max_length=100)
    icon_cloud = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Day.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id_district = validated_data.get('id_district', instance.id_district)
        instance.name_precipitation = validated_data.get('name_precipitation', instance.name_precipitation)
        instance.icon_precipitation = validated_data.get('icon_precipitation', instance.icon_precipitation)
        instance.name_cloud = validated_data.get('name_cloud', instance.name_cloud)
        instance.icon_cloud = validated_data.get('icon_cloud', instance.icon_cloud)
        instance.save()
        return instance
