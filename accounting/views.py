from rest_framework import generics

from accounting.models import Company
from accounting.serializers import CompanySerializer, CompanyDetailSerializer


class CompanyList(generics.ListCreateAPIView):
    """
    List all current user companies
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get one company where the current user is authorize to manage
    """
    queryset = Company.objects.all()
    serializer_class = CompanyDetailSerializer
