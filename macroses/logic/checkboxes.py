from ..models import Greeting, Apologizing, AskingTheReason, Ending, Tail, Descriptor


def get_data_for_checkboxes(sorted_data):
    period = get_period(sorted_data)  # Returns list of [[trial_period, full_period], [trial_price, full_price]]
    descriptor_part = build_descriptor_part(period, sorted_data)  # Returns descriptor part with full data
    return descriptor_part


def get_period(sorted_data, defauld=True):
    """
    get: data list with all info regarding the form
    :return: lists
    """
    if defauld: # If defauld=True - means that there is no upsell (product2 is empty) Line 147
        periods = sorted_data[2]  # Here we get text from Period1 field.
    else:
        periods = sorted_data[3]
    to_parse = periods.split()
    lll = ['7', '3', '6', 'month', '3months', 'months', 'days', '1', 'Weekly']
    periods_1 = [x for x in to_parse if x in lll]
    if ',' in periods:
        price = [x for x in to_parse if ',' in x]
    else:
        price = [x for x in to_parse if '.' in x]

    if len(periods_1) == 4 and len(price) == 2:
        trial_period = f'{periods_1[0]} {periods_1[1]}'
        full_period = f'{periods_1[2]} {periods_1[3]}'
        trial_price = f'{price[0]}'
        full_price = f'{price[1]}'
        if trial_period == '3 months':
            trial_period = '3-month'
        if trial_period == '6 months':
            trial_period = '6-month'
        return [[trial_period, full_period], [trial_price, full_price]]
    elif len(periods_1) == 3:
        trial_period = f'{periods_1[0]} {periods_1[1]}'
        full_period = f'{periods_1[2]}'
        trial_price = f'{price[0]}'
        full_price = f'{price[1]}'
        if trial_period == '7 days':
            trial_period = '7-day'
        return [[trial_period, full_period], [trial_price, full_price]]
    elif (len(periods_1) == 2 and len(price) == 2) or (len(periods_1) == 2 and len(price) == 1):
        if periods_1[0] == 'month' and periods_1[1] == 'month':
            trial_period = 'first month'
            full_period = periods_1[1]
            trial_price = price[0]
            full_price = price[1]
            return [[trial_period, full_period], [trial_price, full_price]]
        elif len(periods_1) == 2 and len(price) == 2:
            return [[periods_1[0], periods_1[1]], [price[0], price[1]]]
        else:
            return [[periods_1[1]], [price[0]]]
    elif len(periods_1) == 1:
        if periods_1[0] == '3months':
            full_period = f'3 months'
            full_price = f'{price[0]}'
            return [[full_period], [full_price]]
        elif periods_1[0] == 'Weekly':
            full_period = f'week'
            full_price = f'{price[0]}'
            return [[full_period], [full_price]]
        elif periods_1[0] == 'month':
            trial_period = 'first month'
            full_period = periods_1[0]
            trial_price = price[0]
            full_price = price[1]
            return [[trial_period, full_period], [trial_price, full_price]]


