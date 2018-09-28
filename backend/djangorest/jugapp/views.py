from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, GroupSerializer, ScriptSerielizer, HostSerielizer, ScriptHostMappingSerielizer
from .serializers import TestSerielizer
from .models import Script, Host, ScriptHostMapping, Test


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ScriptViewSet(viewsets.ModelViewSet):
    queryset = Script.objects.all()
    serializer_class = ScriptSerielizer


class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerielizer


class ScriptHostMappingViewSet(viewsets.ModelViewSet):
    queryset = ScriptHostMapping.objects.all()
    serializer_class = ScriptHostMappingSerielizer


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerielizer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

