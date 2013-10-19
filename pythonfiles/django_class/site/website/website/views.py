#CURRENTLY NOT IN USE

#from django.views.generic import ListView

#class home(ListView):
#   template_name = 'homepage.html'
from django.http import HttpResponse

def home(request):
   return HttpResponse('Hello World!')
