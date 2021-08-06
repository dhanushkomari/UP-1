from simpleApp.forms import AchievementForm
from django.contrib import admin
# from .models import Skill, Person

# admin.site.register(Skill)
# admin.site.register(Person)

# # Register your models here.


from .models import Skills,Achievement
class SkillsAdmin(admin.ModelAdmin):
    list_display = ['id']

admin.site.register(Skills, SkillsAdmin)

class AchievementAdmin(admin.ModelAdmin):
    list_display = ['id']
admin.site.register(Achievement, AchievementAdmin)