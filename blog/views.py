from django.shortcuts import render

posts = [
    {
        'author': 'Rafael Ferreira',
        'title' : '1º post',
        'content': 'Hi everbody, my name is Rafael, and i am learning how to use DJANGO!',
        'date':'July 2, 2026',
    }, # <--- A VÍRGULA VAI AQUI!
    {
        'author': 'Pedro Gustavo',
        'title' : '2º post',
        'content': 'I am pretty hyped w/ the 2026 world cup',
        'date': 'July 10, 2026',
    }
]


def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request,'blog/about.html')
