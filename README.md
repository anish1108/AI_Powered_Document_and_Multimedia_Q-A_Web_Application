

An AI-powered web application that allows users to upload **PDFs, audio, or video files**, automatically extract or transcribe content, and interact with it through a **chatbot interface**.

The system generates summaries and answers user questions using the uploaded content as context.

---

## 🚀 Features

✅ Upload PDF, Audio, or Video files  
✅ Automatic speech-to-text transcription (Deepgram API)  
✅ PDF text extraction  
✅ AI Chatbot Q&A over uploaded content  
✅ Auto-generated summaries  
✅ Timestamp-based answers for media files  
✅ Media player with jump-to-time functionality  
✅ Clean React + Tailwind UI  
✅ Django REST backend

---

## 🏗️ Tech Stack

### Backend
- Django 6
- Django REST Framework
- Deepgram (Speech-to-Text)
- Groq API (LLM for Q&A)
- Sumy (Text Summarization)
- Python

### Frontend
- React (Vite)
- Tailwind CSS
- Axios

---





---

## ⚙️ Setup Guide

---

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-chat-bot.git
cd ai-chat-bot
```

---

## 🧠 Backend Setup (Django)

### Create Virtual Environment

```bash
cd backend
python -m venv venv
```

Activate:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Environment Variables

Create a `.env` file inside `backend/`:

```
DEEPGRAM_API_KEY=your_deepgram_key
GROQ_API_KEY=your_groq_key
```

---

### Run Migrations

```bash
python manage.py migrate
```

---

### Start Backend Server

```bash
python manage.py runserver
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

## 🎨 Frontend Setup (React)

Open new terminal:

```bash
cd frontend
npm install
```

Run frontend:

```bash
npm run dev
```

Frontend runs at:

```
http://localhost:5173
```

---

## 📡 API Endpoints

---

### Upload File

```
POST /api/user/upload/
```

FormData:
```
file: <pdf | audio | video>
```

Response:
```json
{
  "transcript_id": 1,
  "file_url": "/media/uploads/file.mp3"
}
```

---

### Ask Question

```
POST /api/user/ask/
```

FormData:
```
transcript_id
question
```

Response:
```json
{
  "answer": "Explanation based on uploaded content",
  "start_time": 35.2
}
```

---

### Generate Summary

```
POST /api/user/summary/
```

FormData:
```
transcript_id
```

Response:
```json
{
  "summary": "Short summary of uploaded content..."
}
```

---

## 🧪 Testing the Application

### Step-by-step Test Flow

1. Start backend server
2. Start frontend server
3. Open browser → `localhost:5173`
4. Upload:
   - PDF OR
   - Audio OR
   - Video file
5. Wait for processing
6. Navigate to Chat page
7. Ask questions about content
8. View summary panel
9. Click timestamps to jump media playback

---

## 🧠 How It Works

### Processing Pipeline

#### PDF
```
Upload → Text Extraction → Database Storage → Chat Context
```

#### Audio / Video
```
Upload
   ↓
Deepgram Transcription
   ↓
Transcript Saved
   ↓
AI Q&A via Groq
```

---

### Question Answering Flow

```
User Question
      ↓
Fetch Transcript
      ↓
Send Context + Question to LLM
      ↓
Generate Answer
      ↓
Return Timestamp (if media)
```

---

## 🔐 Security Notes

- API keys stored in `.env`
- `.env` excluded via `.gitignore`
- CSRF disabled only for development APIs

---

## 🧩 Future Improvements

- Streaming chat responses
- Semantic search (vector embeddings)
- Multi-file workspace
- User authentication
- Cloud storage support
- Background task queue (Celery)




