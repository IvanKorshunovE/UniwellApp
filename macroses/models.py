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


class Descriptor(models.Model):
    descriptor = models.TextField('Descriptor', max_length=5000)

    def __str__(self):
        return self.descriptor


class PayPalRefund(models.Model):
    pay_pal_refund = models.TextField('PayPal refund', max_length=5000)

    def __str__(self):
        return self.pay_pal_refund


class TransferToBilling(models.Model):
    transfer_to_billing = models.TextField('Transfer to billing', max_length=5000)

    def __str__(self):
        return self.transfer_to_billing


class AfraidNotCancel(models.Model):
    afraid_not_cancel = models.TextField('Afraid not cancel', max_length=5000)

    def __str__(self):
        return self.afraid_not_cancel


class NoFreeTrial(models.Model):
    no_free_trial = models.TextField('No free trial', max_length=5000)

    def __str__(self):
        return self.no_free_trial


class NoTime(models.Model):
    no_time = models.TextField('No Time', max_length=5000)

    def __str__(self):
        return self.no_time


class BadMeals(models.Model):
    bad_meals = models.TextField('Bad Meals', max_length=5000)

    def __str__(self):
        return self.bad_meals


class BadWorkouts(models.Model):
    bad_workouts = models.TextField('bad workouts', max_length=5000)

    def __str__(self):
        return self.bad_workouts