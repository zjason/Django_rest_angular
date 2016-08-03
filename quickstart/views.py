from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer
from django.shortcuts import render
from django.http import HttpResponse


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

def index(request):
    return render(request, 'quickstart/login.html', context=None)

def signup(request):
    dt = request.POST
    print "username: ",dt['Username']," Password: ", dt['Password']
    #return HttpResponse("<h1>username: "+str(dt['Username'])+" Password: "+str(dt['Password'])+"</h1>")
    user = authenticate(username=dt['Username'],password=dt['Password'])
    if user is not None:
        return HttpResponse("enter another name")
    else:
        user = User.objects.create_user(dt['Username'], '', dt['Password'])
        return HttpResponse('Success')
