from rest_framework import serializers

from accounting.models import Company


class CompanySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.first_name')

    class Meta:
        model = Company
        fields = ["id", "name", "phone", "default_currency", "country", 'owner', ]


class CompanyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name", "phone", "default_currency", "country", "abbr", ]
