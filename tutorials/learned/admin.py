from django.contrib import admin
from .models import Content, Step, Paragraph

class ParagraphAdmin(admin.ModelAdmin):
    fields = ['step', 'head', 'order', 'text', 'text_type' ]
    list_filter = ('step',)
    list_display = ('step', 'order', 'text', 'text_type')
    ordering = ('step','order',)

class StepAdmin(admin.ModelAdmin):
    fields = ['content', 'step_number', 'step_name', ]
    list_filter = ('content',)
    list_display = ('content', 'step_number', 'step_name',)
    ordering = ('content','step_number',)
admin.site.register(Content)
admin.site.register(Step, StepAdmin)
admin.site.register(Paragraph, ParagraphAdmin)
