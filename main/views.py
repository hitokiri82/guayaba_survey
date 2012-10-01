from json import loads
import urllib

#from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from main.models import Visit, Question, Question_Text, Option, Option_Text


class DispQuestion:
    def __init__(self, idq, text, q_type, options):
        self.id = idq
        self.text = text
        self.type = q_type
        self.options = options


class DispOption:
    def __init__(self, ido, text):
        self.id = ido
        self.text = text


def index(request):
    locale = "es_ES"
    questions = Question.objects.all().order_by('order')
    display_qs = []
    for q in questions:
        question_text = q.question_text_set.get(locale=locale).content
        options = []
        if q.q_type == 'M':
            for o in q.option_set.all().order_by('order'):
                options.append(DispOption(o.id, o.texts.get(locale=locale).content))
                display_qs.append(DispQuestion(q.id, question_text, q.q_type, options))
    return render_to_response('poll.html', {"questions": display_qs, "locale": locale}, context_instance=RequestContext(request))


def process(request):
    num_lawyers = request.POST['num_lawyers']
    answer1 = request.POST['answer1']
    answer2 = request.POST['answer2']
    email = request.POST['email']
    ip_address = request.META['REMOTE_ADDR']
    response = loads(urllib.urlopen('http://api.hostip.info/get_json.php?ip=' + ip_address).read())
    country = response['country_name']
    city = response['city']

    v = Visit(ip_address=ip_address, num_lawyers=num_lawyers, answer1=answer1, answer2=answer2, email=email, country=country, city=city)
    v.save()

    return render_to_response('result.html', {"ip_address": ip_address, "country": country, "answer1": answer1})
