from django.shortcuts import render
import chatgpt_integration as chatgpt

def index(request):
    if request.POST:
        response = chatgpt.get_how_to(request.POST['text'])
        return render(request, 'index.html', {'response': response})
    else:
        return render(request, 'index.html')
