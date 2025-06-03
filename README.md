# Agent Wrapper API (Retell + Vapi)

This FastAPI project wraps Retell and Vapi agent creation in a single endpoint.

## Setup

1. Clone the repo
2. Create a `.env` file and add your API keys:

RETELL_API_KEY=your_retell_key
VAPI_API_KEY=your_vapi_key

3. Install dependencies:

pip install -r requirements.txt

4. Run the server:

uvicorn app.main:app --reload

## Usage

### POST /create-agent

Request body:

````json
{
  "provider": "retell",
  "name": "TestAgent",
  "voice_id": "11labs-Adrian",
  ...
}
Supports:

provider = "retell" or "vapi"

(You can customize this further, I can help if you'd like.)

---

### 🔗 5. **Create GitHub repo**
Go to [GitHub](https://github.com), click **"New Repository"**, name it something like:

agent-wrapper-api

**Don’t** initialize with README or .gitignore (you already did locally).

---

### ⬆️ 6. **Push your code**
Back in terminal:

```bash
git add .
git commit -m "Initial commit - working wrapper API for Retell and Vapi"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/agent-wrapper-api.git
git push -u origin main
````
