from rest_framework import serializers

class AdverticeSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=100)
    heading = serializers.CharField(max_length=100)
    picture = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=100)
    firm_name = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Advertice.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.subject = validated_data.get('subject', instance.subject)
        instance.heading = validated_data.get('heading', instance.heading)
        instance.picture = validated_data.get('picture', instance.picture)
        instance.description = validated_data.get('description', instance.description)
        instance.firm_name = validated_data.get('firm_name', instance.firm_name)
        instance.save()
        return instance
