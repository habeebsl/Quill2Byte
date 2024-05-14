from django import forms


class TranslatorForm(forms.Form):
    choose_translator = forms.ChoiceField(choices=[
        ('', 'Translate to'), 
        ('modern', 'Modern English'), 
        ('early', 'Early English'),],
        widget=forms.Select(attrs={'class':'select-field'})
    )
    input_text = forms.CharField(max_length=5000, 
        widget=forms.Textarea(attrs={'placeholder': 'Enter text', 'id':'input-field'})
    )