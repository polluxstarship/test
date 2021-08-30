from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": 'title', }))
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(
                                      attrs={
                                          "placeholder": 'description',
                                          "class": "new-class-name two",
                                          "id": "my-id-for-textarea",
                                          "rows": 20,
                                          "cols": 100,

                                      }
                                  ))
    price = forms.DecimalField(initial=99.99)
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, * args, **kwargs):
        title = self.cleaned_data.get("title")
        if not 'abc' in title:
            raise forms.ValidationError("it requires abc in title")
        return title



















# class RawProductForm(forms.Form):
#     title = forms.CharField(label="", widget= forms.TextInput(attrs={"placeholder":'title',}))
#     description = forms.CharField(required=False,
#                                   widget=forms.Textarea(
#                                       attrs={
#                                           "placeholder": 'description',
#                                           "class": "new-class-name two",
#                                           "id": "my-id-for-textarea",
#                                           "rows": 20,
#                                           "cols": 100,
#
#                                       }
#                                   ))
#     price = forms.DecimalField(initial=199.99)