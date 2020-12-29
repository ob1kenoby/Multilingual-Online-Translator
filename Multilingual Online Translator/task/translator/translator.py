import argparse
import re
import requests
from bs4 import BeautifulSoup


def capitalize(language_name: str) -> str:
    return language_name[0].upper() + language_name[1:]


def translate(source, target, word):
    translation_page = requests.get(f"https://context.reverso.net/translation/{source}-{target}/{word}",
                                    headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(translation_page.content, 'html.parser')
    words_translated = set([_word.text.strip().lower() for _word in soup.find_all('a', {'class': 'link_highlighted'})])
    words = '\n'.join(words_translated)
    example_src = soup.find('div', {'class': 'src ltr'}).text.strip()
    example_trg = soup.find('div', {'class': re.compile('trg[ a-zA-Z]*')}).text.strip()
    output = f"""{capitalize(target)} Translations:
{words}

{capitalize(target)} Example:
{example_src}
{example_trg}

"""
    return output


parser = argparse.ArgumentParser()
parser.add_argument("source")
parser.add_argument("target")
parser.add_argument("word")

args = parser.parse_args()

source = args.source
target = args.target
word = args.word

languages = ['arabic', 'german', 'english', 'spanish', 'french', 'hebrew', 'japanese', 'dutch', 'polish', 'portuguese',
             'romanian', 'russian', 'turkish']

# print("Hello, you're welcome to the translator. Translator supports:")
# for i in range(len(languages)):
#     print(f'{i + 1}. {capitalize(languages[i])}')
# print('Type the number of your language: ')
# source = languages[int(input()) - 1]
# print("Type the number of language you want to translate to or '0' to translate to all languages:")
# choice = int(input())
# print('Type the word you want to translate:')
# word = input().lower()


translated_text = ''
if target == "all":
    for i in range(len(languages)):
        if languages[i] != source:
            translated_text += translate(source, languages[i], word)
else:
    translated_text = translate(source, target, word)
print(translated_text)
f = open(f'{word}.txt', 'w')
f.write(translated_text)
f.close()
