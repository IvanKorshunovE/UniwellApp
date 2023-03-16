from ..models import Greeting, Apologizing, AskingTheReason, Ending, Tail, PayPalRefund, TransferToBilling, Thanking
from .dummy_data_changer import change_name_email, change_product, define_currency, refund_sum, change_agent_name
from googletrans import Translator
from .checkboxes import get_data_for_checkboxes
from .other_checkboxes import afraid_not_cancel, no_free_trial, no_time, bad_meals, bad_workouts
translator = Translator()


def receive_form(user_form):
    """
    First - we select macro - then we should do checkboxes login.
    :param user_form:
    :return:
    """
    sorted_data = data_sorter(user_form)
    # Checkboxes



    # First you have to select macros
    final_macro = select_macro(user_form, sorted_data)


    # Then substitute all dummy data
    final_macro = change_name_email(final_macro, sorted_data[0], sorted_data[1])
    final_macro = change_product(final_macro, sorted_data)
    final_macro = define_currency(final_macro, sorted_data)
    final_macro = refund_sum(final_macro, sorted_data)
    final_macro = change_agent_name(final_macro, sorted_data)
    # Change language
    final_macro = detect_language(final_macro, sorted_data)
    # Remove spaces from end
    # final_macro = final_macro.strip()
    final_macro = remove_locos(final_macro)
    return final_macro

