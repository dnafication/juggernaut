from .models import Script, Host, Mapping, Test
from rest_framework import serializers


class ScriptSerielizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Script
        fields = ('url', 'name', 'script_upload')


class HostSerielizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Host
        fields = ('url', 'name', 'ip_address')


class MappingSerielizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mapping
        fields = ('url', 'script', 'host', 'test')


class TestSerielizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Test
        fields = ('url', 'name', 'scripts')
