import requests
import json

response=requests.post('https://pokemonbattle.me:5000//trainers/reg',json= {
"trainer_token": "dbe261bb0c27356809340cdcf7a131eb",
"email": "yura_levoshuk@mail.ru",
"password": "nmKjU78jKO01m"})

token = 'dbe261bb0c27356809340cdcf7a131eb'
response=requests.post('https://pokemonbattle.me:5000/pokemons',headers={'trainer_token': token},json= {
"name":"Чаризард",
"photo":"https://www.pngfind.com/pngs/m/33-336813_charizard-png-download-cartoon-transparent-png.png"
})
print(response.text)


response_put=requests.put('https://pokemonbattle.me:5000/pokemons',headers={'trainer_token': token},json={
    "pokemon_id": 1726,
    "name": "Юризард",
    "photo": "https://www.pngfind.com/pngs/m/33-336813_charizard-png-download-cartoon-transparent-png.png"
})
print(response_put.text)



response_post=requests.post('https://pokemonbattle.me:5000/trainers/addPokebol',headers={'trainer_token': token},json={
    "pokemon_id": 1740,
})
print(response_post.text)

response_1=requests.post('https://pokemonbattle.me/trainers/ ')
print(response.status_code)
if response.status_code == 200:
            print('Ok')
else:
    print('not Ok')