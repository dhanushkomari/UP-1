from django import forms
from .models import Achievement

# class PersonForm(forms.ModelForm):
#     class Meta:
#         model = Achievement
#         fields = ['skills',]

from django_select2 import forms as s2forms
class SkillsWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = [
        "name__icontains",
    ]
class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ['skills'] 