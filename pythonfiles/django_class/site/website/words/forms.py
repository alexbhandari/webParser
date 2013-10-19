from django.utils.translation import gettext_lazy as _
from django import forms
from words.parse import parse

class ParseAddressForm(forms.Form):

   address = forms.CharField(label=_("Address"),
               max_length=255,
               widget=forms.TextInput,
   )
   parse = parse()

   def parse(self,address): 
      list_of_links = []
      list_of_links.append(address)
      (self.parse.parse(list_of_links,save=True))
