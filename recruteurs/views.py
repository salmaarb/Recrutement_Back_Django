from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Recruteur
from candidats/models import Candidat

from .serializers import  RecruteurSerializer
from candidats/serializers import CandidatSerializer





class RecruteurViewSet(viewsets.ModelViewSet):
    queryset = Recruteur.objects.all()
    serializer_class = RecruteurSerializer

    @action(detail=False, methods=['get'], url_path='voir-tous-les-candidats')
    def voir_tous_les_candidats(self, request):
        """
        Retourne tous les candidats pour le recruteur.
        """
        candidats = Candidat.objects.all()
        serializer = CandidatSerializer(candidats, many=True)
        return Response(serializer.data)



    @action(detail=True, methods=['post'], url_path='ajouter-fav/(?P<id_candidat>[^/.]+)')
    def ajouter_favori(self, request, pk=None, id_candidat=None):
        recruteur = self.get_object()

        try:
            candidat = Candidat.objects.get(pk=id_candidat)
        except Candidat.DoesNotExist:
            return Response({"detail": "Candidat introuvable."}, status=status.HTTP_404_NOT_FOUND)

        recruteur.candidats_vus.add(candidat)
        return Response({"detail": f"Candidat (id={id_candidat}) ajouté aux favoris."})