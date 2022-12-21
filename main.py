import requests

locations_list = {
  1 : ['Череповец', 'Cherepovets'],
  2 : ['Аэропорт Шереметьево', 'SVO'],
  3 : ['Лондон', 'London']
}

print('Выберите местность из списка:')
for i in range (1, 4):
  print(i, '\t', locations_list.get(i)[0])

location_selected = locations_list.get(int(input()))[1]
url_template = 'http://wttr.in/{}?nTqM&lang=ru'
url = url_template.format(location_selected)
#url = f'https://wttr.in/{location_selected}?nTqm&lang=ru'
response = requests.get(url)
response.raise_for_status()
print(response.text)
