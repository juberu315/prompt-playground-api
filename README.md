# Prompt Playground API

A FastAPI-based playground API for testing, improving, and experimenting with AI prompts using the OpenAI API.

This project is designed to help developers learn prompt engineering techniques, AI response formatting, structured JSON extraction, and AI-powered text generation using FastAPI and OpenAI.

---

## 🚀 Features

- FastAPI backend
- OpenAI API integration
- Prompt engineering practice
- AI text rewriting
- Text classification
- JSON extraction from unstructured text
- AI email generation
- Prompt improvement endpoint
- Swagger API documentation
- Beginner-friendly structure

---

## 🛠 Tech Stack

- Python 3.12
- FastAPI
- OpenAI API
- Uvicorn
- Pydantic
- python-dotenv

---

## 📁 Project Structure

```txt
prompt-playground-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── schemas.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── openai_service.py
│
├── .env
├── .env.example
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/prompt-playground-api.git
cd prompt-playground-api
```

---

### 2. Create virtual environment

```bash
python -m venv venv
```

---

### 3. Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

---

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory.

```env
OPENAI_API_KEY=your_openai_api_key_here
```

Get your API key from the OpenAI API platform.

---

## ▶️ Run the Server

```bash
uvicorn app.main:app --reload
```

Server URL:

```txt
http://127.0.0.1:8000
```

Swagger API docs:

```txt
http://127.0.0.1:8000/docs
```

ReDoc documentation:

```txt
http://127.0.0.1:8000/redoc
```

---

# 📡 API Endpoints

---

## 1. Rewrite Text

### Endpoint

```http
POST /rewrite
```

### Request

```json
{
  "text": "This product is very good",
  "tone": "professional"
}
```

### Response

```json
{
  "result": "This product delivers excellent performance and reliability."
}
```

---

## 2. Classify Text

### Endpoint

```http
POST /classify
```

### Request

```json
{
  "text": "I want a refund for my order."
}
```

### Response

```json
{
  "category": "customer_support"
}
```

---

## 3. Extract JSON

### Endpoint

```http
POST /extract-json
```

### Request

```json
{
  "text": "John Smith, email john@example.com, budget $5000"
}
```

### Response

```json
{
  "name": "John Smith",
  "email": "john@example.com",
  "budget": 5000
}
```

---

## 4. Generate Email

### Endpoint

```http
POST /generate-email
```

### Request

```json
{
  "topic": "Meeting Request",
  "tone": "professional"
}
```

### Response

```json
{
  "email": "Dear John,\n\nI hope you are doing well..."
}
```

---

## 5. Improve Prompt

### Endpoint

```http
POST /improve-prompt
```

### Request

```json
{
  "prompt": "write blog"
}
```

### Response

```json
{
  "improved_prompt": "Write a detailed SEO-friendly blog post about modern AI development trends."
}
```

---

# 📦 Example Requirements

```txt
fastapi
uvicorn
openai
python-dotenv
pydantic
```

---

# 🎯 Learning Goals

This project helps you learn:

- FastAPI fundamentals
- API route creation
- Request and response validation
- OpenAI API integration
- Prompt engineering basics
- Structured AI outputs
- JSON response formatting
- AI backend architecture
- Environment variable management

---

# 🧠 Prompt Engineering Concepts Practiced

- Clear instructions
- Role prompting
- Output formatting
- JSON generation
- Tone control
- Constraints
- Few-shot prompting
- Anti-hallucination prompts

---

# 🚧 Future Improvements

- Streaming AI responses
- Conversation memory
- Authentication
- Rate limiting
- Token usage tracking
- Database integration
- Docker support
- Frontend playground UI
- AI agent workflows

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

Built as a practice project for learning FastAPI, Prompt Engineering, and OpenAI API development.