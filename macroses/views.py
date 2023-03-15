from django.shortcuts import render
from .forms import NameForm
from .logic.dummy_data_changer import change_name_email

from .logic.request_receiver import receive_form

from .models import Greeting

# Create your views here.
def home(request):
    return render(request, 'macroses/home.html', {})

def refunds(request):
    greeting = Greeting.objects.get(id=1)

    if request.method == 'POST':
        form = NameForm(request.POST)
        final_macro = f'{greeting}<br><br>Here is your email: U_EMAIL'

        if form.is_valid():
            final_macro = receive_form(form)

            return render(request, 'macroses/final_macro.html', {
                'final_macro': final_macro
            })
            # in {} i should paste final macro
    else:
        form = NameForm()
        final_macro = ''
    return render(request, 'macroses/home2.html', {
        'form': form,
        'final_macro': final_macro,
    })