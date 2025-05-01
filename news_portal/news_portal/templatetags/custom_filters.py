from django import template

register = template.Library(name='censor')

CENSORED_WORDS = [
    'блин',
    'редиска',
    'воландеморт',
    'дурак',
    'пес'
]

@register.filter()
def currency(value):
    # words_value = value.split()
    # for word in words_value:
    #     if word[1:].islower():
    # for censored_word in CENSORED_WORDS:


