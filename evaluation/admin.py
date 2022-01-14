from django.contrib import admin
from . models import *

class Labels(admin.TabularInline):
    model = Label
    extra = 0
    fk_name = "question"
    
class Options(admin.TabularInline):
    model = Option
    extra = 0
    fk_name = "question"

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('name',)    
    inlines = [Labels, Options]    
admin.site.register(Question, QuestionAdmin)

admin.site.register(LogicalString)
admin.site.register(DifinedLabel)
admin.site.register(Biofuel)
admin.site.register(Evaluator)

