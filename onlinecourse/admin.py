from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice

# <HINT> Register QuestionInline and ChoiceInline classes here


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text', 'grade', 'lesson')
    list_filter = ['lesson']
    search_fields = ['question_text']


class ChoiceAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ('choice_text', 'is_correct', 'question')
    list_filter = ['question']
    search_fields = ['choice_text']

# <HINT> Register Question and Choice models here


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
