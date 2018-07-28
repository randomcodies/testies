from django.db import models

# Create your models here.
# question 1 has a pk 1

class Questions(models.Model):
    question_text = models.TextField(max_length=300)
    question_title = models.TextField(max_length=300)
    category = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.question_title + ' - ' + self.question_text

class Answers(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    answer = models.TextField(max_length=500)
    submit_answer = models.IntegerField(default=0)
    def __str__(self):
        return self.answer