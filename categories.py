# app/categories.py
from flask import Blueprint, render_template, request, url_for, flash, redirect
from app import conn

category_bp = Blueprint('categories', __name__)

@category_bp.route('/categories')
def index_categories():
    cur = conn.cursor()
    # cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Categories")
    data = cur.fetchall()
    cur.close()
    return render_template('admin/category.html', Categories=data)

@category_bp.route('/insert', methods=['POST'])
def insert_category():
    if request.method == "POST":
        flash("Category Data Inserted Successfully")
        name = request.form['name']
        description = request.form['description']
        # cur = mysql.connection.cursor()
        cur = conn.cursor()
        cur.execute("INSERT INTO Categories (CategoryName, Description) VALUES (%s, %s)", (name, description))
        conn.commit()
        cur.close()
        return redirect(url_for('categories.index_categories'))

@category_bp.route('/delete/<string:id_data>', methods=['GET'])
def delete_category(id_data):
    flash("Category Record Has Been Deleted Successfully")
    cur = conn.cursor()
    # cur = mysql.connection.cursor()
    cur.execute("DELETE FROM Categories WHERE CategoryID=%s", (id_data,))
    conn.commit()
    cur.close()
    return redirect(url_for('categories.index_categories'))

@category_bp.route('/update', methods=['POST'])
def update_category():
    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        description = request.form['description']
        cur = conn.cursor()
        cur.execute("""
        UPDATE Categories SET CategoryName=%s, Description=%s
        WHERE CategoryID=%s
        """, (name, description, id_data))
        conn.commit()
        cur.close()
        flash("Category Data Updated Successfully")
        return redirect(url_for('categories.index_categories'))
