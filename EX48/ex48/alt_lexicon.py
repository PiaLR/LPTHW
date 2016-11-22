lexicon = [('direction', 'north'), ('direction', 'south'),  ('direction', 'east'),
            ('direction', 'west'), ('direction', 'down'), ('direction', 'up'),
            ('direction', 'left'), ('direction', 'right'), ('direction', 'back')]
stuff = raw_input('> ')
words = stuff.split()

first_word = ()
second_word = ()
third_word = ()

sentence = [first_word, second_word, third_word]

class Lexicon(object):

    #def __init__(self):
        #self.name = name



    #number = []

# should scan lexicon for given input 'north' and find and return 'direction' 'north'
    def scan(self, stuff):
            #stuff = raw_input('> ')
            #words = stuff.split()
            direction = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
            verb = ['go', 'stop', 'kill', 'eat']
            stop = ['the', 'in', 'of', 'from', 'at', 'it']
            noun = ['door', 'bear', 'princess', 'cabinet']
            #print stuff
            if stuff in direction:
                word = [('direction', stuff)]
                print word
            #elif stuff in verb:
                #word = ('verb', stuff)
                #print word
            else:
                print "no"

#test = Input()
#lexicon = Lexicon()
#lexicon.scan("north")
