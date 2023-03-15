from ..models import Greeting, Apologizing, AskingTheReason, Ending, Tail
from .dummy_data_changer import change_name_email, change_product
from googletrans import Translator
translator = Translator()


def receive_form(user_form):
    sorted_data = data_sorter(user_form)
    # First you have to select macros
    final_macro = select_macro(user_form)
    # Then substitute all dummy data
    final_macro = change_name_email(final_macro, sorted_data[0], sorted_data[1])
    final_macro = change_product(final_macro, sorted_data)
    # Change language
    final_macro = detect_language(final_macro, sorted_data)
    # Remove spaces from end
    # final_macro = final_macro.strip()
    final_macro = remove_locos(final_macro)
    return final_macro


def select_macro(u_form):
    selected_macro = u_form.cleaned_data['macro']
    final_macro = ''
    if selected_macro == 'RefWhy':
        greeter = Greeting.objects.get(id=1)
        apologize = Apologizing.objects.get(id=1)
        ask_reason = AskingTheReason.objects.get(id=1)
        ending = Ending.objects.get(id=1)
        tail = Tail.objects.get(id=1)
        default_refund_why = [greeter, apologize, ask_reason, ending, tail]
        i = 0
        for part in default_refund_why:
            final_macro += str(part)
            i += 1
            if i < len(default_refund_why):
                final_macro += f' <br><br>'


    return final_macro


def data_sorter(user_form):
    name = user_form.cleaned_data['user_name']
    email = user_form.cleaned_data['user_email']
    product1 = user_form.cleaned_data['product']
    product2 = user_form.cleaned_data['product2']
    refund_amount = user_form.cleaned_data['refund_amount']
    final_date = user_form.cleaned_data['final_date']
    radio_language = user_form.cleaned_data['radio']

    data_list = [name, email, product1, product2, refund_amount, final_date, radio_language]
    return data_list

def detect_language(macro, data_list):
    choice = data_list[6]
    if choice == 'esp':
        translated_macro = translator.translate(macro, dest='es').text
        translated_macro = remove_space_from_beginning(translated_macro)
    elif choice == 'deu':
        translated_macro = translator.translate(macro, dest='de').text
        translated_macro = remove_space_from_beginning(translated_macro)
    elif choice == 'fra':
        translated_macro = translator.translate(macro, dest='fr').text
        translated_macro = remove_space_from_beginning(translated_macro)
    elif choice == 'prt':
        translated_macro = translator.translate(macro, dest='pt').text
        translated_macro = remove_space_from_beginning(translated_macro)
    else:
        return macro
    return translated_macro


def remove_locos(macro):
    'Remove all typos during translation'
    if 'músculos locos' in macro:
        macro = macro.replace('músculos locos', 'Mad Muscles')
    if 'unméale' in macro:
        macro = macro.replace('unméale', 'Unimeal')
    if 'U_agent' in macro:
        macro = macro.replace('U_agent', 'U_AGENT')
    return macro

def remove_space_from_beginning(macro):
    "remove space before each paragraph"
    new_macro = ''
    for x in macro.split('\n'):
        x = x.replace('<br> ', '<br>')
        new_macro += x
    return new_macro



