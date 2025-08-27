
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Livre, Auteur
from .serializers import LivreSerializer, AuteurSerializer

class LivreViewSet(viewsets.ModelViewSet):
	queryset = Livre.objects.all()
	serializer_class = LivreSerializer

class AuteurViewSet(viewsets.ModelViewSet):
	queryset = Auteur.objects.all()
	serializer_class = AuteurSerializer

	def get_queryset(self):
		queryset = Auteur.objects.all()
		year = self.request.query_params.get('year')
		if year is not None:
			try:
				year_int = int(year)
				queryset = queryset.filter(date_naissance__year__gt=year_int)
			except ValueError:
				pass
		return queryset

	@action(detail=True, methods=['get'])
	def titres(self, request, pk=None):
		auteur = self.get_object()
		titres = list(auteur.livres.values_list('titre', flat=True))
		return Response({'titres': titres})
