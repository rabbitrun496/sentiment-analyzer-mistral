# 🧠 Sentiment Analyzer using Mistral (via Ollama)

## 📌 Overview

A simple AI-powered app that analyzes the **sentiment** of any text you enter using the **Mistral** language model via **Ollama**, with:

- 🧠 **Mistral** via Ollama – runs locally, no API keys needed
- ⚙️ **FastAPI** – handles the backend and model interaction
- 🖼️ **Streamlit** – provides a simple user interface for input/output

---

## 🧰 Tech Stack

- [Ollama](https://ollama.com) – Run LLMs locally
- [FastAPI](https://fastapi.tiangolo.com/) – Modern Python web framework
- [Streamlit](https://streamlit.io) – Frontend UI for apps
- Python 3.10+ with `venv`

---

## ⚙️ Setup Instructions

### 🔹 Step 1: Set up the environment

1. Create and activate a virtual environment:

```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # macOS/Linux
```

2. Install the dependencies:

```bash
pip install fastapi uvicorn streamlit requests python-multipart
```

3. Save your installed packages:

```bash
pip freeze > requirements.txt
```

---

### 🔹 Step 2: Install and run Ollama

1. Download and install Ollama: [https://ollama.com](https://ollama.com)  
2. Pull the Mistral model:

```bash
ollama pull mistral
```

3. Start the model:

```bash
ollama run mistral
```

Keep this running in a terminal window.

---

### 🔹 Step 3: Run the backend (FastAPI)

1. Navigate to your project root.
2. Start the FastAPI server:

```bash
uvicorn backend.main:app --reload
```

- Visit the auto-generated docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### 🔹 Step 4: Run the frontend (Streamlit)

In a separate terminal (activate `venv` again if needed):

```bash
streamlit run frontend/app.py
```

Visit [http://localhost:8501](http://localhost:8501) to use the app.

---

## 🗂️ Structure

```
Sentiment-Analyzer using Mistral via Ollama
├── backend/
│   └── main.py
├── frontend/
│   └── app.py
├── venv/                # local virtual environment (not pushed to GitHub)
├── requirements.txt
└── README.md
```

---

## 🧪 Features

- Accepts user text via a web interface
- Sends the text to a locally hosted LLM (Mistral via Ollama)
- Returns a sentiment classification: **Positive**, **Negative**, or **Neutral**

---

## ⚠️ Notes

- Ensure Ollama is running **before** you start the backend.
- `venv/` is typically excluded using `.gitignore` and **should not be pushed to GitHub**.

## 📝 License

This project is licensed under the [MIT License](LICENSE).

### Acknowledgements

- This project uses [FastAPI](https://fastapi.tiangolo.com/) licensed under the **MIT License**.
- It also uses [Streamlit](https://streamlit.io/) licensed under the **Apache License 2.0**.
- The language model **Mistral 7B** is licensed under the **Apache License 2.0**.
- The model is served locally using [Ollama](https://ollama.com), a proprietary tool.
- Works fully offline once set up.

---



