
import requests
import pytest

def test_status_code():
    response=requests.get('https://pokemonbattle.me:5000/trainers')
    assert response.status_code == 200 

def test_trainer_name():
    response=requests.get('https://pokemonbattle.me:5000/trainers', params={'trainer_id':'1382'})
    assert response.json()['trainer_name']=='Юрий'

@pytest.mark.parametrize('key, value', [('trainer_name','Юрий')])

def test_trainer_name_2(key,value):
    response=requests.get('https://pokemonbattle.me:5000/trainers', params={'trainer_id':'1382'})   
    assert response.json()[key] == value

    