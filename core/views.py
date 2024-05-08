from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView
from core.models import Games
# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        games = Games.objects.all()
        context = super().get_context_data(**kwargs)
        context["Games"] = games
        return context

def play_view(request, name):
    games = Games.objects.all()[:10]
    return render(request, 'play.html',context={"Games":games,})
