import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TodoSerializer
from .models import todo
from .forms import TodoForm
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def todofn(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TodoForm()
        return render(request,'todo.html',{"form":form})
    
@api_view(['PUT'])
def manualapiedit(request,id):
    idforedit = todo.objects.get(id=id)
    serializerfortodo = TodoSerializer(data=request.data,instance = idforedit)

    if serializerfortodo.is_valid():
        serializerfortodo.save()
        return Response(serializerfortodo.data)
    else:
        return Response("Error")

@api_view(['DELETE'])
def manualapidelete(request,id):
    x = todo.objects.get(id=id)
    x.delete()
    return Response("Done")



@csrf_exempt
@api_view(['GET'])
def apitodo(request):
    TodoList = todo.objects.all()
    TodoJson = TodoSerializer(TodoList,many=True)

    return Response(TodoJson.data)

@csrf_exempt
def apiedittodo(request, t_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            item = todo.objects.get(id=t_id)
            item.title = data.get('title', item.title)
            item.description = data.get('description', item.description)
            item.save()
            return JsonResponse({'message': 'Updated successfully'})
        except todo.DoesNotExist:
            return JsonResponse({'error': 'Todo not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=405)

@csrf_exempt
def apideletetodo(request, t_id):
    if request.method == 'POST':
        try:
            item = todo.objects.get(id=t_id)
            item.delete()
            return JsonResponse({'message': 'Deleted successfully'})
        except todo.DoesNotExist:
            return JsonResponse({'error': 'Todo not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=405)
