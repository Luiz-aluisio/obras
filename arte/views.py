from rest_framework import permissions, viewsets

from .models import Autor, Obra
from .serializers import AutorSerializer, ObraSerializer


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = [permissions.IsAuthenticated]


class ObraViewSet(viewsets.ModelViewSet):
    queryset = Obra.objects.all()
    serializer_class = ObraSerializer
    permission_classes = [permissions.IsAuthenticated]
