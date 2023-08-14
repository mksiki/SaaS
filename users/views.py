from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import logout, get_user_model

User = get_user_model()

# Create your views here.
def home(request):
     return render(request, 'home.html')


def logout_view(request):
     logout(request)
     return redirect('/')


# Get all users
@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

# Get a single user
@api_view(['GET'])
def getUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

# Add user
@api_view(['POST'])
def addUser(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Update user
@api_view(['POST'])
def updateUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Delete user
@api_view(['DELETE'])
def deleteUser(request, pk):
        user = User.objects.get(id=pk)
        user.delete()
        return Response('Successfully deleted!')