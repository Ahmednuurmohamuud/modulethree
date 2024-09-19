# app/staff.py
from flask import Blueprint, jsonify, render_template, request, session, url_for, flash, redirect
# from app import mysql
from app import conn


profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile')
def index_profile():
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE u_id = %s", (session['user_id'],))
    profile = cur.fetchall()
    cur.close()

    return render_template('user/profile.html',profile=profile)





@profile_bp.route('/update', methods=['POST'])
def update_user():
    if request.method == 'POST':
        FullName = request.form['name']
        Email = request.form['email']
        Phone = request.form['phone']
        Address = request.form['address']
        Username = request.form['uname']
        Password = request.form['password']
        cur = conn.cursor()
        cur.execute("""
        UPDATE users SET name=%s, email=%s, phone=%s, address=%s, username=%s, password=%s
        WHERE u_id=%s
        """, (FullName, Email,Phone,Address, Username,Password,session['user_id']))
        conn.commit()
        flash("Your Info has Updated Successfully")
        return redirect(url_for('profile.index_profile'))
    




