from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from googletrans import Translator


def index(request):
    return render(request,'index.html')


@csrf_exempt
def trans(request):
    translator = Translator()
    text = request.POST['text']
    dest = request.POST['lang']
    print(dest)
    transText = translator.translate(text, dest=dest)
    print(transText.text)
    return HttpResponse(transText.text)
