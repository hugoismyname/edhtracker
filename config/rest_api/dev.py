from rest_framework import authentication

from django.contrib.auth import get_user_model

User = get_user_model()

class Devauthentication(authentication.BasicAuthentication):
    def authenticate(self, request):
        user = User.objects.get(id=1) 
        
        return(user, None)