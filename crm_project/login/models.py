from django.db import models


class Login(models.Model):
    username = models.CharField(max_length=55)
    password = models.CharField(max_length=55)

# #modified data    

#     def __str__(self):
#         return self.username
