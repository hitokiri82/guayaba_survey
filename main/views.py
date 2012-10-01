from json import loads
import urllib


#from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from main.models import Visit, VisitForm


def index(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = VisitForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/')  # Redirect after POST
    else:
        form = VisitForm()  # An unbound form
    return render_to_response('poll.html', {'form': form, }, context_instance=RequestContext(request))


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
