from django.contrib import admin
from .models import MultipleChoice,ShortAns, ImageAns 
from django.contrib.auth.models import User

# Register your models here.
# class UserAdmin(admin.ModelAdmin):
#     list_display=('first_name', 'last_name', 'username')

class MultipleChoiceAdmin(admin.ModelAdmin):
    list_display=('question','option1','option2', 'option3', 'option4', 'submitted_answer', 'correct_answer')

class ShortAnsAdmin(admin.ModelAdmin):
    list_display=('question','submitted_answer', 'correct_answer')

class ImageAnsAdmin(admin.ModelAdmin):
    list_display=('question','submitted_answer', 'correct_answer')

# admin.site.register(User, UserAdmin)
admin.site.register(MultipleChoice, MultipleChoiceAdmin)
admin.site.register(ShortAns, ShortAnsAdmin)
admin.site.register(ImageAns, ImageAnsAdmin)
