import eel
from main import sentence_constructor, get_translate




@eel.expose
def translate_before():
    word = sentence_constructor()
    return word


@eel.expose
def translate_after(str):
    result = get_translate(str)
    return result


eel.init('web')
eel.start('main.html', size=(700, 700))