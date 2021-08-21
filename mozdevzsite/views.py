from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

# Create your views here.
class ProgramView(viewsets.ModelViewSet):
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()


class GeralView(viewsets.ModelViewSet):
    serializer_class = GeralSerializer
    queryset = Geral.objects.all()


class EmbassadorView(viewsets.ModelViewSet):
    serializer_class = EmbassadorSerializer
    queryset = Embassador.objects.all()


class ContactView(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class PersonView(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()