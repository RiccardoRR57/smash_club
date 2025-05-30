from django.http import HttpResponse
from django.shortcuts import render
from .models import Player

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