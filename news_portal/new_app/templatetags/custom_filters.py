from django import template
import re
from new_app.resources import CENSORED_WORDS

register = template.Library()

@register.filter(name='censor')
def currency(value):
    try:
        words_value = value.split()
        censored_value = ''
        for word in words_value:
            word_clean = ''.join(re.findall('[а-яА-яЁё]', word))
            if word[1:].islower():
                if word_clean.lower() in CENSORED_WORDS:
                    censored_value += word.replace(word_clean[1:], len(word_clean[1:]) * '*') + ' '
                else:
                    censored_value += word + ' '
            else:
                censored_value += word + ' '
        return censored_value[:-1]
    except Exception as e:
        print(e)
        return ''
