from random import randint
from googletrans import Translator

verbs = ['love', 'live', 'like' 'say', 'go', 'can', 'look', 'know', 'get',
         'come', 'see', 'think', 'make', 'want']
irregular_verbs = {'say': 'said', 'go': 'went', 'can': 'could', 'know': 'knew',
                   'get': 'got', 'come': 'came', 'see': 'saw',
                   'think': 'thought','make': 'made'}
pronouns = ('I', 'You', 'We', 'They', 'He', 'She')



def verb_conjugation(infinitive, irregular_verb=False):
    """
    Добавляет глагол в множество правильных глаголов или к словарю неправильных
    """
    if irregular_verb:
        irregular_verbs[infinitive] = irregular_verb
        verbs.append(infinitive)
    else:
        verbs.append(infinitive)


def sentence_constructor():
    """
    Генератор предложений на английском из verbs
    """
    verb = verbs[randint(0, len(verbs) - 1)]
    num = randint(1, 9)
    pronoun = pronouns[randint(0, 5)]
    if num == 1:
        result = f'Will {pronoun} {verb}?'
    elif num == 2:
        result = f'{pronoun} will {verb}'
    elif num == 3:
        result = f'{pronoun} willn\'t {verb}'
    elif num == 4:
        if pronoun in ['He', 'She']:
            result = f'Does {pronoun} {verb}?'
        else:
            result = f'Do {pronoun} {verb}?'
    elif num == 5:
        if pronoun in ['He', 'She']:
            result = f'{pronoun} {verb}s'
        else:
            result = f'{pronoun} {verb}'
    elif num == 6:
        if pronoun in ['He', 'She']:
            result = f'{pronoun} doesn\'t {verb}'
        else:
            result = f'{pronoun} don\'t {verb}'
    elif num == 7:
        result = f'Did {pronoun} {verb}?'
    elif num == 8:
        if verb in irregular_verbs:
            verb = irregular_verbs.get(verb)
        else:
            verb += 'ed'
        result = f'{pronoun} {verb}'
    elif num == 9:
        result = f'{pronoun} didn\'t {verb}'
    return result.capitalize()


# Перевод на русский
def get_translate(word):
    translator = Translator()
    result_text = translator.translate(word, src='en', dest='ru')
    return result_text.text

