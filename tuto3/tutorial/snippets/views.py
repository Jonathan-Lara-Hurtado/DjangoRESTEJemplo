from snippets.models import Snippet
from snippets.serializers import SnippetSerialiezer, UsuarioSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from django.contrib.auth.models import User

from rest_framework import permissions


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetalles(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer()




class SnippetList(APIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(propietario=self.request.user)


    def get(self, request ,format = None):
        snipets = Snippet.objects.all()
        serializer = SnippetSerialiezer(snipets,many=True)
        return Response(serializer.data)
    
    def post(self,request, format = None):
        serializer = SnippetSerialiezer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SnippetDetail(APIView):
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self,pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format = None):
        snippet = self.get_object(pk)
        serializer = SnippetSerialiezer(snippet)
        return Response(serializer.data)
    
    def put(self, request, pk, format= None):
        snippet = self.get_object(pk)
        serializer = SnippetSerialiezer(snippet,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 
    
    def delete(self, request, pk, format= None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)











'''
from os import stat
import re
from telnetlib import STATUS
from django.shortcuts import render

from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerialiezer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def snippet_list(request,format=None):
    """
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerialiezer(snippets,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerialiezer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk,format=None):
    try:
        snippet = Snippet.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SnippetSerialiezer(snippet)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = SnippetSerialiezer(snippet,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''


'''
@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerialiezer(snippets,many = True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerialiezer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)

@csrf_exempt
def snippet_detail(request,pk):
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerialiezer(snippet)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerialiezer(snippet,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status= 400)
    
    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)

'''