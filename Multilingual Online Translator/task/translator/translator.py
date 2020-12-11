import requests
from bs4 import BeautifulSoup


def capitalize(language_name):
    return language_name[0].upper() + language_name[1:]


# languages = {'en': 'english', 'fr': 'french'}

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
print(f"{translation_page.status_code} OK\n")

soup = BeautifulSoup(translation_page.content, 'html.parser')

words_translated = set(word.text.lower() for word in soup.find_all('a', {'class': 'link_highlighted'}))
# examples_prc = [phrase.text.strip() for phrase in soup.find_all('div', {'class': 'trg ltr'})]
examples_raw = [block for block in soup.find_all('div', {'class': 'example'})]
examples = []
for block in examples_raw:
    print(block)
    example = [block.find('div', {'class': 'src ltr'}).text.strip(),
               block.find('div', {'class': 'trg ltr'}).text.strip()]

print("Context examples:\n")
print(f"{capitalize(target)} Translations:")
for word in words_translated:
    print(word)
# print(*words_translated, sep=', ')
print()
print(f"{capitalize(target)} Examples:")
for example in examples:
    print(example[0])
    print(example[1])
# print(*examples_prc, sep=', ')
