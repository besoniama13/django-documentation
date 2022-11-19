from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import generic
from .models import Content, Step, Paragraph


def index(request):
    return HttpResponse("<h1>Learned Index</h1>")

class IndexView(generic.ListView):
    template_name = 'learned/search.html'
    context_object_name = 'contents'

    def get_queryset(self):
        return Content.objects.order_by('-heading')

class ContentDetailView(generic.DetailView):
    model = Content
    template = 'learned/detailed.html'
    context_object_name = 'content'


def search(request):
    search = request.GET['query']
    contents = Content.objects.filter(heading__icontains=search)
    return render(request, 'learned/search.html', {
        'contents' : contents,
        'search' : search
        })

def all(request):
    response = Content.objects.all()

    return JsonResponse( { 'response' : response } )


def get_step(pk):
    return Step.objects.filter(content=pk)

def get_paragraph(pk):
    return Paragraph.objects.filter(step=pk)

#def detail(request, pk):
#    content = Content.objects.get(id=pk)
#    steps = get_step(pk)
#    i = 0
#    for step in steps:
#        paragraphs = get_paragraph(step.id)
#        steps[i].paragraphs = paragraphs
#        i += 1
#    content.steps = steps
#
#    return render(request, 'learned/detailed.html', { 'content' : content })
