import pandas as pd
import random
from datetime import datetime, timedelta

# Generating users data
users_data = []
for i in range(1, 101):
    user = {
        'id': i,
        'name': f'User {i}',
        'email': f'user{i}@example.com',
        'password': 'password',
        'address': f'Address {i}'
    }
    users_data.append(user)

users_df = pd.DataFrame(users_data)

# Generating products data
products_data = []
for i in range(1, 21):
    product = {
        'id': i,
        'name': f'Product {i}',
        'description': f'Description for product {i}',
        'price': round(random.uniform(10, 100), 2),
        'stock': random.randint(10, 100)
    }
    products_data.append(product)

products_df = pd.DataFrame(products_data)

# Generating orders data
orders_data = []
order_items_data = []

start_date = datetime.now() - timedelta(days=365)
for i in range(1, 1001):
    date_of_order = start_date + timedelta(days=random.randint(0, 365))
    user_id = random.randint(1, 100)
    order_id = i
    status = random.choice(['completed', 'pending', 'shipped', 'delivered'])

    order_items_count = random.randint(1, 5)
    total_amount = 0

    for j in range(order_items_count):
        product_id = random.randint(1, 20)
        quantity = random.randint(1, 5)
        price = products_df.loc[products_df['id'] == product_id, 'price'].values[0]
        total_amount += price * quantity

        order_item = {
            'id': len(order_items_data) + 1,
            'order_id': order_id,
            'product_id': product_id,
            'quantity': quantity,
            'price': price
        }
        order_items_data.append(order_item)

    order = {
        'id': order_id,
        'user_id': user_id,
        'total_amount': round(total_amount, 2),
        'date_of_order': date_of_order.strftime('%Y-%m-%d'),
        'status': status
    }
    orders_data.append(order)

orders_df = pd.DataFrame(orders_data)
order_items_df = pd.DataFrame(order_items_data)

# Save to CSV files
users_df.to_csv('users.csv', index=False)
products_df.to_csv('products.csv', index=False)
orders_df.to_csv('orders.csv', index=False)
order_items_df.to_csv('order_items.csv', index=False)
