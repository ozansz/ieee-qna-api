from django.db import models

class Question(models.Model):
    question_text = models.TextField()
    sender_name = models.CharField(max_length=100)
    sender_school = models.CharField(max_length=100)
    sender_email = models.CharField(max_length=100)

    _active = models.BooleanField(default=False)
    
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "<Question #{}: '{}'>".format(self.id, self.question_text[:50] + "...")

    def __repr__(self):
        return self.__str__()