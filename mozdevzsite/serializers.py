from rest_framework import serializers
from .models import Program, Geral, Embassador, Contact, Person


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ('id', 'title', 'description', 'logo')


class GeralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geral
        fields = ('id', 'quemSomos', 'visao','oqueFazemos')


class EmbassadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Embassador
        fields = ('id', 'name', 'site', 'logo')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'email', 'subject', 'message')


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'fullname', 'team', 'ocupation', 'picture')