#from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from main.models import Visit
import json
import urllib


def index(request):
    #return HttpResponse("Hello, world. You're at the poll index.")
    return render_to_response('poll.html', {}, context_instance=RequestContext(request))


def process(request):
    num_lawyers = request.POST['num_lawyers']
    answer1 = request.POST['answer1']
    answer2 = request.POST['answer2']
    email = request.POST['email']
    ip_address = request.META['REMOTE_ADDR']
    response = json.loads(urllib.urlopen('http://api.hostip.info/get_json.php?ip=' + ip_address).read())
    country = response['country_name']
    city = response['city']

    v = Visit(ip_address=ip_address, num_lawyers=num_lawyers, answer1=answer1, answer2=answer2, email=email, country=country, city=city)
    v.save()

    return render_to_response('result.html', {"ip_address": ip_address, "country": country, "answer1": answer1})
