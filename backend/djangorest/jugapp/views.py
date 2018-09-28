from rest_framework import viewsets, permissions
from .serializers import ScriptSerielizer, HostSerielizer, MappingSerielizer
from .serializers import TestSerielizer
from .models import Script, Host, Mapping, Test

class ScriptViewSet(viewsets.ModelViewSet):
    queryset = Script.objects.all()
    serializer_class = ScriptSerielizer


class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerielizer


class MappingViewSet(viewsets.ModelViewSet):
    queryset = Mapping.objects.all()
    serializer_class = MappingSerielizer


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerielizer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

