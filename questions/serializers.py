from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Question
from answers.models import Answer
from django.core.exceptions import ObjectDoesNotExist

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        exclude = ('_active',)

class QuestionAnswerSerializer(ModelSerializer):
    answer_text = SerializerMethodField()
    sender_name = SerializerMethodField()

    class Meta:
        model = Question
        fields = ('question_text', 'sender_name', 'sender_school', 'answer_text')

    def get_answer_text(self, obj):
        try:
            if obj.answer != None:
                return obj.answer.answer_text
            else:
                return None
        except ObjectDoesNotExist:
            return None

    def get_sender_name(self, obj):
        nfs = obj.sender_name.split(" ")

        if len(nfs) > 1:
            name = " ".join([n.capitalize() for n in nfs[:-1]])
            name += " " +  nfs[-1][0].upper() + "."
        else:
            name = nfs[0].capitalize()

        return name