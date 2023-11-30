from rest_framework import permissions, viewsets
from rest_framework.response import Response

from .models import Autor, Obra
from .serializers import AutorSerializer, ObraSerializer


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        autor = Autor.objects.get(pk=kwargs.get('pk'))
        if autor.obras.exists():
            return Response(
                {'autor': ['autor não pode ser excluido pois possui obras']}
            )
        return super().destroy(request, *args, **kwargs)


class ObraViewSet(viewsets.ModelViewSet):
    queryset = Obra.objects.all()
    serializer_class = ObraSerializer
    permission_classes = [permissions.IsAuthenticated]
