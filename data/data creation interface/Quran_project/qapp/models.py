from django.db import models

class QuestionData(models.Model):
    pq_id = models.TextField()
    context = models.TextField()
    question = models.TextField()
    answer = models.TextField(default='')

    objects = models.Manager()

class FactoidQuestion(models.Model):
    pq_id = models.TextField()
    context = models.TextField()
    question = models.TextField()
    answer = models.TextField(default='')

    objects = models.Manager()

class NonFactoidQuestion(models.Model):
    pq_id = models.TextField()
    context = models.TextField()
    question = models.TextField()
    answer = models.TextField(default='')

class FactoidDone(models.Model):
    pq_id = models.TextField()
    context = models.TextField()
    question = models.TextField()
    answer = models.TextField(default='')

    objects = models.Manager()

class AutomaticQuestion(models.Model):
    pq_id = models.TextField()
    context = models.TextField()
    question = models.TextField()
    answer = models.TextField(default='')
    score = models.TextField(default='3')

class MultipleAutomatic(models.Model):
    pq_id = models.TextField()
    context = models.TextField()
    question = models.TextField()
    answer = models.TextField(default='')
    score = models.TextField(default='3')

class QUQAComplete(models.Model):
    pq_id = models.TextField()
    context = models.TextField()
    question = models.TextField()
    answer = models.TextField(default='')

class QUQA(models.Model):
    pq_id = models.TextField()
    context = models.TextField()
    question = models.TextField()
    answer = models.TextField(default='')

class QaraatiFirst(models.Model):
    pq_id = models.TextField()
    context = models.TextField()
    question = models.TextField()
    answer = models.TextField(default='')

class QaraatiSecond(models.Model):
    pq_id = models.TextField()
    context = models.TextField()
    question = models.TextField()
    answer = models.TextField(default='')

class QaraatiThird(models.Model):
    pq_id = models.TextField()
    context = models.TextField()
    question = models.TextField()
    answer = models.TextField(default='')


class RuleBased(models.Model):
    pq_id = models.TextField()
    context = models.TextField()
    question = models.TextField()
    answer = models.TextField(default='')
