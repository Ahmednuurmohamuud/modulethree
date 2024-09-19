# app/staff.py
from flask import Blueprint, current_app,  jsonify, render_template, request, url_for, session,flash, redirect
from app import ALLOWED_EXTENSIONS
from app import conn
import os
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename

login_bp = Blueprint('login', __name__)

@login_bp.route('/login')
def index_login():
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            p.p_id, p.name, c.CategoryName, p.imageURL, p.description, s.price, p.date, 
            c.CategoryID
        FROM products p 
        JOIN categories c ON p.c_id = c.CategoryID
        JOIN stock s ON p.p_id = s.p_id
        where s.qty >=1
    """)
    data = cur.fetchall()
    cur.close()

    return render_template('user/login.html', products=data)

@login_bp.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        
        # Check if the user is an admin
        cur = conn.cursor()
        cur.execute("SELECT id, username FROM admin WHERE username = %s AND password = %s", (username, password))
        admin = cur.fetchone()
        
        if admin:
            # Admin login successful
            session['user_id'] = admin[0]
            session['username'] = admin[1]
            session['role'] = 'admin'
            return render_template('admin/base.html')
        
        # Check in the users table for regular users if not admin
        cur.execute("SELECT u_id, username FROM users WHERE username = %s AND password = %s", (username, password))
        user = cur.fetchone()
        cur.close()

        if user:
            # User login successful
            session['user_id'] = user[0]
            session['username'] = user[1]
            session['role'] = 'user'
            # Execute the query to get the cart quantity for the user
            cur = conn.cursor()
            cur.execute("SELECT SUM(qty) FROM carts WHERE u_id = %s", (session['user_id'],))
            cart = cur.fetchone()
            cur.close()

            # Handle cases where no cart items are found
            if cart[0] is None:
                session['cartqty'] = 0
            else:
                session['cartqty'] = cart[0]
            return redirect(url_for('menu.index_menu'))
        else:
            flash('Invalid username or password')
            return redirect(url_for('login.login'))

        
@login_bp.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.')
    return render_template('user/login.html')  








