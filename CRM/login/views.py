# from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView

# Create your views here.

from .models import Loginuser
from .serializers import Leadserializer
class API(GenericAPIView):
    serializer_class=Leadserializer
class login(viewsets.ModelViewSet):

    queryset = Loginuser.objects.all()
    serializer_class = Leadserializer
    # permission_classes=[permissions.IsAuthenticated]

    # def  addmodule(request):

    #         f=forms.Leadmoduleform()
    #         if Leadmodules.method=="POST":
    #             f=Leadmoduleform(request.POST)
    #             if f.is_valid():
    #                 f.save()
    #                 print(f.is_valid())
    #                 return HttpResponse("Data submitted")
    #             else:
    #                 print(f.is_valid)
    #                 print(f.errors)
    #         else:
    #             f= Leadmoduleform()

                        






