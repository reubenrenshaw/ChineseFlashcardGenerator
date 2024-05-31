"""
original
import re
import translator
import AnkiGenerator
import os
import jieba

def contains_only_zhhz(word):
    for char in word:
        if(not re.match(r'[\u5e00-\u9fff]', char)):
            return False
    return True

def main():

    set_of_unique_chars = set()
    char_dict = dict()
    with open('text.txt', 'r', encoding = 'utf-8', errors = 'replace') as file:
        text = file.read()
        words = jieba.cut(text)
        for word in words:
            if(contains_only_zhhz(word)):
                print("Translating: " + word)
                char_dict[word] = translator.translate_word(word)
        AnkiGenerator.package_deck()    
    

if __name__ == "__main__":
    main()
"""
import re
import translator  # Assuming you have a custom 'translator' module
import AnkiGenerator  # Assuming you have a custom 'AnkiGenerator' module
import os
import jieba

# Regex optimization: Pre-compile the pattern for better performance.
zhhz_pattern = re.compile(r'[\u4e00-\u9fff]+')  # Match one or more CJK characters

def contains_only_zhhz(word):
    return bool(zhhz_pattern.fullmatch(word))  # More concise and efficient check

def main():
    char_dict = {}
    i = 0
    with open('text.txt', 'r', encoding='utf-8', errors='replace') as file:
        words = jieba.cut(file.read())  # No need for intermediate 'text' variable
        for word in words:
            if contains_only_zhhz(word):
                i += 1
                if(i > 100):
                    break
                if(not word in char_dict):
                    print("Translating:", word)
                    char_dict[word] = translator.translate_word(word)

    AnkiGenerator.create_flashcards(char_dict)

if __name__ == "__main__":
    main()