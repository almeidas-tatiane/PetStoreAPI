import pytest
import requests

url = 'https://petstore.swagger.io/v2/pet'

def testar_incluir_pet():
    # Configura
    status_code_esperado = 200  # comunicação
    name_esperado = 'Toto'


    headers = {'Content-Type': 'application/json'}

    # Executa
    resposta = requests.post(f'{url}',
                             data=open('json/pets1.json', 'rb'), headers=headers)

    corpo_da_resposta = resposta.json()
    print(resposta)  # Status Code
    print(resposta.status_code)  # Status Code
    print(resposta.json())  # Response Body

    # Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['name'] == name_esperado

def testar_consultar_pet():
    # Configura
    petId = 10  # input / entrada para a consulta
    status_code_esperado = 200  # comunicação
    id_esperado= 10
    name_esperado = 'Toto'
    status_esperado = 'available'


    headers = {'Content-Type': 'application/json'}

    #Executa
    resposta = requests.get(f'{url}/{petId}', headers=headers)

    corpo_da_resposta = resposta.json()
    print(resposta)  # Status Code
    print(resposta.status_code)  # Status Code
    print(resposta.json())  # Response Body

    # Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['id'] == id_esperado
    assert corpo_da_resposta['name'] == name_esperado
    assert corpo_da_resposta['status'] == status_esperado

def testar_atualizar_pet():
    # Configura
    status_code_esperado = 200  # comunicação
    name_esperado = 'Miau'


    headers = {'Content-Type': 'application/json'}

    # Executa
    resposta = requests.post(f'{url}',
                             data=open('json/petsUpdated.json', 'rb'), headers=headers)

    corpo_da_resposta = resposta.json()
    print(resposta)  # Status Code
    print(resposta.status_code)  # Status Code
    print(resposta.json())  # Response Body

    # Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['name'] == name_esperado

def testar_deletar_pet():
    #Configura
    petId = 10  #input
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    messagem_esperada = '10'

    headers = {'Content-Type': 'application/json'}

    #Executa
    resposta = requests.delete(f'{url}/{petId}', headers=headers)


    corpo_da_resposta = resposta.json()
    print(resposta)
    print(resposta.status_code)
    print(resposta.json())

    # Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == messagem_esperada
