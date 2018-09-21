from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from .models import URLs


class PostForm(forms.ModelForm):

    targetURL = forms.CharField(max_length=256)

    def clean_targetURL(self):
        validate = URLValidator()
        cleaned_data = self.clean()
        url = cleaned_data.get('targetURL')
        try:
            validate(url)
        except ValidationError as e:
            self.add_error('targetURL', "The url is not valid")
        else:
            return url

    class Meta:
        model = URLs
        fields = ('targetURL',)
