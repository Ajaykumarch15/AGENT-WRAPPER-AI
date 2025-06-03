

---


# 🎙️ Agent Wrapper API (Retell + Vapi)

This project is a FastAPI wrapper that allows you to create agents for **Retell AI** and **Vapi** via a **single unified endpoint**.

---

## 🚀 Features

- ✅ Unified `/create-agent` endpoint
- ✅ Supports both **Retell** and **Vapi** agent creation
- ✅ Easy to configure with `.env` file
- ✅ Clean error handling and response formatting
- ✅ Ready for production use and extensible for more providers

---

## 🛠️ Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/agent-wrapper-api.git
cd agent-wrapper-api
````

### 2. Create `.env` File

Add your API keys to a `.env` file:

```env
RETELL_API_KEY=your_retell_api_key
VAPI_API_KEY=your_vapi_api_key
```

> ⚠️ Do **not** share your API keys publicly.

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI Server

```bash
uvicorn app.main:app --reload
```

---

## 📡 API Usage

### Endpoint

```
POST /create-agent
```

### Request Body

```json
{
  "provider": "retell", // or "vapi"
  "name": "TestAgent",
  "voice_id": "11labs-Adrian",
  "response_engine": {
    "type": "retell-llm",
    "llm_id": "llm_XXXXXXXX"
  }
}
```

> For **Retell**, the following fields are required:
>
> * `provider`
> * `name`
> * `voice_id`
> * `response_engine` with valid `type` and `llm_id`

> For **Vapi**, structure must match their API schema exactly (no `voice_id` inside `voice` object).

### Example with `curl`

```bash
curl -X POST http://localhost:8000/create-agent \
  -H "Content-Type: application/json" \
  -d '{
    "provider": "retell",
    "name": "DemoAgent",
    "voice_id": "11labs-Adrian",
    "response_engine": {
      "type": "retell-llm",
      "llm_id": "llm_xxxxxxxx"
    }
  }'
```

---

## 🧾 File Structure

```
agent-wrapper-api/
├── app/
│   ├── main.py
│   ├── schemas.py
│   └── services/
│       ├── retell.py
│       └── vapi.py
├── .env                 # API keys (excluded from Git)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 👨‍💻 Contributing

Pull requests are welcome! Feel free to fork the repo and propose enhancements.

---

## 🛡️ License

This project is licensed under the MIT License.

---

## 💬 Need Help?

Open an issue or reach out via GitHub if you face any issues.

```

✅ You're now ready to commit and push this file:


git add README.md
git commit -m "Add detailed README"
git push
```

