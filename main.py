from random import randint
from googletrans import Translator

verbs = ['love', 'live', 'like']
irregular_verbs = {}
pronouns = ('I', 'You', 'We', 'They', 'He', 'She')
structural_proposal = ['Will', 'Do' 'Does', 'Did', 'not', '?', 's', 'ed']


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
            result = f'{pronoun} {verb}'
        else:
            result = f'{pronoun} {verb}s'
    elif num == 6:
        if pronoun in ['He', 'She']:
            result = f'{pronoun} don\'t {verb}'
        else:
            result = f'{pronoun} doesn\'t {verb}'
    elif num == 7:
        result = f'Did {pronoun} {verb}?'
    elif num == 8:
        if verb in irregular_verbs:
            verb = irregular_verbs.get(verb)
        else:
            verb += 'ed'
        result = f'{pronoun} {verb}'
    elif num == 9:
        result = f'{pronoun} did\'t {verb}'
    return result


# Перевод на русский

translator = Translator()
result_text = translator.translate(sentence_constructor(), src='en', dest='ru')
print(result_text.text)
