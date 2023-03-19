from ..models import AfraidNotCancel, NoFreeTrial, NoTime, BadMeals, BadWorkouts, Canceled, NotUserFriendly, \
    HowMuchWeight


def how_much_weight(sorted_data):
    weight = HowMuchWeight.objects.get(id=1)
    final_parts = [weight]
    return build_checkbox_part(final_parts)

def not_user_friendly(sorted_data):

    checkbox_list = [
        sorted_data[9],  # descriptor
        sorted_data[11],  # Afraid not cancel
        sorted_data[12],  # Bad meals (should come first)
        sorted_data[13],  # Bad workouts (should come first)
    ]

    if 'MM' in sorted_data[2]:
        if True in checkbox_list:  # Additionally (if other checkboxes marked)
            part1 = NotUserFriendly.objects.get(id=9)
        else:
            part1 = NotUserFriendly.objects.get(id=8)
        if 'upsell' in sorted_data[2]:
            part2 = NotUserFriendly.objects.get(id=6)
        else:
            part2 = NotUserFriendly.objects.get(id=7)
        final_parts = [part1, part2]
    else:
        if True in checkbox_list:
            part1 = NotUserFriendly.objects.get(id=5)
        else:
            part1 = NotUserFriendly.objects.get(id=1)
        if 'upsell' in sorted_data[2]:
            part2 = NotUserFriendly.objects.get(id=2)
        else:
            part2 = NotUserFriendly.objects.get(id=3)
        part3 = NotUserFriendly.objects.get(id=4)
        final_parts = [part1, part2, part3]

    return build_checkbox_part(final_parts)


def cancel_the_sub(sorted_data):
    canceled = Canceled.objects.get(id=1)
    return build_checkbox_part([canceled])


def afraid_not_cancel(sorted_data):
    afraid = AfraidNotCancel.objects.get(id=1)
    double_check = AfraidNotCancel.objects.get(id=2)
    afraid_not_cancel_part = [afraid, double_check]
    return build_checkbox_part(afraid_not_cancel_part)


def no_free_trial(sorted_data):
    no_free_tr = NoFreeTrial.objects.get(id=1)
    no_free_part = [no_free_tr]
    return build_checkbox_part(no_free_part)


def no_time(sorted_data):
    selected_macro = sorted_data[15]

    checkbox_list = [
        sorted_data[9],  # descriptor
        sorted_data[11],  # Afraid not cancel
        sorted_data[12],  # Bad meals (should come first)
        sorted_data[13],  # Bad workouts (should come first)
        sorted_data[14],  # No free trial
    ]

    no_time_part = []

    if 'UM' in sorted_data[2]:
        if True in checkbox_list:
            no_time = NoTime.objects.get(id=2)
            no_time_part.append(no_time)
        else:
            no_time = NoTime.objects.get(id=1)
            no_time_part.append(no_time)
    else:
        no_time_sorry = NoTime.objects.get(id=6)
        if True in checkbox_list:
            no_time1 = NoTime.objects.get(id=9)
        else:
            no_time1 = NoTime.objects.get(id=3)  # First part for both upsell and no upsell
        no_time3 = NoTime.objects.get(id=5)  # Second part for both upsell and no upsell
        if selected_macro != 'RefWhy':
            no_time_part.append(no_time_sorry)  # To avoid double-sorry.
        no_time_part.append(no_time1)
        no_time_part.append(no_time3)

        if 'upsell' in sorted_data[2]:
            no_time2 = NoTime.objects.get(id=4)
            no_time_meals_healthy = NoTime.objects.get(id=7)
            no_time_part.insert(2, no_time2)
            no_time_part.append(no_time_meals_healthy)
        else:
            no_time_workouts_healthy = NoTime.objects.get(id=8)
            no_time_part.append(no_time_workouts_healthy)

    return build_checkbox_part(no_time_part)


