from main.models import *
from django.contrib import admin


class OTextAdmin(admin.ModelAdmin):
    list_display = ('id', 'locale', 'content')
    list_filter = ['locale']


class QTextAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'locale', 'content')
    list_filter = ['locale']


class OptionInline(admin.TabularInline):
    model = Option
    extra = 0


class QTextInline(admin.TabularInline):
    model = Question_Text
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    inlines = [QTextInline, OptionInline]

admin.site.register(Visit)
admin.site.register(Question_Text, QTextAdmin)
admin.site.register(Option_Text, OTextAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
