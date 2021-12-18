from django.shortcuts import render
from django.views.generic import DetailView
from django.http import JsonResponse
from . import services
from .models import Entries
from django.db.models.functions import Lower



def index(request):
    return render(request, 'main/index.html', services.get_initial_entries())


def dynamic_entries_load(request):
    start_index = int(request.GET.get('lastEntryIndex'))
    more_entries = services.get_entries_for_dynamic_load(start_index, start_index + 20)
    return JsonResponse(more_entries)


def entry_list_load(request):
    module = int(request.GET.get('module', 0))
    letter = request.GET.get('letter', '').lower()
    data = services.get_entries_by_attributes(module=module, word__startswith=letter)
    return render(request, 'main/entry_list.html', data)


def exercises(request):
    return render(request, 'main/exercise_page.html', {'modules_num': range(1, 13)})


def entry(request):
    word = request.GET.get("word")
    module = request.GET.get("module")
    myKwargs = {'word':word, 'module':module}

    data = services.get_entry_data(**myKwargs)
    if data["found"]:
        return render(request, 'main/entry_page.html', data)
    else:
        return render(request, 'main/not_found.html', {"word": word, "module": module})


def live_search(request):

    pattern = request.GET.get('pattern')
    if request.is_ajax():

        results = []
        if len(pattern) > 0:
            results = services.live_search(pattern)
        return JsonResponse({'data': results})
    else:
        return entry(request)


################
### ТРЕНАЖЕР ###
################



def render_exercise_page(request):
    type = request.GET.get('type', 'card')
    lang = request.GET.get('lang', 'eng')
    print(type, lang)
    specification = request.GET.get('spec', '')
    exercises = {
        'card': 'main/card.html',
        'translate': 'main/translate.html',
        'choose': 'main/choose.html',
    }
    return render(request, exercises[type], {"lang": lang, "spec": specification})






def get_translation_task(request):
    lang = request.GET.get('lang', 'eng')
    print(request.GET)
    data = services.get_translation_task(lang)
    return JsonResponse(data)


def get_choose_task(request):
    lang = request.GET.get('lang', 'eng')
    spec = request.GET.get('spec', '')
    data = services.get_choose_task(lang, spec)
    return JsonResponse(data)


def get_card(request):
    return JsonResponse(services.get_card())














