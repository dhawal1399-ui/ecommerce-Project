# 🛒 E-commerce Project (Django + React)

This is a full-stack e-commerce application built using Django (REST Framework) for the backend and React for the frontend. It supports user authentication, product management, cart and checkout system, role-based access, and admin order control.

---

## 🚀 Features

### ✅ Customer Side
- User Registration and Login with JWT
- Browse Products and View Details
- Add to Cart, Update Quantity, Remove Items
- Checkout and Place Order
- View My Orders with Product Breakdown

### 🛠 Admin Panel
- Add/Edit/Delete Products and Categories
- View All Orders with Product and Customer Info
- Admin-only Access to Dashboard
- Role-based Navigation (Admin vs Customer)

---

## 🧱 Tech Stack

| Layer      | Technology                        |
|------------|------------------------------------|
| Frontend   | React, React Router DOM, Context API |
| Backend    | Django, Django REST Framework      |
| Auth       | JWT (Access + Refresh tokens)      |
| Database   | SQLite (default, can be changed to PostgreSQL/MySQL) |
| Styling    | Basic CSS / Custom Stylesheets     |

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/dhawal1399-ui/ecommerce-Project.git
cd ecommerce-Project


cd backend   

python -m venv venv
source venv/bin/activate   

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py runserver



cd frontend  

npm install
npm start

ecommerce-Project/
│
├── backend/              # Django backend
│   ├── manage.py
│   ├── store/            # Main Django app
│   └── ...
│
├── frontend/             # React frontend
│   ├── src/
│   ├── public/
│   └── ...
│
├── README.md
└── .gitignore

📦 API Endpoints
Endpoint	Method	Description
/api/products/	GET	List all products
/api/cart/	POST	Add item to cart
/api/order/	POST	Place order from cart
/api/order/	GET	Get logged-in user orders
/api/admin/orders/	GET	Admin view of all orders
/api/token/	POST	Get JWT access & refresh
/api/token/refresh/	POST	Refresh JWT access token



🧑‍💼 Author
Dhawal Somkuwar
Email: dhawalsomkuwar2@gmail.com
GitHub: https://github.com/dhawal1399-ui

---

Let me know if you'd like:
- A deployment section (Render, Heroku, Vercel)
- Screenshots/Badges
- Live demo hosted link added

I'm happy to tailor it further!
