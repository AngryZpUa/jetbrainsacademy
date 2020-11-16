import requests
import sys
from bs4 import BeautifulSoup

languages = ('Arabic', 'German', 'English', 'Spanish', 'French', 'Hebrew', 'Japanese', 'Dutch',
             'Polish', 'Portuguese', 'Romanian', 'Russian', 'Turkish')


def request_response(source_lang, dest_lang, word, counter=5):
    try:
        global languages
        translate_lst = []
        example_lst = []
        my_url = 'https://context.reverso.net/translation/'
        my_url += '{}-{}/{}'.format(source_lang.lower(), dest_lang.lower(), word)
        headers = {'User-Agent': 'Mozilla/5.0'}
        my_request = requests.get(my_url, headers=headers)
        if my_request.status_code == 200:
            soup = BeautifulSoup(my_request.content, features="html.parser")
            translate_words_section = soup.find('div', {'id': 'translations-content'})
            my_counter = 0
            for item in translate_words_section.find_all('a'):
                if my_counter == counter:
                    break
                translate_lst.append(item.text.strip())
                my_counter += 1
            translate_examples_section = soup.find_all('section', {'id': 'examples-content'})[0]
            phrases = translate_examples_section.find_all('div', {'class': 'example'})
            my_counter = 0
            for div_tag_content in phrases:
                if my_counter == counter:
                    break
                src_ltr = div_tag_content.find('div', {'class': 'src ltr'})
                example_lst.append(src_ltr.find('span', {'class': 'text'}).text.strip() + ':')
                trg_ltr = div_tag_content.find_all('div')[1]
                example_lst.append(trg_ltr.find('span', {'class': 'text'}).text.strip())
                my_counter += 1
            result_dict = {1: translate_lst, 2: example_lst}
            return result_dict
        elif my_request.status_code == 404:
            print('Sorry, unable to find {}'.format(word))
            sys.exit()
    except Exception:
        print('Something wrong with your internet connection')
        sys.exit()


if len(sys.argv) == 1:
    source_l = 'English'
    dest_n = -1
    word_to_translate = 'hello'
else:
    source_l = sys.argv[1].capitalize()
    if source_l not in languages:
        print("Sorry, the program doesn't support {}".format(sys.argv[1]))
        sys.exit()
    if sys.argv[2] == 'all':
        dest_n = -1
    else:
        if sys.argv[2].capitalize() not in languages:
            print("Sorry, the program doesn't support {}".format(sys.argv[2]))
            sys.exit()
        dest_n = languages.index(sys.argv[2].capitalize())
    word_to_translate = sys.argv[3]
if dest_n == -1:
    for i in range(len(languages)):
        dest_l = languages[i]
        if dest_l != source_l:
            result = request_response(source_l, dest_l, word_to_translate, 1)
            trans_lst = result[1]
            example_lst = result[2]
            file_name = word_to_translate + '.txt'
            with open(file_name, 'a') as my_file:
                print(dest_l + ' Translations:')
                my_file.write(dest_l + ' Translations:\n')
                print(trans_lst[0])
                my_file.write(trans_lst[0] + '\n')
                print()
                my_file.write('\n')
                print(dest_l + ' Example:')
                my_file.write(dest_l + ' Example:\n')
                print(example_lst[0])
                my_file.write(example_lst[0] + '\n')
                print(example_lst[1])
                my_file.write(example_lst[1] + '\n')
                print()
                my_file.write('\n')
                print()
                my_file.write('\n')
else:
    dest_l = languages[dest_n]
    result = request_response(source_l, dest_l, word_to_translate)
    trans_lst = result[1]
    examp_lst = result[2]
    print()
    print(dest_l + ' Translations:')
    for trans in trans_lst:
        print(trans)
    print()
    print(dest_l + ' Examples:')
    for i in range(0, len(examp_lst), 2):
        print(examp_lst[i])
        print(examp_lst[i + 1])
        print()