def bad_meals(sorted_data):
    bad_meals_part = []

    checkbox_list = [
        sorted_data[9],  # descriptor
        sorted_data[9],  # no time
        sorted_data[11],  # Afraid not cancel
        sorted_data[13],  # Bad workouts (should come first)
        sorted_data[14],  # No free trial
    ]

    if True in checkbox_list:
        if 'UM' in sorted_data[2]:
            um_part1 = BadMeals.objects.get(id=2)
            bad_meals_part.append(um_part1)
            um_part2 = BadMeals.objects.get(id=3)
            bad_meals_part.append(um_part2)
            um_part3 = BadMeals.objects.get(id=4)
            bad_meals_part.append(um_part3)
        else:
            bad_meals_part.append('')
    else:
        if 'UM' in sorted_data[2]:
            um_part1 = BadMeals.objects.get(id=1)
            bad_meals_part.append(um_part1)
            um_part2 = BadMeals.objects.get(id=3)
            bad_meals_part.append(um_part2)
            um_part3 = BadMeals.objects.get(id=4)
            bad_meals_part.append(um_part3)
        else:
            if 'upsell' in sorted_data[2]:
                mm_part = BadMeals.objects.get(id=5)
                um_part3 = BadMeals.objects.get(id=4)
                bad_meals_part.append(mm_part)
                bad_meals_part.append(um_part3)
            else:
                bad_meals_part.append('!!! USER DOES NOT HAVE MEAL PLAN !!!')

    return build_checkbox_part(bad_meals_part)


def bad_workouts(sorted_data):
    bad_workouts_part = []

    checkbox_list = [
        sorted_data[9],  # descriptor
        sorted_data[9],  # no time
        sorted_data[11],  # Afraid not cancel
        sorted_data[12],  # Bad meals
        sorted_data[14],  # No free trial
    ]

    if True in checkbox_list:
        if 'MM' in sorted_data[2]:
            if not sorted_data[12]:
                mm_part1 = BadWorkouts.objects.get(id=2)  # Let me also provide
            else:
                mm_part1 = BadWorkouts.objects.get(id=7)
            bad_workouts_part.append(mm_part1)
            mm_part2 = BadWorkouts.objects.get(id=3)  # Assistant feature
            bad_workouts_part.append(mm_part2)
            if not sorted_data[12]:  # If BAD MEALS CHECKBOX is NOT checked
                mm_part3 = BadWorkouts.objects.get(id=4)  # If you don't like a suggested exercise, click "Swap" next
                # to it to have it replaced.
                bad_workouts_part.append(mm_part3)
            else:
                mm_part3 = BadWorkouts.objects.get(id=5)
                bad_workouts_part.append(mm_part3)
                if 'upsell' in sorted_data[2]:
                    mm_part3_1 = BadWorkouts.objects.get(id=6)  # Exersice or MEAL
                else:
                    mm_part3_1 = '!!! USER DOES NOT HAVE MEAL PLAN (if you want that instructions type upsell in ' \
                                 'product field)!!!'
                bad_workouts_part.append(mm_part3_1)
                if 'upsell' in sorted_data[2]:
                    mm_part3_5 = BadMeals.objects.get(id=4)
                else:
                    mm_part3_5 = '!!! USER DOES NOT HAVE MEAL PLAN (if you want that instructions type upsell in ' \
                                 'product field)!!!'
                bad_workouts_part.append(mm_part3_5)
        else:
            um = BadMeals.objects.get(id=6)
            bad_workouts_part.append(um)
    else:
        if 'MM' in sorted_data[2]:
            mm_part1 = BadWorkouts.objects.get(id=1)  # Let me provide
            bad_workouts_part.append(mm_part1)
            mm_part2 = BadWorkouts.objects.get(id=3)
            bad_workouts_part.append(mm_part2)
            mm_part3 = BadWorkouts.objects.get(id=4)
            bad_workouts_part.append(mm_part3)
            mm_part4 = BadWorkouts.objects.get(id=5)
            bad_workouts_part.append(mm_part4)
        else:
            um = BadMeals.objects.get(id=6)
            bad_workouts_part.append(um)

    return build_checkbox_part(bad_workouts_part)


def build_checkbox_part(text_parts: list):
    final_text = ''
    i = 0
    for part in text_parts:
        if len(str(part)) < 3:
            continue
        final_text += str(part)
        i += 1
        if i < len(text_parts):
            final_text += f' <br><br>'
    return final_text
