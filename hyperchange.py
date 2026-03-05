import requests
token = str(input("Coloque seu token do discord\n> "))
choice = int(input("Escolha um Hypesquad, 3:Balance, 2:Brilliance, 1:Bravery\n> "))

headers = {
    'authorization': token
}
body = {
    'house_id': choice
}
response = requests.post('https://discord.com/api/v9/hypesquad/online', headers=headers, json=body)

if response.status_code == 204:
    print("Successfully changed Hypesquad [204]")
else:
    print("Token errado/incorreto")