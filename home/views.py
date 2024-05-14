from django.shortcuts import render
from django.http import HttpResponse
from .forms import TranslatorForm
from .utils import Translator

def translator_view(request):
    form = TranslatorForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            translator = form.cleaned_data['choose_translator']
            text = form.cleaned_data['input_text']
            converter = Translator(text)
            if translator == 'modern':
                converter.to_current_modern_english()
                converted_text = converter.text
            elif translator == 'early':
                converter.to_early_modern_english()
                converted_text = converter.text
            else:
                return HttpResponse("Invalid translator selection")
            
            print(converted_text)
            return render(request, 'home.html', {"converted_text": converted_text, "form": form})
        else:
            # Handle invalid form data here if needed
            return HttpResponse("Invalid form data")
    
    else:
        return render(request, 'home.html', {"form": form})
