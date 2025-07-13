from django.views.generic import TemplateView
# from django.shortcuts import render
# vista basada en clase
class HomeView(TemplateView):
    template_name = 'index.html'

# clase basada en funcion
# def index(request):
#     return render(request, 'index.html')