def build_descriptor_part(list_with_period, sorted_data):
    email_field = sorted_data[1]
    product_2_field = len(sorted_data[3]) == 0
    product_2_field_text = sorted_data[3]
    final = list_with_period
    if len(final[1]) == 2 and final[1][0] != final[1][1] and product_2_field:
        may_clarify = Descriptor.objects.get(id=1)
        describe_terms = Descriptor.objects.get(id=3)
        needed_to_be_canceled = Descriptor.objects.get(id=5)
        links = Descriptor.objects.get(id=6)
        sorry = Descriptor.objects.get(id=7)
        canceled = Descriptor.objects.get(id=8)
        descriptor_part = [
            may_clarify,
            describe_terms,
            needed_to_be_canceled,
            links,
            sorry,
            canceled,
        ]
        if len(email_field) > 0:
            email = Descriptor.objects.get(id=2)
            descriptor_part.insert(1, email)
    elif not product_2_field:
        may_clarify = Descriptor.objects.get(id=1)
        describe_terms = Descriptor.objects.get(id=9)
        needed_to_be_canceled = Descriptor.objects.get(id=5)
        links = Descriptor.objects.get(id=6)
        sorry = Descriptor.objects.get(id=7)
        canceled = Descriptor.objects.get(id=8)
        descriptor_part = [
            may_clarify,
            describe_terms,
            needed_to_be_canceled,
            links,
            sorry,
            canceled,
        ]
        if len(email_field) > 0:
            email = Descriptor.objects.get(id=2)
            descriptor_part.insert(1, email)
    else:
        may_clarify = Descriptor.objects.get(id=1)
        describe_terms = Descriptor.objects.get(id=4)
        needed_to_be_canceled = Descriptor.objects.get(id=5)
        links = Descriptor.objects.get(id=6)
        sorry = Descriptor.objects.get(id=7)
        canceled = Descriptor.objects.get(id=8)
        descriptor_part = [
            may_clarify,
            describe_terms,
            needed_to_be_canceled,
            links,
            sorry,
            canceled,
        ]
        if len(email_field) > 0:
            email = Descriptor.objects.get(id=2)
            descriptor_part.insert(1, email)

    final_text = ''
    i = 0
    for part in descriptor_part:
        final_text += str(part)
        i += 1
        if i < len(descriptor_part):
            final_text += f' <br><br>'

    if len(final[1]) == 2 and final[1][0] != final[1][1] and product_2_field:
        final_text = final_text.replace('U_TRIAL_PERIOD', final[0][0])
        final_text = final_text.replace('U_TRIAL_PRICE', final[1][0])
        final_text = final_text.replace('U_FULL_PERIOD', final[0][1])
        final_text = final_text.replace('U_FULL_PRICE', final[1][1])
    elif not product_2_field:
        product_2_terms = get_period(sorted_data, False)
        final_text = final_text.replace('U_TRIAL_PERIOD', product_2_terms[0][1])
        final_text = final_text.replace('U_TRIAL_PRICE', product_2_terms[1][0])

        final_text = final_text.replace('U_FULL_PERIOD', final[0][1])
        final_text = final_text.replace('U_FULL_PRICE', final[1][1])
        final_text = final_text.replace('U_ADDPAYMENT', final[1][0])
        if 'MM' in sorted_data[2]:
            final_text = final_text.replace('U_WORKOUT_MEAL', 'meal plan')
        else:
            final_text = final_text.replace('U_WORKOUT_MEAL', 'workout plan')
    else:
        final_text = final_text.replace('U_FULL_PERIOD', final[0][0])
        final_text = final_text.replace('U_FULL_PRICE', final[1][0])

    return final_text

# def exclude_descriptor_short(macro):
#     '''
#
#     :param macro: macro in string
#     :return: macro in string
#     '''
#     final = self.get_period()
#     if len(final[1]) == 2 and final[1][0] != final[1][1]:
#         # Then EXCLUDE SHORT MACRO
#         # print(final[0][0])
#         macro = macro.replace('U_TRIAL_PERIOD', final[0][0])
#         macro = macro.replace('U_TRIAL_PRICE', final[1][0])
#         macro = macro.replace('U_FULL_PERIOD', final[0][1])
#         macro = macro.replace('U_FULL_PRICE', final[1][1])
#     else:
#         # Then EXCLUDE LONG MACRO
#         macro = macro.replace('U_FULL_PERIOD', final[0][0])
#         macro = macro.replace('U_FULL_PRICE', final[1][0])
#     return macro


# def descriptor_part(self):
#     des_charges_dictionary = self.descriptor_charges_dictionary.copy()
#     final = self.get_period()
#     if self.ref_descriptor_charges_checkbox.isChecked():
#         if self.lineEdit_2.text() == '':
#             des_charges_dictionary.pop('Purchased')
#         if len(final[1]) == 2 and final[1][0] != final[1][1]:
#             des_charges_dictionary.pop('Short price')
#         else:
#             des_charges_dictionary.pop('Long price')
#         return [x[0] for x in des_charges_dictionary.values()]
