import requests

def main_1(name):
    intelligence_dict = {}
    URI = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api'
    URL = URI + '/all.json'
    response = list(filter(lambda hero: hero['name'] == name, requests.get(URL).json()))
    intelligence_dict[name] = [val['powerstats']['intelligence'] for val in response]
    return intelligence_dict

def main_2(name):
    intelligence_dict = {}
    URI = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api'
    URL = URI + '/all.json'
    response = list(filter(lambda hero: hero['name'] == name, requests.get(URL).json()))
    intelligence_dict[name] = [val['powerstats']['intelligence'] for val in response]
    return intelligence_dict

def main_3(name):
    intelligence_dict = {}
    URI = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api'
    URL = URI + '/all.json'
    response = list(filter(lambda hero: hero['name'] == name, requests.get(URL).json()))
    intelligence_dict[name] = [val['powerstats']['intelligence'] for val in response]
    return intelligence_dict

hero_dict = {**main_1('Hulk'), **main_2('Captain America'), **main_3('Thanos')}
print(max(hero_dict))