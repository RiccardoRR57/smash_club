from django import forms

class SearchForm(forms.Form):

    CHOICE_LIST = [("Nome","Cerca tra i nomi"), ("Cognome","Cerca tra i cognomi")]

    search_string = forms.CharField(label="Search String",max_length=100,min_length=3, required=True)
    
    search_where = forms.ChoiceField(label="Search Where?", required=True, choices=CHOICE_LIST)