from django.http import HttpResponse
from gestione.models import Player

def fill_db(request):
    players = [
        Player(first_name='Luca', last_name='Rossi', birth_date='1990-01-01'),
        Player(first_name='Giulia', last_name='Bianchi', birth_date='1992-02-02'),
        Player(first_name='Alessandro', last_name='Ferrari', birth_date='1988-03-03'),
        Player(first_name='Francesca', last_name='Esposito', birth_date='1995-04-04'),
        Player(first_name='Matteo', last_name='Russo', birth_date='1991-05-05'),
        Player(first_name='Chiara', last_name='Romano', birth_date='1987-06-06'),
        Player(first_name='Davide', last_name='Gallo', birth_date='1993-07-07'),
        Player(first_name='Martina', last_name='Costa', birth_date='1994-08-08'),
        Player(first_name='Simone', last_name='Fontana', birth_date='1989-09-09'),
        Player(first_name='Sara', last_name='Conti', birth_date='1996-10-10'),
        Player(first_name='Andrea', last_name='Greco', birth_date='1990-11-11'),
        Player(first_name='Elena', last_name='Mancini', birth_date='1992-12-12'),
        Player(first_name='Marco', last_name='Lombardi', birth_date='1988-01-13'),
        Player(first_name='Valentina', last_name='Moretti', birth_date='1995-02-14'),
        Player(first_name='Stefano', last_name='Barbieri', birth_date='1991-03-15'),
        Player(first_name='Federica', last_name='Giordano', birth_date='1987-04-16'),
        Player(first_name='Giorgio', last_name='Colombo', birth_date='1993-05-17'),
        Player(first_name='Paola', last_name='Ricci', birth_date='1994-06-18'),
        Player(first_name='Fabio', last_name='Marino', birth_date='1989-07-19'),
        Player(first_name='Roberta', last_name='Bruno', birth_date='1996-08-20'),
        Player(first_name='Emanuele', last_name='Galli', birth_date='1990-09-21'),
        Player(first_name='Ilaria', last_name='Martini', birth_date='1992-10-22'),
        Player(first_name='Tommaso', last_name='Leone', birth_date='1988-11-23'),
        Player(first_name='Silvia', last_name='Longo', birth_date='1995-12-24'),
        Player(first_name='Nicola', last_name='Gentile', birth_date='1991-01-25'),
        Player(first_name='Marta', last_name='Lorenzi', birth_date='1987-02-26'),
        Player(first_name='Pietro', last_name='De Luca', birth_date='1993-03-27'),
        Player(first_name='Angela', last_name='Riva', birth_date='1994-04-28'),
        Player(first_name='Riccardo', last_name='Ferri', birth_date='1989-05-29'),
        Player(first_name='Beatrice', last_name='Serra', birth_date='1996-06-30'),
    ]
    
    for player in players:
        player.save()
    
    return HttpResponse("Database filled with sample players.")


def erase_db(request):
    Player.objects.all().delete()
    return HttpResponse("Database erased.")
