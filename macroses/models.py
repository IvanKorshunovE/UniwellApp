from django.db import models

# Create your models here.
class Greeting(models.Model):
    greeting = models.TextField('Greeting', max_length=120)

    def __str__(self):
        return self.greeting

class Thanking(models.Model):
    thanking = models.TextField('Thanking', max_length=2000)

    def __str__(self):
        return self.thanking


class Apologizing(models.Model):
    apologizing = models.TextField('Apologizing', max_length=4000)

    def __str__(self):
        return self.apologizing


class AskingTheReason(models.Model):
    ask_reason = models.TextField('AskingTheReason', max_length=4000)

    def __str__(self):
        return self.ask_reason


class Ending(models.Model):
    ending = models.TextField('Ending', max_length=2100)

    def __str__(self):
        return self.ending


class Tail(models.Model):
    tail = models.TextField('The most end part', max_length=120)

    def __str__(self):
        return self.tail
