from rest_framework.generics import ListAPIView, CreateAPIView

from .models import Question
from .serializers import QuestionSerializer, QuestionAnswerSerializer

class QuestionPostView(CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionListView(ListAPIView):
    queryset = Question.objects.all().filter(_active=True)
    serializer_class = QuestionAnswerSerializer