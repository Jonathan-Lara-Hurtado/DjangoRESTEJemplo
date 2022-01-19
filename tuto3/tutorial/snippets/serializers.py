from email.policy import default
from rest_framework import serializers
from snippets.models import Snippet,LANGUAGE_CHOICES,STYLE_CHOICES

from django.contrib.auth.models import User

class UsuarioSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True,queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id','username','snippets']


class SnippetSerialiezer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ['id','titulo','codigo','linenos','lenguaje','estilo','owner']


'''
version 1
class SnippetSerialiezer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    titulo = serializers.CharField(required=False,allow_blank=True,max_length=100)
    codigo = serializers.CharField(style={'base_template','textarea.html'})
    linenos = serializers.BooleanField(required=True)
    lenguaje = serializers.ChoiceField(choices=LANGUAGE_CHOICES,default='python')
    estilo = serializers.ChoiceField(choices=STYLE_CHOICES,default='friendly')


    def create(self, validated_data):
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.titulo = validated_data.get('titulo',instance.titulo)
        instance.codigo = validated_data.get('codigo',instance.codigo)
        instance.linenos = validated_data.get('linenos',instance.linenos)
        instance.lenguaje = validated_data.get('lenguaje',instance.lenguaje)
        instance.estilo = validated_data.get('estilo',instance.estilo)        
        instance.save()
        return instance
'''