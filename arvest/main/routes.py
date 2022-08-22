from flask import Blueprint, render_template, request, url_for, redirect
main = Blueprint('main', __name__)

@main.route('/')
def error_page():
    return redirect(url_for('portals.signin'))

@main.route('/syncing-account')
def syncing():
    return render_template('syncing.html')
