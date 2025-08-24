from django.urls import path
from .views import (
    RegisterUser,
    LoginUser,
    CategoryList,
    WordListCreateView,
    VocabularyWordList,
    VocabularyWordDetail,
    LearnedWordListCreate,
    FavoriteWordListCreate,
    QuizListCreate,
    Progress
)

urlpatterns = [
    # User accounts
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),

    # Categories
    path('categories/', CategoryList.as_view(), name='categories'),

    # Words (basic Word model API)
    path('word/', WordListCreateView.as_view(), name='word'),

    # Vocabulary
    path('words/', VocabularyWordList.as_view(), name='words'),
    path('words/<int:pk>/', VocabularyWordDetail.as_view(), name='word-detail'),

    # Learned words
    path('learned/', LearnedWordListCreate.as_view(), name='learned'),

    # Favorite words
    path('favorite/', FavoriteWordListCreate.as_view(), name='favorite'),

    # Quizzes
    path('quiz/', QuizListCreate.as_view(), name='quiz'),

    # Progress
    path('progress/', Progress.as_view(), name='progress'),
]
