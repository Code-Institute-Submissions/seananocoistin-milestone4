from django import forms
from .models import Listing, Category


class ListingForm(forms.ModelForm):

    class Meta:
   
        model = Listing
        exclude = ['paid','owner']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'