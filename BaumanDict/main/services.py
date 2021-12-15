from .models import Entries
from random import sample, choice, randint
import re


def get_card_head(**kwargs):
    if len(kwargs) == 1:
        if list(kwargs.keys())[0] == 'module':
            return 'words of module '+str(kwargs['module'])
        elif list(kwargs.keys())[0] == 'word__startswith':
            return 'letter "'+kwargs['word__startswith'].upper()+'"'
    else:
        return 'user set list of entries'


def get_initial_entries():
    entries = Entries.objects.all()[:20]
    data = {
        'imgs1': [('main/img/' + str(c) + '.png', c) for c in range(1, 13, 2)],
        'imgs2': [('main/img/' + str(c) + '.png', c) for c in range(2, 13, 2)],
        'entries': entries,
        'letters': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'lastEntryIndex': len(entries)
    }
    return data


def get_entries_by_attributes(**kwargs):
    kwargs = {key:kwargs[key] for key in kwargs if kwargs[key]}
    entries = Entries.objects.filter(**kwargs)
    return {'data':entries, 'list_header':get_card_head(**kwargs)}


def get_entries_for_dynamic_load(start, finish):
    more_entries = Entries.objects.all().values()[start: finish]

    if not more_entries:
        return {'data': [], 'moreEntries': False, 'count': 0}

    more_entries = [
        {"word": entry["word"], "translation": entry["translation"], "module": entry['module']}
        for entry in more_entries
    ]
    return {'data': more_entries, 'moreEntries': True, 'count': finish}


def get_entry_data(**kwargs):
    kwargs = {k: kwargs[k]  for k in kwargs if kwargs[k]}
    try:
        entry = Entries.objects.filter(**kwargs)[0]
    except IndexError:
        return {"found": False}
    # здесь filter всегда (наверное) строит список из 1 элемента
    data = {"entry": entry,
            "eng": entry.getEng().replace('<<b>', '<b>').replace('<d>>', '</b>'),
            "ru": entry.getRu().replace('<<b>', '<b>').replace('<d>>', '</b>'),
            "found": True
            }
    return data


def live_search(pattern):
    entries = []
    if len(pattern)>0:
        entries = list(Entries.objects.filter(word__istartswith=pattern))
    return [
        {"word": entry.word, "module": entry.module}
        for entry in entries
    ]


################
### ТРЕНАЖЕР ###
################
#
# def get_specific_entries(count, **kwargs):
#     entries = Entries.objects.filter(**kwargs)
#     return sample(count, entries)



def formate(data, sep):
    return list(map(str.strip, data.split(sep)))

def get_translation_task(lang, modules='None'):
    data = choice(Entries.objects.all())

    if lang == 'ru':
        ll= {'task': data.word, 'answer': formate(data.translation, ',')}
    else:
        ll= {'task': data.translation, 'answer': formate(data.word, ',')}
    return ll


def get_choose_task(lang, spec, modules='None'):
    pos = choice(('v', 'phr', 'n', 'adj', 'a', 'prep', 'n, v', 'adv', 'conj'))
    entries = list(Entries.objects.filter(pos=pos))
    answs = sample(entries, 4)
    right_answ = answs[randint(0, 3)]
    data = {}

    if lang == 'eng':
        data['right_answ'] = right_answ.word.strip()
        data['task'] = right_answ.translation.strip()
        data['answs'] = [entry.word.strip() for entry in answs]
    else:
        data['right_answ'] = right_answ.translation.strip()
        data['task'] = right_answ.word.strip()
        data['answs'] = [entry.translation.strip() for entry in answs]
    if spec == 'fill':
        data['task'] = re.sub(r'<<b>.*<d>>', '_'*5,  right_answ.getEng())
    data['lang'] = lang
    return data