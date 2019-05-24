from django.contrib.auth.models import User, Group
from rest_framework import serializers
from yisa_django.quickstart.models import Daoju,Shipin,Wupin,Yaowan,Chengjiu

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class DaojuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Daoju
        fields = '__all__'


class ShipinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shipin
        fields = '__all__'

class WupinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wupin
        fields = '__all__'



class YaowanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Yaowan
        fields = '__all__'



class ChengjiuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chengjiu
        fields = '__all__'