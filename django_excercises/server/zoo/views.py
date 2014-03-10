from django.shortcuts import render
from zoo.models import animals
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def home(request):
    if request.method == 'POST':
        #aggiungiamo un animale nel db
        body = request.body
        content = json.loads(body)
        animal = animals(nome=content['nome'])
        animal.save()
        return HttpResponse(status=200)
    elif request.method == 'GET':
        #leggiamo da db e ritorniamo al client
        animal = animals.objects.all()
        list_animal = [{'nome':a.nome}for a in animal]
        resp = json.dumps(list_animal)
        return HttpResponse(resp, content_type='application/json')


