from rest_framework import serializers
from .models import Recruteur
from candidats.models import Candidat
from candidats.serializers import CandidatSerializer



class RecruteurSerializer(serializers.ModelSerializer):
    candidats_vus = CandidatSerializer(many=True, read_only=True)

    class Meta:
        model = Recruteur
        fields = '__all__'
