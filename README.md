# 🧠 AI Gold Investment Advisor
<img width="1536" height="1024" alt="kuber-ai" src="https://github.com/user-attachments/assets/53c6175c-6763-44ba-b675-76b052d2c36d" />


### GenAI + PyTorch Backend System

An end-to-end **Generative AI inspired backend system** that simulates the workflow of an AI financial assistant similar to *Kuber AI*.
The system analyzes user queries related to gold investment, provides financial insights, and nudges users toward purchasing **digital gold** through a simulated purchase API.

The project demonstrates **AI-driven interaction, API orchestration, financial insight generation, and cloud deployment**.

---

# 🚀 Live Deployment

API Documentation (Swagger UI)

```
http://98.94.2.43:8000/docs
```

The company can test the APIs directly from this interface.

---

# 🏗 System Architecture

```
User Query
   ↓
Chat API (FastAPI)
   ↓
Intent Detection (PyTorch-based logic)
   ↓
Gold Investment Advice
   ↓
Purchase Nudge
   ↓
Digital Gold Purchase API
   ↓
Gold Price Simulation
   ↓
SQLite Transaction Storage
   ↓
AWS EC2 Deployment
```

---

# ⚙️ Features

✔ AI-style intent detection for gold investment queries
✔ Financial insight generation for investment decisions
✔ Digital gold purchase simulation
✔ Transaction storage in database
✔ Cloud deployment on AWS
✔ Interactive API testing via Swagger UI

---

# 📡 API Endpoints

## 1️⃣ AI Chat API

Detects gold-related investment questions and responds with financial insights.

**Endpoint**

```
POST /chat
```

**Example Request**

```json
{
  "message": "Is gold a good investment?"
}
```

**Example Response**

```json
{
  "type": "gold_investment",
  "response": "Gold is considered a stable investment and can hedge against inflation. You can invest in digital gold through the Simplify Money app.",
  "next_action": "awaiting_user_confirmation"
}
```

---

## 2️⃣ Digital Gold Purchase API

Simulates the purchase of digital gold and records the transaction.

**Endpoint**

```
POST /buy-gold
```

**Example Request**

```json
{
  "user": "demo",
  "amount": 500
}
```

**Example Response**

```json
{
  "status": "success",
  "gold_price_per_gram": 6500,
  "amount_invested": 500,
  "gold_purchased_grams": 0.0769
}
```

---

# 🧰 Tech Stack

| Technology | Purpose                          |
| ---------- | -------------------------------- |
| Python     | Core programming language        |
| FastAPI    | High-performance API framework   |
| PyTorch    | AI workflow logic                |
| SQLite     | Lightweight transaction database |
| Uvicorn    | ASGI server                      |
| AWS EC2    | Cloud deployment                 |

---

# 📂 Project Structure

```
kuber-ai
│
├── app
│   ├── main.py
│   ├── chat_api.py
│   ├── purchase_api.py
│   ├── database.py
│   ├── llm_service.py
│   └── gold_price_service.py
│
├── requirements.txt
└── README.md
```

---

# ☁️ Deployment

The project is deployed on **AWS EC2** using an Ubuntu server.

Server configuration:

* Instance: `t2.micro`
* Python virtual environment
* FastAPI served via **Uvicorn**

Run server:

```
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

---

# 🔮 Future Improvements

* Integration with real gold price APIs
* Fine-tuned transformer model for intent detection
* Conversational memory for multi-turn dialogue
* Web chat interface for better user interaction
* Secure payment simulation

---

# 📌 Key Learning Outcomes

This project demonstrates:

* Building **GenAI-inspired backend systems**
* Designing **REST APIs for AI applications**
* Implementing **financial insight workflows**
* Managing **database transactions**
* Deploying **AI services to cloud infrastructure**

---

# 👨‍💻 Author

**Prerit**

Data Science & AI Enthusiast

## 📥 Clone the Repository

Clone the project to your local machine using Git:

```bash
git clone https://github.com/YOUR_USERNAME/kuber-ai.git
cd kuber-ai
```

---

## ⚙️ Setup Environment

Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate

pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Then open the API documentation:

```
http://localhost:8000/docs
```

