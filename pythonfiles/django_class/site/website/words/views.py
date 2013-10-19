from django.http import HttpResponse
from django.views.generic import View

class Hello_world(View):
   
   def get(self, request, *args, **kwargs):
      return HttpResponse('Hello World!')

from django.views.generic import ListView
from words.models import Word

class ListWordView(ListView):

   model = Word
   template_name = 'word_list.html'

from django.core.urlresolvers import reverse
from django.views.generic import CreateView

class CreateWordView(CreateView):

   model = Word
   template_name = 'edit_word.html'

from django.views.generic.edit import FormView
from words.forms import ParseAddressForm

class ParseAddressView(FormView):

   form_class = ParseAddressForm
   success_url = '/display_parse'
   template_name = 'parse_address.html'

   def form_valid(self, form):
      address = form['address'].value()
      form.parse(address)
      return super(ParseAddressView,self).form_valid(form) #render_to_response return
   
   def form_invalid(self,form):
      pass

class DisplayParseView(ListView):

   model = Word
   template_name = 'display_parse.html'
