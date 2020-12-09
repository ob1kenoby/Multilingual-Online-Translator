import requests
from bs4 import BeautifulSoup

print('Type "en" if you want to translate from French into English, or "fr" if you want to translate from English '
      'into French:')
target_language = input()
print('Type the word you want to translate:')
word = input()
print(f'You chose "{target_language}" as the language to translate "{word}" to.')

if target_language == "fr":
    source = "english"
    target = "french"
else:
    source = "french"
    target = "english"

translation_page = requests.get(f"https://context.reverso.net/translation/{source}-{target}/{word}",
                                headers={'User-Agent': 'Mozilla/5.0'})
print(f"{translation_page.status_code} OK")

soup = BeautifulSoup(translation_page.content, 'html.parser')

words_translated = [word.text for word in soup.find_all('a', {'class': 'link_highlighted'})]
examples = [phrase.text.strip() for phrase in soup.find_all('div', {'class': 'trg ltr'})]

print("Translations")
print(*words_translated, sep=', ')
print(*examples, sep=', ')
