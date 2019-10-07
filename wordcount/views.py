from django.http import HttpResponse

from django.shortcuts import render
def homepage(request):
    return render (request, 'home.html')

def count(request):
    data = request.GET ['fulltextarea']
    data_list = data.split()
    master = len(data_list)
    
    word_dictionary = {}
    for word in data_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    return render(request, 'count.html',{'fulltext' : data , "words" : master, 'dictionary' : word_dictionary.items()})


def newpage(request):
    return render(request, 'page.html')