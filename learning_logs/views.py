from django.shortcuts import render
from . models import Topic
from .forms import TopicForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    """ Página principal do Learning_log """
    return render(request, 'learning_logs/index.html')

def topics(request):
    """ Mostra todos os assuntos """
    topics = Topic.objects.order_by('data_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """ Mostra todos os assuntos e suas entradas """
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-data_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """ Adiciona um novo assunto """
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topics'))
        
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)