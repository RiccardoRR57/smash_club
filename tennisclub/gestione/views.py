from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .models import Player
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from .forms import *

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Tennis Club Management System!")

def player_list(request):
    
    templ = 'player_list.html'
    ctx = { "title":"Lista dei Giocatori",
        "playerlist": Player.objects.all()}

    return render(request, templ, ctx)

def add_player(request):
    message = ""

    if "first_name" in request.GET:
        first_name = request.GET["first_name"]
        last_name = request.GET["last_name"]
        birth_date = request.GET["birth_date"]
        
        new_player = Player()
        new_player.first_name = first_name
        new_player.last_name = last_name
        new_player.birth_date = birth_date
        try:
            new_player.save()
            message = f"Player {first_name} {last_name} added successfully!"
        except Exception as e:
            message = f"Error adding player: {e}"
        
    return render(request, 'add_player.html', context={'title':"Aggiungi giocatore", 'message': message})

class PlayerListView(ListView):
    model = Player
    template_name = "player_list_class.html"

    def test_function(self):
        return Player.objects.all().count()
    
class PlayerCreateView(CreateView):
    model = Player
    template_name = "add_player_class.html"
    fields = "__all__"
    success_url = reverse_lazy('gestione:player_list_class')

class PlayerDetailView(DetailView):
    model = Player
    template_name = "player_detail.html"

class PlayerUpdateView(UpdateView):
    model = Player
    template_name = "update_player.html"
    fields = "__all__"
    def get_success_url(self):
        pk = self.get_context_data()["object"].pk
        return reverse("gestione:player_detail", kwargs={'pk': pk})
    
class PlayerDeleteView(DeleteView):
    model = Player
    template_name = "delete_player.html"
    success_url = reverse_lazy('gestione:player_list_class')

def search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            sstring = form.cleaned_data.get("search_string")
            where = form.cleaned_data.get("search_where")
            return redirect("gestione:searchresults", sstring, where)
    else:
        form = SearchForm()
    return render(request,template_name="searchpage.html",context={"form":form})

class SearchResultsList(ListView):
    model = Player
    template_name = "player_list_class.html"

    def get_queryset(self):
        sstring = self.kwargs['sstring']
        where = self.kwargs['where']
        if where == "Nome":
            return Player.objects.filter(first_name__icontains=sstring)
        elif where == "Cognome":
            return Player.objects.filter(last_name__icontains=sstring)
        else:
            return Player.objects.none()