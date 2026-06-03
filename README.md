# Order Service API

REST API для управління клієнтами, товарами та замовленнями, реалізований на FastAPI з використанням SQLAlchemy Async та Alembic.

## Технології

* Python 3.12
* FastAPI
* SQLAlchemy 2.0 (Async)
* SQLite
* Alembic
* Pydantic

## Структура проєкту

```text
app/
├── crud/
├── models/
├── routers/
├── schemas/
├── services/
├── database.py
├── dependencies.py
└── main.py

alembic/
requirements.txt
README.md
```

## Встановлення

### 1. Клонувати репозиторій

```bash
git clone <https://github.com/alexx5039-bot/order-service>

```

### 2. Створити та активувати віртуальне середовище

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Встановити залежності

```bash
pip install -r requirements.txt
```

## Міграції бази даних

Застосувати всі міграції:

```bash
alembic upgrade head
```

## Запуск проєкту

```bash
uvicorn app.main:app --reload
```

Після запуску документація буде доступна за адресою:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

### Customers

#### Створити клієнта

```http
POST /customers
```

Приклад:

```json
{
  "name": "John Doe",
  "email": "john@example.com"
}
```

---

### Products

#### Створити товар

```http
POST /products
```

Приклад:

```json
{
  "name": "Calculator",
  "price": 50.00
}
```

---

### Orders

#### Створити замовлення

```http
POST /orders
```

Приклад:

```json
{
  "customer_id": 1,
  "items": [
    {
      "product_id": 1,
      "quantity": 2
    },
    {
      "product_id": 3,
      "quantity": 1
    }
  ]
}
```

#### Отримати всі замовлення клієнта

```http
GET /orders/customer/{customer_id}
```

Приклад:

```http
GET /orders/customer/1
```

## Реалізований функціонал

* Створення клієнтів
* Створення товарів
* Створення замовлень
* Підтримка декількох товарів в одному замовленні
* Автоматичний розрахунок суми замовлення
* Отримання всіх замовлень клієнта
* Валідація вхідних даних
* Міграції через Alembic
* Асинхронна робота з базою даних

## Автор

Oleksandr Kalnyi
