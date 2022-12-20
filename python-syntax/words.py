# For a list of words, print out each word on a separate line, but in 
# all uppercase. How can you change a word to uppercase? Ask Python 
# for help on what you can do with strings!

# Turn that into a function, print_upper_words. Test it out. 
# (Don’t forget to add a docstring to your function!)

# Change that function so that it only prints words that start with 
# the letter ‘e’ (either upper or lowercase).

# Make your function more general: you should be able to pass in a 
# set of letters, and it only prints words that start with one of 
# those letters.

def print_upper_words(list):
    """Takes in a list of words and covert each character in word to 
    uppercase. """
    
    for word in list:
        print(word.upper())
       
print_upper_words(['Egg','dog','cat','mouse','bird', 'elephant','Earwig'])


def print_upper_words2(list):
    """on prints words that start with lower or uppercase 'e' """
    for word in list:
       if word.startswith('e') or word.startswith('E'):
        print (word.upper())

print_upper_words(['Egg','dog','cat','mouse','bird', 'elephant','Earwig'],'m')


def print_upper_words3(list,prefix):
    """print each word on seperate line, uppercased, if starts with given prefix """
    
    for word in list:
        if word.startswith(prefix):
            print(word.upper())
            break
      

print_upper_words3(['Egg','dog','cat','mouse','Bird', 'elephant','Earwig'], prefix=['B','E'])