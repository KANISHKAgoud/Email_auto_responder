# Email_auto_responder

vercel deployed link :- https://email-auto-responder-zeta.vercel.app/

# 📧 NLP-Based Personalized Email Auto-Responder

An intelligent email auto-responder system that uses Natural Language Processing (NLP) to analyze incoming emails and generate context-aware, personalized replies based on intent and tone.

---

## 🚀 Features

* 🔍 **Intent Detection** (Complaint, Meeting, Job, Gratitude, Urgent)
* 🎭 **Tone Analysis** (Angry, Formal, Friendly, Urgent)
* 🤖 **Automated Response Generation**
* 🌐 **Interactive Web Interface**
* ⚡ **Real-time API communication using Flask**

---

## 🧠 Tech Stack

### 🔹 Backend

* Python
* Flask
* Scikit-learn
* NLTK

### 🔹 Frontend

* HTML
* Tailwind CSS
* JavaScript

---

## ⚙️ How It Works

1. User enters an email
2. Text is preprocessed (cleaning, stopword removal)
3. Converted into numerical form using TF-IDF
4. ML models predict:

   * Intent
   * Tone
5. System generates a personalized response
6. Output is displayed on the frontend

---

## 📁 Project Structure

```
email_auto_responder/
│
├── backend/
│   ├── app.py
│   ├── train_model.py
│   ├── model/
│   └── utils/
│
├── frontend/
│   ├── index.html
│   ├── script.js
│
├── requirements.txt
└── README.md
```

---

## 🛠️ Installation & Setup (Run Locally)

### 🔹 1. Clone the Repository

```
git clone https://github.com/your-username/Email_auto_responder.git
cd Email_auto_responder
```

---

### 🔹 2. Install Dependencies

```
pip install -r requirements.txt
```

---

### 🔹 3. Train the Model

```
cd backend
python train_model.py
```

---

### 🔹 4. Run Backend Server

```
python app.py
```

---

### 🔹 5. Run Frontend

Open `frontend/index.html` in your browser

---

## 🌐 Deployment

### 🔹 Frontend

Deployed on Vercel

### 🔹 Backend

Deployed on Render

---

## 🧪 Example Input

```
I am very unhappy with your service. Please respond immediately.
```

### 🔹 Output

* Intent: Complaint
* Tone: Angry
* Response: "We sincerely apologize for the inconvenience..."

---

## 🚧 Limitations

* Uses a small dataset (basic accuracy)
* Rule-based response generation
* Not using deep learning models yet

---

## 🚀 Future Enhancements

* Integration with Gmail API
* Use of BERT for better NLP performance
* Improved dataset (e.g., Enron Email Dataset)
* User-based personalization
* AI-generated responses using LLMs

---

## 🏆 Author

**Kanishka Goud**

---

## ⭐ If you like this project

Give it a star on GitHub ⭐
