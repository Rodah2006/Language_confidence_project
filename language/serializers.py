from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category,Word, VocabularyWord, LearnedWord, FavoriteWord, Quiz

# Serializer for the User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

# Serializer for Categories
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
# Serializer for Word
class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'

# Serializer for Vocabulary Words
class VocabularyWordSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # nested category info

    class Meta:
        model = VocabularyWord
        fields = ['id', 'word', 'meaning', 'example', 'category']

# Serializer for Learned Words
class LearnedWordSerializer(serializers.ModelSerializer):
    word = VocabularyWordSerializer(read_only=True)

    class Meta:
        model = LearnedWord
        fields = ['id', 'user', 'word']

# Serializer for Favorite Words
class FavoriteWordSerializer(serializers.ModelSerializer):
    word = VocabularyWordSerializer(read_only=True)

    class Meta:
        model = FavoriteWord
        fields = ['id', 'user', 'word']

# Serializer for Quizzes
class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'user', 'score', 'date_taken']
