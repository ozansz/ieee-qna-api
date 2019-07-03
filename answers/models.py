from django.db import models

from questions.models import Question

class Answer(models.Model):
    question = models.OneToOneField(
        Question,
        related_name="answer",
        on_delete=models.CASCADE
    )

    answer_text = models.TextField()

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "<Answer to {}>".format(repr(self.question))

    def __repr__(self):
        return self.__str__()