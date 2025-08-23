from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Category, VocabularyWord, LearnedWord, FavoriteWord, Quiz
from .serializers import (
    UserSerializer,
    CategorySerializer,
    VocabularyWordSerializer,
    LearnedWordSerializer,
    FavoriteWordSerializer,
    QuizSerializer
)


# Register a new user
class RegisterUser(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")
        if not username or not password:
            return Response({"error": "Username and password required"}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username, password=password, email=email)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"message": "User created successfully", "token": token.key}, status=status.HTTP_201_CREATED)

# Login user
class LoginUser(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"message": "Login successful", "token": token.key}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


class VocabularyWordList(generics.ListAPIView):
    queryset = VocabularyWord.objects.all()
    serializer_class = VocabularyWordSerializer
    permission_classes = [permissions.AllowAny]

class VocabularyWordDetail(generics.RetrieveAPIView):
    queryset = VocabularyWord.objects.all()
    serializer_class = VocabularyWordSerializer
    permission_classes = [permissions.AllowAny]


class LearnedWordListCreate(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        learned = LearnedWord.objects.filter(user=request.user)
        serializer = LearnedWordSerializer(learned, many=True)
        return Response(serializer.data)

    def post(self, request):
        word_id = request.data.get("word_id")
        if not word_id:
            return Response({"error": "word_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        word = VocabularyWord.objects.get(id=word_id)
        learned_word, created = LearnedWord.objects.get_or_create(user=request.user, word=word)
        serializer = LearnedWordSerializer(learned_word)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class FavoriteWordListCreate(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        favorites = FavoriteWord.objects.filter(user=request.user)
        serializer = FavoriteWordSerializer(favorites, many=True)
        return Response(serializer.data)

    def post(self, request):
        word_id = request.data.get("word_id")
        if not word_id:
            return Response({"error": "word_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        word = VocabularyWord.objects.get(id=word_id)
        favorite_word, created = FavoriteWord.objects.get_or_create(user=request.user, word=word)
        serializer = FavoriteWordSerializer(favorite_word)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class QuizListCreate(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        quizzes = Quiz.objects.filter(user=request.user)
        serializer = QuizSerializer(quizzes, many=True)
        return Response(serializer.data)

    def post(self, request):
        score = request.data.get("score")
        if score is None:
            return Response({"error": "score is required"}, status=status.HTTP_400_BAD_REQUEST)
        quiz = Quiz.objects.create(user=request.user, score=score)
        serializer = QuizSerializer(quiz)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class Progress(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        learned_count = LearnedWord.objects.filter(user=request.user).count()
        quiz_results = Quiz.objects.filter(user=request.user)
        quiz_serializer = QuizSerializer(quiz_results, many=True)
        return Response({
            "words_learned": learned_count,
            "quiz_results": quiz_serializer.data
        })
