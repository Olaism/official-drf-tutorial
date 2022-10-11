from django.https import HttpResponse, JsonResponse
from django.contrib.auth.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Snippet
from .serializers import SnippetSerializer

@csrf_exempt
def snippet_list(request):
    
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(snippets.data, safe=False)
        
    else if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=404)
        
        
        
@csrf_exempt
def snippet_detail(request, pk):
    try:
        snippet = Snippet.objects.get(pk=pk)
    except:
        HttpResponse(status=404)
        
    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)
    else if request.method == 'PUT':
        data = JSONParser.parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save() 
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    else if request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
        
        
        
        
        
        
          
        
        
        
        
        