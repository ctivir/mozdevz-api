from rest_framework import serializers
from .models import Program, Geral, Embassador, Contact, Person


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ('id', 'title', 'description', 'img_url')


class GeralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geral
        fields = ('id', 'description', 'logo')


class EmbassadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Embassador
        fields = ('id', 'name', 'site', 'img_url')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'email', 'subject', 'message')


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'fullname', 'team', 'ocupation', 'img_url')