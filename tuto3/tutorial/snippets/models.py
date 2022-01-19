from fileinput import lineno
from statistics import mode
from django.db import models

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0],item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item,item) for item in get_all_styles()])

class Snippet(models.Model):
    creacion = models.DateField(auto_now_add=True)
    titulo = models.CharField(max_length=100,blank=True, default='')
    codigo = models.TextField()
    linenos = models.BooleanField(default=False)
    lenguaje = models.CharField(choices=LANGUAGE_CHOICES,default='python',max_length=100)
    estilo = models.CharField(choices=STYLE_CHOICES, default= 'friendly', max_length=100)
    owner = models.ForeignKey('auth.User',related_name='snippets', on_delete=models.CASCADE)
    resaltado = models.TextField()

    class Meta:
        ordering = ['creacion']

    def save(self,*args, **kwargs):
        lexer = get_lexer_by_name(self.lenguaje)
        linenos = 'table' if self.linenos else False
        opciones = {'title':self.titulo} if self.titulo else {}
        formato = HtmlFormatter(style=self.estilo,linenos=linenos,full=True, **opciones)
        self.resaltado = highlight(self.codigo,lexer,formato)
        super().save(*args, **kwargs)
    
