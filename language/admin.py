from django.contrib import admin
from .models import Category, VocabularyWord, LearnedWord, FavoriteWord, Quiz

admin.site.register(Category)
admin.site.register(VocabularyWord)
admin.site.register(LearnedWord)
admin.site.register(FavoriteWord)
admin.site.register(Quiz)
