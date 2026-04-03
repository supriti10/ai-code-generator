# 💻 AI Code Generator (LLaMA 3 + Streamlit)

An AI-powered code assistant that can **generate, explain, and debug code** using LLaMA 3 via Groq API.
Built with a simple and clean UI using Streamlit.

## 🌐 Live Demo  
🔗 https://ai-code-generator-s10.streamlit.app/

---

## 🚀 Features

* ✨ Generate code from natural language prompts
* 📘 Explain code step-by-step
* 🐞 Debug and fix errors in code
* ⚡ Fast responses using LLaMA 3 (Groq API)
* 🎯 Clean and structured output (no unnecessary explanations)
* 📥 Download generated code

---

## 🛠 Tech Stack

* **Frontend:** Streamlit
* **Backend Logic:** Python
* **LLM API:** Groq (LLaMA 3)
* **Libraries:** openai, python-dotenv

---

## 📁 Project Structure

```
ai-code-generator/
│
├── app.py
├── llama_api.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
└── utils/
    └── prompt_templates.py
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/supriti10/ai-code-generator.git
cd ai-code-generator
```

---

### 2. Create virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Add API Key

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

### 5. Run the application

```
streamlit run app.py
```

---

## 🧠 How It Works

1. User enters a prompt in the UI
2. Prompt is processed using prompt engineering
3. Request is sent to LLaMA 3 via Groq API
4. AI generates structured output
5. Output is displayed in Streamlit UI

---

## 🎯 Example Prompts

* Write a Python function for binary search
* Explain this Java code
* Fix this error in C++ code

---

## 🔐 Security Note

* API keys are stored in `.env`
* `.env` is excluded using `.gitignore`
* No sensitive data is exposed

---

## 📌 Future Improvements

* Chat history (memory)
* Multi-language detection
* Code execution support
* Deployment on cloud

---
