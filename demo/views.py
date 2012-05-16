from django.template import loader, Context, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse

from models import Person
from django.forms import ModelForm

class PersonForm(ModelForm):
    class Meta:
        model = Person


def show_candidate(request):
    c = RequestContext(request)
    president, _ = Person.objects.get_or_create(name="George Washington")
    c['candidate'] = president
    return render_to_response('person.html', c)


def edit_form(request):
    # article = Article.objects.get(pk=1)
    # form = ArticleForm(instance=article)
    president, _ = Person.objects.get_or_create(name="George Washington")
    c = RequestContext(request)

    if request.method == 'POST':
        form = PersonForm(request.POST, instance=president)
        form.save()
        return HttpResponseRedirect(reverse(show_candidate))
    else:
        c['candidate'] = president
        c['form'] = PersonForm(instance=president)
        return render_to_response('rich_edit.html', c)

