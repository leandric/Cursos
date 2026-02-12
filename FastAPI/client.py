import requests
import json

API_URL = 'http://127.0.0.1:8000'

def _tratar_respostas(resp: requests.Response):
    try:
        data = resp.json()
        print(data)
    except ValueError:
        print("\n Status {resp.status_code}")
        print("Resposta em json.")
        print(resp.text)
        return
    
    if resp.status_code >=400:
        print(f"\n Erro sem JSON.")
        print(json.dumps(data, index=True, ensure=ascii))

def get_livro():
    livro_uuid = input("UUID do livro: ").strip()
    resp = requests.get(f"{API_URL}/livros/{livro_uuid}")
    _tratar_respostas(resp)

def listar_livros():
    resp = requests.get(f"{API_URL}/livros")
    print("\n Listar Livros")
    _tratar_respostas(resp)


def menu():
    print('\n==== Cliente API de Livros =====')
    print("1. Listar Livros")
    print("2. Obter Livro por ID")
    print("0. Sair")

    opcao = input("Escolha a opção: ").strip()

    if opcao == "1":
        listar_livros()
    elif opcao == "2":
        get_livro()
    elif opcao == "0":
        raise

if __name__ == "__main__":
    menu()