from django import forms

class NameForm(forms.Form):
    user_name = forms.CharField(label='',
                                max_length=100,
                                required=False,
                                widget=forms.TextInput(attrs=
                                {
                                    'placeholder': "User's name",
                                    'class': 'form-control',
                                }))
    user_email = forms.EmailField(label='',
                                  required=False,
                                  widget=forms.EmailInput(attrs=
                                                          {
                                                              'placeholder': 'Enter user\'s email',
                                                              'class': 'form-control',
                                                          }))
    product = forms.CharField(label='',
                                max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs=
                                {
                                    'placeholder': "Product",
                                    'class': 'form-control',
                                    'id': 'id_product'
                                }))
    product2 = forms.CharField(label='',
                                max_length=100,
                                required=False,
                                widget=forms.TextInput(attrs=
                                {
                                    'placeholder': "Product for upsells",
                                    'class': 'form-control',
                                }))
    refund_amount = forms.CharField(label='',
                                max_length=100,
                                required=False,
                                widget=forms.TextInput(attrs=
                                {
                                    'placeholder': "Refund amount",
                                    'class': 'form-control',
                                    'id': 'id_refund_amount'
                                }))
    final_date = forms.CharField(label='',
                                max_length=100,
                                required=False,
                                widget=forms.TextInput(attrs=
                                {
                                    'placeholder': "Final date/UUID",
                                    'class': 'form-control',
                                }))
    #
    # # THIS IS SEEMS TO BE NOT NECESSARY
    # def clear_fields(self):
    #     self.fields['user_name'].initial = ''
    #     self.fields['user_email'].initial = ''
    #     self.fields['product'].initial = ''
    #     self.fields['product2'].initial = ''
    #     self.fields['refund_amount'].initial = ''
    #     self.fields['final_date'].initial = ''
    # # END OF NOT NECESSARY
    #
    # Add the Select widget to the form
    MACRO_CHOICES = (
        ('RefWhy', 'Refund Why'),
        ('PPRef', 'PayPal refund'),
        ('TransferToBill', 'Transfer to billing'),
    )
    macro = forms.ChoiceField(choices=MACRO_CHOICES, label='Macros', widget=forms.Select(attrs={
        'class': 'form-select',
        'style': 'width: 540px; font-size: 25px',
    }))
    #
    clear = forms.CharField(label='Clear', required=False, widget=forms.TextInput(attrs={
        'type': 'button',
        'value': 'Clear',
        'onclick': 'clearFields()',
        'class': 'btn btn-secondary btn-default btn-block',
    }))
    #
    submit = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'type': 'submit',
            'value': 'Generate',
            'class' :"btn btn-primary btn-default btn-block",
        })
    )

    RADIO_CHOICES = (
        ('esp', 'ES'),
        ('deu', 'DE'),
        ('fra', 'FR'),
        ('prt', 'PT'),
        ('eng', 'ENG'),
    )
    radio = forms.ChoiceField(choices=RADIO_CHOICES, label='Radio Buttons', initial='eng', widget=forms.RadioSelect(attrs={
        'class': 'form-check-input',
        'style': 'font-size: 10px; margin-bottom: 25px;',
    }))

    android = forms.BooleanField(label='Android', required=False, widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input',
        'id': 'andr',  # Set the ID of the input
    }))

    apple = forms.BooleanField(label='Apple', required=False, widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input',
        'id': 'appl',  # Set the ID of the input
    }))

    descriptor = forms.BooleanField(label='Descriptor charges', required=False, widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input',
        'id': 'descr',  # Set the ID of the input
    }))

    no_time = forms.BooleanField(label='No Time', required=False, widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input',
        'id': 'notime',  # Set the ID of the input
    }))