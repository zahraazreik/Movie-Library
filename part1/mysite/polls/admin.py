from django.contrib import admin

from .models import Choice, Question

#admin.site.register(Question)

#the modification
#This particular change above makes the “Publication date” come before the “Question” field:


class ChoiceInline(admin.TabularInline): # this tells Django: "Choice" are edited on the question admin page. 
    model = Choice                       #other way of presenting the choices filed: StackedInline
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [ #the fieldsets are displayed in change question page
            (None,               {'fields': ['question_text']}),
            ('Date information', {'fields': ['pub_date'], 'classes': ['collapse'] } ),
    ]
    inlines = [ChoiceInline] 
    list_display = ('question_text', 'pub_date', 'was_published_recently')# displays the attributes in the questions page
    list_filter = ['pub_date'] #based on the utterances of the parameter
    search_fields=['question_text'] # search input field
#you will want to customize how the admin form looks and works
#you will do this by telling Django the options you want when you register the project
admin.site.register(Question, QuestionAdmin)
