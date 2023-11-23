from rest_framework import serializers

from .models import Autor


class AutorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Autor
        fields = [
            'id',
            'nome',
            'sexo',
            'email',
            'data_nascimeto',
            'nacionalidade',
            'cpf',
        ]
