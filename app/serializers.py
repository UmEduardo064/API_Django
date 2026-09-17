from rest_framework import serializers
from .models import Grupo, Material

class GrupoSerializer(serializers.ModelSerializer):

    def validade_nome(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("O nome deve conter mais de 5 letras")

        if len(value) > 50:
            raise serializers.ValidationError("O nome deve conter menos de 50 Letras ")

    def validade_descricao(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("A descrição deve conter mais de 10 letras")

        if len(value) > 500:
            raise serializers.ValidationError("A descrição deve conter menos de 500 letras ")

    #def validate(self, value):
        #if value.nome == 'Mauricio':
            #raise serializers.ValidationError("O nome não pode ser 'Mauricio'")

    proprietario = serializers.CharField(write_only='True')
    class Meta:
        model = Grupo
        fields = ["id", "nome", "descricao", "proprietario"]

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ["id", "titulo", "conteudo", "grupo"]