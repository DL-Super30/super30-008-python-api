# from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import generics
from django.contrib.auth import authenticate
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT,HTTP_401_UNAUTHORIZED
# from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

from .models import user
from .serializers import RegisterSerializer,LoginSerializer
class API(GenericAPIView):
    serializer_class=LoginSerializer,RegisterSerializer
class Register(generics.GenericAPIView):

    queryset = user.objects.all()
    serializer_class = RegisterSerializer
    # permission_classes=[permissions.IsAuthenticated]
class login(generics.GenericAPIView):

    queryset = user.objects.all()
    serializer_class = LoginSerializer
#     # permission_classes=[permissions.IsAuthenticated]
#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
        
#         user_name = serializer.validated_data['user_name']
#         password = serializer.validated_data['password']
        
#         user = authenticate(use_rname=user_name, password=password)
#         if user is not None:
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#             })
#         return Response({'detail': 'Invalid credentials'}, status=HTTP_401_UNAUTHORIZED)
    
    

    def destroy(self,request,pk=None):

        instance=self.get_object()

        instance.delete()

        return Response({"message":"record successfully deleted."},status=HTTP_204_NO_CONTENT)






