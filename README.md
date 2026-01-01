# 🍎 AI Fruit Drawing Recognizer

An interactive web application that recognizes hand-drawn fruit sketches using a machine learning model served through a FastAPI backend.

---

## 📑 Table of Contents
- [Project Overview](#project-overview)
- [Motivation](#motivation)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Installation Prerequisites](#installation-prerequisites)
  - [How to Run the Project Locally](#how-to-run-the-project-locally)
  - [Quick Demo](#quick-demo)
- [Architecture Overview](#architecture-overview)
- [Future Development](#future-development)
- [Acknowledgements & Resources](#acknowledgements--resources)

---

## 📌 Project Overview
The **AI Fruit Drawing Recognizer** is a full-stack web application that allows users to draw pixel-based fruit images on a custom canvas and receive real-time predictions from a trained machine learning model.

---

## 💡 Motivation
This project was built to explore end-to-end AI application development, combining frontend drawing interfaces with backend machine learning inference through a REST API.

---

## ✨ Features
- Pixel-based drawing canvas
- Color picker, eraser, and clear grid tools
- Grid-based input optimized for ML predictions
- Fruit classification using a **Keras** model
- **FastAPI** backend serving predictions
- Clean and interactive UI

---

## 🚀 Getting Started

### 🔧 Installation Prerequisites
Ensure you have the following installed:

- Python 3.9+
- pip
- Git

Required Python libraries:
- fastapi  
- uvicorn  
- keras  
- numpy  
- pillow  

---

### ▶️ How to Run the Project Locally

1. Clone the repository:
```
bash
git clone https://github.com/your-username/ai-fruit-drawing-recognizer.git
cd ai-fruit-drawing-recognizer

```

2. Create and activate a virtual environment:

```
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate     # Windows

```

3. Install dependencies:

```
pip install -r requirements.txt

```

4. Start the FastAPI backend:

```
uvicorn main:app --reload
```

5. Open the frontend

Open index.html in your browser

Or serve it using a local server