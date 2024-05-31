import genanki
import random
import requests  # To send requests to AnkiConnect

model_id = random.randrange(1 << 30, 1 << 31)
note_id = random.randrange(1 << 30, 1 << 31)



# Create a deck
my_deck = genanki.Deck(
    random.randrange(1 << 30, 1 << 31),
    'Chinese Flashcards'
)

my_model = genanki.Model(
        model_id,
        'Chinese-English Model',
        fields=[
            {'name': 'Chinese Character'},
            {'name': 'English Translation'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Chinese Character}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{English Translation}}',
            },
        ])

def create_flashcards(words):
    # Create a unique ID for the card (to avoid duplicates)
    # Basic card model
    
    # Create a note with the character and translation
    for word in words.keys():
        my_note = genanki.Note(
            model=my_model,
            fields=[word, words[word]],
            guid=note_id,
        )
        my_deck.add_note(my_note)

    # Package the deck
    genanki.Package(my_deck).write_to_file('ankideck.apkg')