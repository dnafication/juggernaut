from rest_framework import viewsets, permissions
from .serializers import ScriptSerielizer, HostSerielizer, MappingSerielizer
from .serializers import TestSerielizer
from .models import Script, Host, Mapping, Test
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

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



def execute_test(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    return HttpResponse(content='test is started with')
    

def test_status(request, test_id):
    raise NotImplementedError()


def validate_script(request, script_id):
    script = get_object_or_404(Script, pk=script_id)
    script.validate()
    return HttpResponse(content='validating...')
