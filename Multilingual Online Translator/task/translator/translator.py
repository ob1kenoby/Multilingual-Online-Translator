import requests
from bs4 import BeautifulSoup


def capitalize(language_name: str) -> str:
    return language_name[0].upper() + language_name[1:]


def translate(source, target, word):
    translation_page = requests.get(f"https://context.reverso.net/translation/{source}-{target}/{word}",
                                    headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(translation_page.content, 'html.parser')
    words_translated = set(_word.text.lower() for _word in soup.find_all('a', {'class': 'link_highlighted'}))
    example_src = [_phrase.text.strip() for _phrase in soup('div', {'class': 'src ltr'})]
    example_trg = [_phrase.text.strip() for _phrase in soup('div', {'class': 'trg ltr'})]
    output = [f'{capitalize(target)} Translations:\n']
    for _word in words_translated:
        output.append(_word + '\n')
    output.append(f'\n{capitalize(target)} Example:\n')
    output.append(example_src[0] + '\n')
    output.append(example_trg[0] + '\n')
    print(''.join(output))
    return ''.join(output)


languages = ['arabic', 'german', 'english', 'spanish', 'french', 'hebrew', 'japanese', 'dutch', 'polish', 'portuguese',
             'romanian', 'russian', 'turkish']

print("Hello, you're welcome to the translator. Translator supports:")
for i in range(len(languages)):
    print(f'{i + 1}. {capitalize(languages[i])}')
print('Type the number of your language: ')
source = languages[int(input()) - 1]
print("Type the number of language you want to translate to or '0' to translate to all languages:")
choice = int(input())
print('Type the word you want to translate:')
word = input().lower()

f = open(f'{word}.txt', 'w')
if choice == 0:
    for language in languages:
        f.write(translate(source, language, word))
else:
    f.write(translate(source, languages[choice - 1], word))
f.close()
