
from rest_framework import viewsets
# from rest_framework import permissions
from rest_framework .response import  Response 
from rest_framework.status import HTTP_204_NO_CONTENT



# Create your views here.
from. models import Login
from.serializers import LoginSerializer

class LoginViewSets(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
    # permission_classes=[permissions.IsAuthenticated]


