from django import forms
from .models import Schedule 

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule 
        fields = ['group', 'subject', 'teacher', 'day', 'start_time']
        widgets = {
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['teacher'].label_from_instance = lambda obj: f"{obj.last_name} {obj.first_name[0]}.{obj.middle_name[0] if obj.middle_name else ''}"