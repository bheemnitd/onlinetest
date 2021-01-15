from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from .models import MultipleChoice, ShortAns, ImageAns
from rest_framework.viewsets import ModelViewSet
from .serializers import MultipleChoiceSerializer, ShortAnsSerializer, ImageAnsSerializer

# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
# class UserCRUDCBV(ModelViewSet):
    
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class MultipleChoiceCRUDCBV(ModelViewSet):
    
    queryset = MultipleChoice.objects.all()
    serializer_class = MultipleChoiceSerializer

class ShortAnsCRUDCBV(ModelViewSet):
    
    queryset = ShortAns.objects.all()
    serializer_class = ShortAnsSerializer

class ImageAnsCRUDCBV(ModelViewSet):
    
    queryset = ImageAns.objects.all()
    serializer_class = ImageAnsSerializer

class Index(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'exam/index.html')

