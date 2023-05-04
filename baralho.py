import requests

naipe_escolhido = input("Insira o naipe da carta: ").upper()
numero_escolhido = input("Insira o número da carta: ").upper()
naipe_comprado = 0
numero_comprado = 0

api_url = 'https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1'
response = requests.get(api_url)
baralho = response.json()
baralho["deck_id"]

comprar_carta = f'https://deckofcardsapi.com/api/deck/{baralho["deck_id"]}/draw/?count=1'

carta_procurada = False

while not carta_procurada:
    if naipe_comprado == naipe_escolhido and numero_comprado == numero_escolhido:
        print(f'Acertei! A carta escolhida é: {deck["cards"][0]["value"]} de {deck["cards"][0]["suit"]}')
        carta_procurada = True
    else:
        carta_comprada = requests.get(comprar_carta)
        deck = carta_comprada.json()
        print(f'Comprada a carta {deck["cards"][0]["value"]} de {deck["cards"][0]["suit"]}')
        naipe_comprado = (deck["cards"][0]["suit"])
        numero_comprado = (deck["cards"][0]["value"])
