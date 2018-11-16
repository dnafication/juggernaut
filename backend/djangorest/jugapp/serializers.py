from .models import Script, Host, Mapping, Test
from rest_framework import serializers


class ScriptSerielizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Script
        fields = "__all__"


class HostSerielizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Host
        fields = ('url', 'name', 'ip_address', 'is_active')


class MappingSerielizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mapping
        fields = ('url', 'script', 'host', 'test')


class TestSerielizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"
        
