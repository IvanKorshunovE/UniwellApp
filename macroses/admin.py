from django.contrib import admin
from .models import Greeting, Thanking, Apologizing, AskingTheReason, Ending, Tail, Descriptor, PayPalRefund,\
    TransferToBilling, BadMeals, BadWorkouts, NoTime, NoFreeTrial, AfraidNotCancel, Canceled, GoWith, NotUserFriendly, \
    HowMuchWeight

# Register your models here.
admin.site.register(Greeting)
admin.site.register(Thanking)
admin.site.register(Apologizing)
admin.site.register(AskingTheReason)
admin.site.register(Ending)
admin.site.register(Tail)
admin.site.register(Descriptor)
admin.site.register(TransferToBilling)
admin.site.register(PayPalRefund)
admin.site.register(BadMeals)
admin.site.register(BadWorkouts)
admin.site.register(NoTime)
admin.site.register(NoFreeTrial)
admin.site.register(AfraidNotCancel)
admin.site.register(Canceled)
admin.site.register(GoWith)
admin.site.register(NotUserFriendly)
admin.site.register(HowMuchWeight)








