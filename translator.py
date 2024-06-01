#gets all unique characters in a file
#make the set
import APIKEY
import AnkiGenerator
import re
import jieba
import cedict
import deepl
from cedict_utils.cedict import CedictParser

# Regex optimization: Pre-compile the pattern for better performance.
zhhz_pattern = re.compile(r'[\u4e00-\u9fff]+')  # Match one or more CJK characters

translator = deepl.Translator(APIKEY.API_KEY)

parser = CedictParser()
parser.read_file('cedict_ts.u8')
#entries = parser.parse()
cedict_dict = {}
for entry in parser.parse():
    cedict_dict[entry.simplified] = ', '.join(entry.meanings)

def contains_only_zhhz(word):
    return bool(zhhz_pattern.fullmatch(word))  

def translate_block(block, word_count):
    results = {}
    for word in block:
        if(not contains_only_zhhz(word)):
            continue
        entry = cedict_dict.get(word)
        if entry:  # Check if the word was found
            print(f"{word}: {entry}")
        else:
            result = translator.translate_text(word, source_lang="ZH", target_lang="EN-US")
            entry = result.text
            print(f"{word}: {entry}")
        results[word] = entry
    AnkiGenerator.create_flashcards(results) 
    