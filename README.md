# TrackIt API 🚀

The secure, cloud-powered backend for the TrackIt mobile application. Built with Django and PostgreSQL, featuring field-level encryption and robust data isolation.

## 🛡️ Key Features
- **User Authentication**: Secure JWT-based auth via SimpleJWT.
- **Data Privacy**: Sensitive fields (Amounts, Descriptions, Weights, Notes) are encrypted at the database level using Fernet (AES-128).
- **Multi-User Isolation**: Automatic filtering ensures users only access their own records.
- **Finance Tracking**: REST API for managing expenses with categorical analysis.
- **Fitness Tracking**: Support for workouts, exercises, and set data with nested serialization.
- **Reliable Static Serving**: Integrated with WhiteNoise for efficient asset management.

## 🛠️ Technology Stack
- **Framework**: Django 6.0 + Django REST Framework
- **Database**: PostgreSQL
- **Security**: Fernet (Encryption), SimpleJWT (Auth)
- **Deployment Ready**: WhiteNoise, Gunicorn compatible, .env configuration

## ⚙️ Setup Instructions

### 1. Clone & Environment
```bash
# Navigate to project
cd trackit_backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment Variables
Create a `.env` file in the root directory:
```env
DEBUG=True
SECRET_KEY=your_django_secret_key
DATABASE_URL=postgres://user:password@localhost:5432/trackit_db
ENCRYPTION_KEY=your_32_byte_base64_key
SALT_KEY=your_random_salt
```

### 3. Database Migration
```bash
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

### 4. Run Server
```bash
python manage.py runserver
```

## 📡 API Endpoints

### Authentication
- `POST /api/auth/register/` - Register new user
- `POST /api/token/` - Get JWT tokens
- `POST /api/token/refresh/` - Refresh access token

### Finance
- `GET /api/finance/expenses/` - List expenses
- `POST /api/finance/expenses/` - Create expense
- `PUT/DELETE /api/finance/expenses/{id}/` - Update/Delete expense

### Fitness
- `GET /api/fitness/workouts/` - List workouts (nested with exercises/sets)
- `POST /api/fitness/workouts/` - Create workout (supports nested creation)
- `GET /api/fitness/routines/` - List training routines

## 🔒 Data Security Note
This project uses `django-fernet-encrypted-fields`. Even a database administrator cannot view sensitive values without the `ENCRYPTION_KEY`. Ensure your `.env` file is never committed to version control.

---
Built by Walker 🤖
