
def change_name_email(macro, u_name='', u_email=''):
    name = u_name.strip().lower().capitalize()
    email = u_email.strip()

    if len(name) == 0:
        macro = macro.replace('U_NAME', '')
    else:
        macro = macro.replace('U_NAME', f' {name}')

    if len(email) == 0:
        macro = macro.replace('U_EMAIL', '')
    else:
        macro = macro.replace('U_EMAIL', f' {email}')
    return macro