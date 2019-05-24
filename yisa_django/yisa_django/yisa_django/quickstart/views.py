from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from yisa_django.quickstart.models import Daoju,Shipin,Wupin,Yaowan,Chengjiu
from yisa_django.quickstart.serializers import UserSerializer, GroupSerializer,DaojuSerializer,ShipinSerializer,WupinSerializer,YaowanSerializer,ChengjiuSerializer

# Create your views here.


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


class DaojuViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Daoju.objects.all()
    serializer_class = DaojuSerializer


class ShipinViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Shipin.objects.all()
    serializer_class = ShipinSerializer


class WupinViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Wupin.objects.all()
    serializer_class = WupinSerializer


class YaowanViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Yaowan.objects.all()
    serializer_class = YaowanSerializer


class ChengjiuViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Chengjiu.objects.all()
    serializer_class = ChengjiuSerializer

