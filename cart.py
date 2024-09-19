# app/suppliers.py
from flask import Blueprint, jsonify, request, session
from app import conn

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    if 'user_id' not in session:
        return jsonify({'message': 'User not logged in'}), 401
    
    user_id = session['user_id']
    cart_items = request.json.get('cartItems', [])
    
    if not cart_items:
        return jsonify({'message': 'No cart items provided'}), 400
    
    cur = conn.cursor()
    for item in cart_items:
        product_id = item['id']
        quantity = item['quantity']
        cur.execute(
            "INSERT INTO carts (u_id, p_id, qty) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE qty = qty + VALUES(qty)",
            (user_id, product_id, quantity)
        )
        conn.commit()
        cur.close()
    
    return jsonify({'message': 'Cart items added successfully!'}), 200

@cart_bp.route('/get_cart_items', methods=['GET'])
def get_cart_items():
    if 'user_id' not in session:
        return jsonify({'message': 'User not logged in'}), 401
    
    user_id = session['user_id']
    cur = conn.cursor()
    cur.execute(
    """
    SELECT 
    c.p_id, 
    p.name, 
    p.imageURL, 
    s.price, 
    SUM(c.qty) AS total_qty, 
    (SELECT SUM(c2.qty) 
     FROM carts c2 
     WHERE c2.u_id = %s) AS sum_all_qty
FROM 
    carts c
JOIN 
    products p ON c.p_id = p.p_id 
JOIN 
    stock s ON p.p_id = s.p_id 
WHERE 
    c.u_id = %s
GROUP BY 
    c.p_id, p.name, p.imageURL, s.price;

    """,
    (user_id,user_id)
)

    cart_items = cur.fetchall()
    cur.close()
    
    print('Cart items fetched from database:', cart_items)  # Debug print statement
    
    return jsonify(cart_items), 200


@cart_bp.route('/delete_item', methods=['POST'])
def delete_cart_item():
    if 'user_id' not in session:
        return jsonify({'message': 'User not logged in'}), 401
    
    user_id = session['user_id']
    product_id = request.json.get('product_id')
    
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM carts WHERE u_id = %s AND p_id = %s",
        (user_id, product_id)
    )
    conn.commit()
    cur.close()
    
    return jsonify({'message': 'Cart item deleted successfully!'}), 200


@cart_bp.route('/update_qty', methods=['POST'])
def update_qty():
    if 'user_id' not in session:
        return jsonify({'message': 'User not logged in'}), 401
    
    user_id = session['user_id']
    product_id = request.json.get('product_id')
    quantity = request.json.get('quantity')
    
    cur = conn.cursor()
    cur.execute(
        "update carts set qty = %s WHERE u_id = %s AND p_id = %s",
        (quantity,user_id, product_id)
    )
    cur = conn.cursor()
    cur.close()

    
    return jsonify({'message': 'Cart item updated successfully!'}), 200



