from rest_framework import permissions, viewsets

from .models import Autor
from .serializers import AutorSerializer


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = [permissions.IsAuthenticated]
