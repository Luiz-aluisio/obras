from datetime import date

from rest_framework import serializers

from .models import Autor


class AutorSerializer(serializers.HyperlinkedModelSerializer):
    def validate(self, attrs):
        if attrs.get('nacionalidade') == 'BR' and not attrs.get('cpf'):
            raise serializers.ValidationError(
                {'cpf': 'se nacionalidade brasil cpf obrigatorio'}
            )
        if attrs.get('nacionalidade') != 'BR' and attrs.get('cpf'):
            raise serializers.ValidationError(
                {'cpf': ['cpf somente para nacionalidade brasil']}
            )
        hoje = date.today()

        if attrs.get('data_nascimeto') > hoje:
            raise serializers.ValidationError(
                {
                    'data_nascimeto': [
                        f'Certifique-se que este valor seja menor ou igual a {hoje}.'
                    ]
                }
            )
        return super().validate(attrs)

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
