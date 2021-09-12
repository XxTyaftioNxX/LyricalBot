import random
import string
from graph import Graph, Vertex
import re
import os

def get_words_from_text(text_path):
    with open(text_path, 'r') as f:
        text = f.read()
        #remove brackets and text in it
        text = re.sub(r'\[(.+)\]', ' ', text)
        #removing white spaces
        text = ' '.join(text.split())
        text = text.lower()
        #removing punctuation
        text = text.translate(str.maketrans('','', string.punctuation))

    words = text.split()
    return words

def make_garph(words):
    g = Graph()

    previous_word = None

    #check if word is in graph and add an edge if not add it to graph (done in get_vertex)
    for word in words:
        word_vertex = g.get_vertex(word)
        
        #add edge if there is previous word    
        if previous_word:
            previous_word.increment_edge(word_vertex)

        previous_word = word_vertex 
    
    #set probability mapping
    g.generate_probability_mappings()

    return g

def compose(g, words, length=50):
    composition = []
    word = g.get_vertex(random.choice(words))
    for i in range(length):
        if (i+1)%5 == 0:
            composition.append(word.value)
            composition.append('\n')
        else:
            composition.append(word.value)
        word = g.get_next_word(word)

    return ' '.join(composition)

def main(artist):
    
    words = []

    #get the words we want to make chain from
    for song in os.listdir(f'songs/{artist}'):
        song_words = get_words_from_text(f'songs/{artist}/{song}')
        words.extend(song_words)
    

    #make graph using the words
    g = make_garph(words)

    return compose(g, words, 100)
    
if __name__ == "__main__":
    print(main('Eminem'))


