lexicon = {
    'north': 'direction',
    'south': 'direction',
    'east': 'direction',
    'west': 'direction',
    'down': 'direction',
    'up': 'direction',
    'left': 'direction',
    'right': 'direction',
    'back': 'direction',
    'go': 'verb',
    'stop': 'verb',
    'kill': 'verb',
    'eat': 'verb',
    'the': 'stop',
    'in': 'stop',
    'of': 'stop',
    'from': 'stop',
    'at': 'stop',
    'it': 'stop',
    'door': 'noun',
    'bear': 'noun',
    'princess': 'noun',
    'cabinet': 'noun',
            }

def scan(sentence):
    words = sentence.split()
    result = []

    for word in words:
        try:
            pair = (lexicon[word], word)
            result.append(pair)
        except KeyError:
            try:
                int(word)
                number = ('number', int(word))
                result.append(number)
            except ValueError:
                error = ('error', word)
                result.append(error)

#    print result # uncommand this to test file on its own

    return result

#scan("north 1234 east") # uncommand this to test file on its own
