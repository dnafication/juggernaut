from django.contrib.auth.models import User, Group
from .models import Script, Host, ScriptHostMapping, Test
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ScriptSerielizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Script
        fields = ('url', 'name', 'script_upload')


class HostSerielizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Host
        fields = ('url', 'name', 'ip_address')


class ScriptHostMappingSerielizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ScriptHostMapping
        fields = ('url', 'script', 'host', 'test')


class TestSerielizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Test
        fields = ('url', 'name')