# 7, 8, 9, 10, 11, 12, 13, 14
def select_macro(u_form, sorted_data):
    checkmark_trues = [sorted_data[10], sorted_data[12], sorted_data[13]]
    checkmark_trues2 = [sorted_data[10], sorted_data[12], sorted_data[13], sorted_data[7], sorted_data[8],
                        sorted_data[9], sorted_data[11], sorted_data[14]]
    selected_macro = u_form.cleaned_data['macro']
    final_macro = ''
    if selected_macro == 'RefWhy':
        greeter = Greeting.objects.get(id=1)
        if sorted_data[14]:
            apologize = Thanking.objects.get(id=1)
        else:
            apologize = Apologizing.objects.get(id=1)
        ####
        if True in checkmark_trues:
            ask_reason = AskingTheReason.objects.get(id=2) # Are there anything else?
        else:
            ask_reason = AskingTheReason.objects.get(id=1)
        ###
        ending = Ending.objects.get(id=1)
        tail = Tail.objects.get(id=1)

        selected_macro = [greeter, apologize, ask_reason, ending, tail]

        if sorted_data[13]:  # Check if bad workouts
            bad_workouts_2 = bad_workouts(sorted_data)
            selected_macro.insert(2, bad_workouts_2)

        if sorted_data[12]:  # Check if bad meals
            if 'MM' in sorted_data[2] and sorted_data[13]:
                pass
            bad_meals2 = bad_meals(sorted_data)
            selected_macro.insert(2, bad_meals2)

        if sorted_data[10]:  # Check if no time checkbox is active
            no_time_part = no_time(sorted_data)
            selected_macro.insert(2, no_time_part)

        if sorted_data[9]: # Check if descriptor checkbox is active
            descriptor = get_data_for_checkboxes(sorted_data)
            selected_macro.insert(2, descriptor)

        if sorted_data[14]: # Check if not free trial checkbox is checked
            free_trial_absent = no_free_trial(sorted_data)
            selected_macro.insert(2, free_trial_absent)

        if sorted_data[11]: # Check if afraid not cancel
            afraid_not_canceled = afraid_not_cancel(sorted_data)
            selected_macro.insert(2, afraid_not_canceled)

        i = 0
        for part in selected_macro:
            if len(str(part)) < 3:
                # print(' ____ ----- ______ ------ _______ --------_____ _-----____')
                continue
            final_macro += str(part)
            i += 1
            if i < len(selected_macro):
                final_macro += f' <br><br>'

    elif selected_macro == 'PPRef':
        greeter = Greeting.objects.get(id=1)
        apologize = Apologizing.objects.get(id=1)
        pp_refund_part = PayPalRefund.objects.get(id=1)
        ending = Ending.objects.get(id=2)
        tail = Tail.objects.get(id=1)

        selected_macro = [greeter, apologize, pp_refund_part, ending, tail]

        if sorted_data[13]:  # Check if bad workouts
            bad_workouts_2 = bad_workouts(sorted_data)
            selected_macro.insert(2, bad_workouts_2)

        if sorted_data[12]:  # Check if bad meals
            bad_meals2 = bad_meals(sorted_data)
            selected_macro.insert(2, bad_meals2)

        if sorted_data[10]: # Check if no time checkbox is active
            no_time_part = no_time(sorted_data)
            selected_macro.insert(2, no_time_part)

        if sorted_data[9]: # Check if descriptor checkbox is active
            descriptor = get_data_for_checkboxes(sorted_data)
            selected_macro.insert(2, descriptor)

        if sorted_data[14]: # Check if not free trial checkbox is checked
            free_trial_absent = no_free_trial(sorted_data)
            selected_macro.insert(2, free_trial_absent)

        if sorted_data[11]: # Check if afraid not cancel
            afraid_not_canceled = afraid_not_cancel(sorted_data)
            selected_macro.insert(2, afraid_not_canceled)

        i = 0
        for part in selected_macro:
            if len(str(part)) < 3:
                # print(' ____ ----- ______ ------ _______ --------_____ _-----____')
                continue
            final_macro += str(part)
            i += 1
            if i < len(selected_macro):
                final_macro += f' <br><br>'

    elif selected_macro == 'TransferToBill':
        greeter = Greeting.objects.get(id=1)
        thank = Thanking.objects.get(id=1)
        transfer_to_billing = TransferToBilling.objects.get(id=1)
        ending = Ending.objects.get(id=2)
        tail = Tail.objects.get(id=1)

        selected_macro = [greeter, thank, transfer_to_billing, ending, tail]

        if True in checkmark_trues2:
            any_other_reason = TransferToBilling.objects.get(id=2)
            selected_macro.insert(2, any_other_reason)

        if sorted_data[13]:  # Check if bad workouts
            bad_workouts_2 = bad_workouts(sorted_data)
            selected_macro.insert(2, bad_workouts_2)

        if sorted_data[12]:  # Check if bad meals
            if 'MM' in sorted_data[2] and sorted_data[13]:
                pass
            bad_meals2 = bad_meals(sorted_data)
            selected_macro.insert(2, bad_meals2)

        if sorted_data[10]: # Check if no time checkbox is active !!! Do not change ORDER!!!
            no_time_part = no_time(sorted_data)
            selected_macro.insert(2, no_time_part)

        if sorted_data[9]: # Check if descriptor checkbox is active
            descriptor = get_data_for_checkboxes(sorted_data)
            selected_macro.insert(2, descriptor)

        if sorted_data[14]: # Check if not free trial checkbox is checked
            free_trial_absent = no_free_trial(sorted_data)
            selected_macro.insert(2, free_trial_absent)

        if sorted_data[11]: # Check if afraid not cancel
            afraid_not_canceled = afraid_not_cancel(sorted_data)
            selected_macro.insert(2, afraid_not_canceled)


        i = 0
        for part in selected_macro:
            if len(str(part)) < 2:
                # print(' ____ ----- ______ ------ _______ --------_____ _-----____')
                continue
            final_macro += str(part)
            i += 1
            if i < len(selected_macro):
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
    checkbox_Android = user_form.cleaned_data['android']
    checkbox_Apple = user_form.cleaned_data['apple']
    checkbox_Descriptor = user_form.cleaned_data['descriptor']
    checkbox_No_Time = user_form.cleaned_data['no_time']
    checkbox_afraid_not_cancel = user_form.cleaned_data['afraid_did_not_receive']
    checkbox_bad_meals = user_form.cleaned_data['bad_meals']
    checkbox_bad_workout = user_form.cleaned_data['bad_workouts']
    checkbox_no_free_trial = user_form.cleaned_data['free_trial']
    selected_macro = user_form.cleaned_data['macro']

    data_list = [
        name,  # 0
        email,  # 1
        product1,  # 2
        product2,  # 3
        refund_amount,  # 4
        final_date,  # 5
        radio_language,  # 6
        checkbox_Android,  # 7
        checkbox_Apple,  # 8
        checkbox_Descriptor,  # 9
        checkbox_No_Time,  # 10
        checkbox_afraid_not_cancel,  # 11
        checkbox_bad_meals,  # 12
        checkbox_bad_workout,  # 13
        checkbox_no_free_trial,  # 14
        selected_macro,  # 15
    ]
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
    elif choice == 'it':
        translated_macro = translator.translate(macro, dest='it').text
        translated_macro = remove_space_from_beginning(translated_macro)
    elif choice == 'prt':
        translated_macro = translator.translate(macro, dest='pt').text
        translated_macro = remove_space_from_beginning(translated_macro)
    else:
        return macro
    return translated_macro


def remove_locos(macro):
    'Remove all typos during translation'
    macro = macro.replace('músculos locos', 'Mad Muscles')
    macro = macro.replace('unméale', 'Unimeal')
    macro = macro.replace('U_agent', 'U_AGENT')
    macro = macro.replace('saluti', 'Saluti')
    macro = macro.replace('saluti', 'Saluti')
    macro = macro.replace('etano', 'Ethan')
    return macro

def remove_space_from_beginning(macro):
    "remove space before each paragraph"
    new_macro = ''
    for x in macro.split('\n'):
        x = x.replace('<br> ', '<br>')
        new_macro += x
    return new_macro
