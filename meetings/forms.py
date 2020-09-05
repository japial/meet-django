from datetime import date

from django.core.exceptions import ValidationError
from django.forms import ModelForm, DateInput, TimeInput, TextInput

from meetings.models import Meeting


class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
            'time': TimeInput(attrs={'type': 'time'}),
            'duration': TextInput(attrs={'type': 'number', 'min': '1', 'max': '4'})
        }

    def clean_date(self):
        d = self.cleaned_data.get('date')
        if d < date.today():
            raise ValidationError('Meeting can not be in past')
        return d

