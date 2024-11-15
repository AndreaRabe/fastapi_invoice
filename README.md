---

# **Invoice management**  

A backend application built with FastAPI for managing and generating invoices efficiently.  

---

## **Table of Contents**

1. [Overview](#overview)  
2. [Features](#features)  
3. [Technologies Used](#technologies-used)  
4. [Installation](#installation)  
5. [Usage](#usage)  
6. [Contact](#contact)  

---

## **Overview**

Invoice management is a robust and scalable backend solution for invoice management. It provides a RESTful API to create, update, retrieve, and manage invoice records efficiently. This application is suitable for businesses and developers looking for an easy-to-integrate invoicing system.  

---

## **Features**

- Create and manage invoice records via API.  
- Update existing invoices with new details.  
- Retrieve detailed information for invoices.  
- Fast and efficient API performance using FastAPI.  
- Built-in data validation and serialization.  

---

## **Technologies Used**

- **FastAPI**: Framework for building APIs.  
- **SQLAlchemy**: For database ORM.  
- **SQLite** (default) or any database supported by SQLAlchemy.  
- **Pydantic**: For data validation and serialization.  
- **Uvicorn**: ASGI server for running the application.  

---

## **Installation**

### Prerequisites  
- Python 3.10 or later.  

### Steps  

1. Clone this repository:  
   ```bash
   git clone https://github.com/AndreaRabe/fastapi_invoice.git
   ```  

2. Navigate to the project directory:  
   ```bash
   cd fastapi_invoice
   ```  

3. Create and activate a virtual environment:  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```  

4. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  

5. Start the FastAPI server:  
   ```bash
   uvicorn main:app --reload
   ```  

6. Open your browser and navigate to `http://127.0.0.1:8000/docs` to explore the API documentation.  

---

## **Usage**

- Use the Swagger UI at `/docs` for API testing.  
- Use `/redoc` for alternative API documentation.  
- Interact with the endpoints to create, retrieve, and manage invoices.  

---

### Example JSON Payload for Invoice Creation:
```json
{
  "customer_name": "John Doe",
  "amount": 250.75,
  "due_date": "2024-12-31"
}
```

## **Contact**

- **Author**: Andrea Rabe   
- **Email**: [nantenainaandrea2@gmail.com](mailto:nantenainaandrea2@gmail.com)  

---
