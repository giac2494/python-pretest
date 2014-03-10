import requests
import json
import argparse

HOST = 'localhost:8000'

def store_animal(nome):
    resp =requests.post(
        'http://{}/zoo'.format(HOST),
        json.dumps({'nome':nome}))
    if resp.status_code == 200:
        print 'OK'
    else:
        print 'Errore'

def list_all_animal():
    resp = requests.get('http://{}/zoo'.format(HOST))
    content = json.loads(resp.content)
    for animal in content:
        print animal['nome']+'\n'

def count_animal(nome):
    resp = requests.get('http://{}/zoo'.format(HOST))
    content = json.loads(resp.content)
    conta = 0
    for animal in content:
        if(animal['nome'] == nome):
            conta +=1
    print conta


parser = argparse.ArgumentParser('zoo client')
parser.add_argument('command')
parser.add_argument('--nome')
args = parser.parse_args()

if args.command == 'store':
    store_animal(args.nome)
elif args.command == 'list':
    list_all_animal()   
elif args.command == 'count':
    count_animal(args.nome)
else:
    print 'Errore'