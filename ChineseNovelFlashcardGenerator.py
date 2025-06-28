import opencc
import re
from translator import translate_block
import AnkiGenerator  
import os
import jieba
import threading

# Block Size for threading
block_size = 100

# opencc converter initializer
converter = opencc.OpenCC('t2s.json')

def main():
    char_dict = {}
    word_count = 0
    with open('text.txt', 'r', encoding='utf-8', errors='replace') as file:
        #test = '你是我的小苹果'
        unique_text = set()
        words = list(jieba.cut(converter.convert(file.read())))
        #words = list(jieba.cut(test))
        unique_text = set()
        for word in words:
            unique_text.add(word)
        unique_text = list(unique_text)
        #unique_text = unique_text[0: 100]
        thread_count = 1
        block_size = int((len(unique_text) / thread_count) + 0.5)
        threads = []
        print(str(thread_count) + " threads created")
    for i in range(0, thread_count):
        block = unique_text[i * block_size: i * block_size + block_size]
        thread = threading.Thread(target = translate_block, args = (block, word_count))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
             
                
    AnkiGenerator.package_deck()

if __name__ == "__main__":
    main()
