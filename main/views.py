from json import loads
from urllib import urlopen

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from main.models import VisitForm, ContactForm


def index(request):
    # print request.META['HTTP_ACCEPT_LANGUAGE']
    if request.method == 'POST':  # If the form has been submitted...
        form = VisitForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            if form.has_changed():
                visit = form.save(commit=False)
                ip_address = request.META['REMOTE_ADDR']
                if 'referer' in request.session:
                    referer = request.session['referer']
                else:
                    referer = None
                response = loads(urlopen('http://api.hostip.info/get_json.php?ip=' + ip_address).read())
                country = response['country_name']
                city = response['city']
                visit.referer = referer
                visit.country = country
                visit.city = city
                visit.save()
            return HttpResponseRedirect('/thanks/')  # Redirect after POST
        else:
            print form.errors
    else:
        form = VisitForm()  # An unbound form
        if 'HTTP_REFERER' in request.META:
            request.session['referer'] = request.META['HTTP_REFERER']
    return render_to_response('poll.html', {'form': form, }, context_instance=RequestContext(request))


def thanks(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = ContactForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            form.save()
            return HttpResponseRedirect('/registered/')  # Redirect after POST
    else:
        form = ContactForm()  # An unbound form
    return render_to_response('thanks.html', {'form': form, }, context_instance=RequestContext(request))


def registered(request):
    return render_to_response('registered.html', {})


def status(request):
    return render_to_response('status.html', {})
