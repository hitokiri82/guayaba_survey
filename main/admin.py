from main.models import *
from django.contrib import admin


class TextAdmin(admin.ModelAdmin):
    list_display = ('id', 'locale', 'content')
    list_filter = ['locale']


class OptionInline(admin.StackedInline):
    model = Option
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]

admin.site.register(Visit)
admin.site.register(Text, TextAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Option)
