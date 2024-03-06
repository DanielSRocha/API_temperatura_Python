import requests

def obter_previsao_tempo(cidade, chave_api):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&lang=pt_br"

    resposta = requests.get(url)
    dados = resposta.json()

    if resposta.status_code == 200:
        return dados
    else:
        return None

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

if __name__ == "__main__":
    cidade = input("Digite o nome da cidade: ")
    chave_api = "cff457ab15170d3438221605ba4fb23c" 

    previsao_tempo = obter_previsao_tempo(cidade, chave_api)

    if previsao_tempo:
        temperatura_celsius = kelvin_para_celsius(previsao_tempo['main']['temp'])
        print("Previsão do Tempo:")
        print(f"Cidade: {previsao_tempo['name']}")
        print(f"Condição: {previsao_tempo['weather'][0]['description']}")
        print(f"Temperatura: {temperatura_celsius:.2f}°C")
        print(f"Umidade: {previsao_tempo['main']['humidity']}%")
        print(f"Pressão: {previsao_tempo['main']['pressure']} hPa")
    else:
        print("Falha ao obter a previsão do tempo.")
