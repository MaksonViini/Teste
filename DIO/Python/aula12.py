import requests


def return_data_cep(cep):
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

    print(response.status_code)
    print(response.json())

    dados_cep = response.json()

    print(dados_cep['localidade'])


def return_data_pokemon(pokemon):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')

    return response.json()


def retorn_response(url):
    response = requests.get(url)

    return response.text


if __name__ == '__main__':
    return_data_cep(39775000)
    # dados_pokemon = return_data_pokemon('pikachu')
    # print(dados_pokemon['sprites']['front_shiny'])
    # response = retorn_response('http://ww1.globallabs.academy/')
    # print(response)
