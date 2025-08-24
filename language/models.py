from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Word(models.Model):
    text = models.CharField(max_length=100, unique=True)   # the word itself
    meaning = models.TextField()                           # definition or explanation
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="words", null=True, blank=True
    )  # optional: link to a category
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class VocabularyWord(models.Model):
    word = models.CharField(max_length=100)
    meaning = models.TextField()
    example = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.word


class LearnedWord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.ForeignKey(VocabularyWord, on_delete=models.CASCADE)


class FavoriteWord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.ForeignKey(VocabularyWord, on_delete=models.CASCADE)


class Quiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)
