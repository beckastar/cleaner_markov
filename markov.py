<<<<<<< HEAD
import sys
from random import randint, choice

=======
#!/usr/bin/env python

import sys
from random import randint, choice 
import re
>>>>>>> 6d9d662a981b5f0691fb704a916cbe6ac86ace29

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
<<<<<<< HEAD
    words = corpus.split()
    #bad practice to change fundamental variable type
    #turn text into words
    #create a tuple of keys
    #start at beginning of text
    # iterate through to end
    #key values are i, i+1
    d = {}
    for i in range(0, len(words)-2):
        key = (words[i], words[i+1])
        value = words[i+2]
        #lists cannot be dictionary keys 
        #this works if there's already a list in the dictionary
        #if there isn't a key in the dictionary, use .get()
        l = d.get(key)
        #checking to see if key is there
        #.get will get *value* for that key. 
        if l == None:
            #get returns none if it isn't there
            new_l = []
            new_l.append(value)
            d[key]= new_l
        else:
            l.append(value)
            #append it to a list if it is there. 
    return d

def add_word (d, l):
    print l
    pair = l[-2:]
    #pair is a list.  Lists can't be keys, so we have to make it a tuple. 
    #pair = tuple(pair)
    print pair 
    pair = (pair[0], pair[1])
    if pair not in d:
        return 
        #do not need else because return statement
    next_word = choice(d[pair])
    print next_word
    l.append(next_word)
    return l

def are_we_done(l):
    punctuation = '?."!'
    if l[-1][-1] in punctuation:
        return True
    else:
        return False

def main():
    args = sys.argv
    script, filename = args 
    #this allows you to reference text file on the command line. 
    corpus = open(filename).read()
    #this ties the variable corpus to the open file
    chain_dict = make_chains(corpus)
    #random_text = make_text(chain_dict)
    text= list(choice(chain_dict.keys()))
    while are_we_done(text) == False:
        add_word(chain_dict, text)
    print " ".join(text)
=======
    chains = {}
    corpus = corpus.split()
    
    for i in range(0, len(corpus) - 2):
        #later in the loop we refer to i+1 and i + 2 -- this prevents a range error
        word_pair = (corpus[i], corpus[i + 1])
        #word_pair = start at the beginning, make k out of word and the word after that
        chains[word_pair] = chains.get(word_pair, [])
        #put an empty list in the value for each pair
        chains[word_pair].append(corpus[i + 2])
        #append the list that is in the value with the word two indeces over from i. 
    return chains

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    random_pair = choice(chains.keys())
    #choose random key of two words
    while random_pair[0][0].isupper() == False:
        #check to see if word is capitalized
        random_pair = choice(chains.keys())            # Choose random key from dictionary
        #choose random key among keys which are not capitalized
    
    random_text = [random_pair[0], random_pair[1]]
        #not in while statement! the random text is a  list of the first and 
        # second word in the keys tuple


    while random_text[-1][-1] != ".":   # Keep the chain going till there's a period.
        # Randomly select next word from the dictionary of key/value pairs
        # Where value = list of all possible next words
        new_word_index = randint(0, len(chains[random_pair]) - 1)
        # Get the value (the actual word) given the randomly selected index position
        new_word = chains[random_pair][new_word_index]
        #new word index is the random integer representing a randomly chosen index position 
        #getting a random integer from list of new possible words (index of new possible word)
        # Append the new word to the string random_text
        random_text.append(new_word)
        # Assign the last two words in random_text to be the new tuple/key          
        
        random_pair = (random_text[-2], random_text[-1])

    return random_text
 
def main():
    args = sys.argv
    script, filename = args
    corpus = open(filename).read()

    chain_dict = make_chains(corpus)
    random_text = make_text(chain_dict)
    print " ".join(random_text)     # So that the text prints out nicely.
>>>>>>> 6d9d662a981b5f0691fb704a916cbe6ac86ace29

if __name__ == "__main__":
    main()