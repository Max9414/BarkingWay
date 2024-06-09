from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, 'home.html')


def custom_404(request, exception):
    return render(
        request, '404.html', status=404)


def custom_500(request):
    return render(request, '500.html', status=500)