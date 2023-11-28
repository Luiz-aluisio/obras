from datetime import date

from rest_framework import serializers

from .models import Autor, Obra


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


class ObraSerializer(serializers.HyperlinkedModelSerializer):
    def validate(self, attrs):
        if (
            attrs.get('data_de_exposicao') is None
            and attrs.get('data_de_publicacao') is None
        ):
            raise serializers.ValidationError(
                {
                    'data_de_exposicao': [
                        'obrigatoria caso a data de publicacao nao seja informada'
                    ],
                    'data_de_publicacao': [
                        'obrigatoria caso a data de exposicao não seja informada'
                    ],
                }
            )
        return super().validate(attrs)

    class Meta:
        model = Obra
        fields = [
            'nome',
            'descricao',
            'data_de_exposicao',
            'data_de_publicacao',
        ]
