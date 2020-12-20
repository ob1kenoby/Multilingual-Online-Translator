import requests
from bs4 import BeautifulSoup


def capitalize(language_name: str) -> str:
    return language_name[0].upper() + language_name[1:]


languages = ['arabic', 'german', 'english', 'spanish', 'french', 'hebrew', 'japanese', 'dutch', 'polish', 'portuguese',
             'romanian', 'russian', 'turkish']

print("Hello, you're welcome to the translator. Translator supports:")
for i in range(len(languages)):
    print(f'{i + 1}. {capitalize(languages[i])}')
print('Type the number of your language: ')
source = languages[int(input()) - 1]
print('Type the number of language you want to translate to:')
target = languages[int(input()) - 1]
print('Type the word you want to translate:')
word = input().lower()

translation_page = requests.get(f"https://context.reverso.net/translation/{source}-{target}/{word}",
                                headers={'User-Agent': 'Mozilla/5.0'})
print(f"{translation_page.status_code} OK\n")

soup = BeautifulSoup(translation_page.content, 'html.parser')

words_translated = set(word.text.lower() for word in soup.find_all('a', {'class': 'link_highlighted'}))
examples_src = [phrase.text.strip() for phrase in soup.find_all('div', {'class': 'src ltr'})]
examples_trg = [phrase.text.strip() for phrase in soup.find_all('div', {'class': 'trg ltr'})]

print("Context examples:\n")
print(f"{capitalize(target)} Translations:")
for word in words_translated:
    print(word)
print()

print(f"{capitalize(target)} Examples:")
for i in range(len(examples_src)):
    if i <= len(examples_trg) and i <= 5:
        print(examples_src[i])
        print(examples_trg[i])
