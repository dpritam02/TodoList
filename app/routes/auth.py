
from flask import Blueprint,render_template,request,redirect,url_for,flash,session

auth_bp = Blueprint('auth',__name__)

# dummy user
USER_CREDENTIAL = {
    'username' : 'admin',
    'password' : '1234'
}

@auth_bp.route('/login', methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        if username == USER_CREDENTIAL['username'] and password == USER_CREDENTIAL['password']:
            session['user'] = username

            flash("Logged in Successfully", 'success')
        else:
            flash("Inavlid username or password", 'Authentication issue!')
    
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged out successfully', 'info')
    return redirect(url_for('auth.login'))
