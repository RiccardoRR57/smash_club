from gestione.models import Player

def fill_db():
    players = [
        Player(first_name='John', last_name='Doe', birth_date='1990-01-01'),
        Player(first_name='Jane', last_name='Smith', birth_date='1992-02-02'),
        Player(first_name='Alice', last_name='Johnson', birth_date='1988-03-03'),
        Player(first_name='Bob', last_name='Brown', birth_date='1995-04-04'),
    ]
    
    for player in players:
        player.save()
    
    print("Database filled with initial data.")

def erase_db():
    Player.objects.all().delete()
    print("Database erased.")