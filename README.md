Inventory Management API
A simple and efficient API built with Django and Django Ninja to manage inventory products. It supports CRUD operations for products, including details like name, price, quantity, and supplier. The API features error handling for missing resources and an easy-to-use Django Admin interface for managing data.

Features
Create, Read, Update, and Delete products.

Link products to suppliers.

RESTful API with Django Ninja.

Installation
Clone the repo: git clone https://github.com/your-username/inventory-management-api.git

Set up a virtual environment and install dependencies: pip install -r requirements.txt

Run migrations: python manage.py migrate

Start the server: python manage.py runserver

Access the API at http://127.0.0.1:8000/api/ and the admin panel at http://127.0.0.1:8000/admin/.
