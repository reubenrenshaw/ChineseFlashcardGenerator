#gets all unique characters in a file
#make the set
import AnkiGenerator
import re
import jieba
import cedict
import deepl
from cedict_utils.cedict import CedictParser


translator = deepl.Translator("913e82d9-45a2-4580-b169-62566762cd72:fx")

parser = CedictParser()
parser.read_file('cedict_ts.u8')
#entries = parser.parse()
cedict_dict = {}
for entry in parser.parse():
    cedict_dict[entry.simplified] = ', '.join(entry.meanings)

def translate_word(word):
    entry = cedict_dict.get(word)
    if entry:  # Check if the word was found
        print(f"{word}: {entry}")
    else:
        result = translator.translate_text(word, source_lang="ZH", target_lang="EN-US")
        entry = result.text
        print(f"{word}: {entry}")
    return entry
    