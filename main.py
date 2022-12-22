import requests

locations = {
  1 : 'Череповец',
  2 : 'Аэропорт Шереметьево',
  3 : 'Лондон',
}

'''
# list of options provided for reference only (see 'options' variable below)

options = {
    n:  'narrow version (only day and night)',
    T:  'force plain text, disable colors',
    q:  'quiet version (no "Weather report" text)',
    M:  'metric (SI), but show wind speed in m/s',
  }

# list of languages provided for reference only (see 'language' variable below)

languages = {
    English :  'en',
    French  :  'fr',
    German  :  'de',
    Russian :  'ru',
  }
'''

for location in locations:
  location_selected = locations[location]
  options = 'nTqM'
  language = 'ru'
  url_template = 'http://wttr.in/{}'
  url = url_template.format(location_selected)
  response = requests.get(url, params = (options + '&lang=' + language))
  response.raise_for_status()
  print(response.text)
