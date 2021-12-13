from django.shortcuts import redirect

def redirect_home(request):
    return redirect('home/')