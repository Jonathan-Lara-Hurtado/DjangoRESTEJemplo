from email.policy import default
from turtle import title
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

#creando un serializador del modelo 
#snipppet pero con con ayuda de ModelSerializer

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'titulo', 'codigo',
                    'linenos','lenguaje','estilos']





'''
#Creando un serializador del modelo snippet desde cero

class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only =True)
    titulo = serializers.CharField(required = False, allow_blank = True, max_length= 100)
    codigo = serializers.CharField(style = {'base_template':'textarea.html'})
    linenos = serializers.BooleanField(required = True)
    lenguaje = serializers.ChoiceField(choices = LANGUAGE_CHOICES,default='python')
    estilos = serializers.ChoiceField(choices = STYLE_CHOICES,default = 'friendly')

    def create(self, validated_data):
        return Snippet.objects.create(**validated_data)

    
    def update(self, instance, validated_data):
        instance.titulo = validated_data.get('titulo', instance.titulo)
        instance.codigo = validated_data.get('codigo', instance.codigo)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.lenguaje = validated_data.get('languaje', instance.lenguaje)
        instance.estilo = validated_data.get('estilo', instance.estilos)
        instance.save()
        return instance
'''