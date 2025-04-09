# 🎬 YouTube Transcript Summarizer

> ✨ Let the app watch the YouTube lecture for you and give you the TL;DR.

This Streamlit-powered web app allows users to paste a YouTube video link and automatically fetch its transcript using the `youtube-transcript-api`, then summarizes the content using an NLP model (`facebook/bart-large-cnn`). Perfect for students, researchers, and anyone who wants to extract insights from long videos—fast.

---

## 📌 Features

- 🔗 **Paste a YouTube link** — the app extracts the transcript (if available)
- 🧠 **Summarizes with Transformers** — uses BART from Hugging Face to generate clear, concise summaries
- 📄 **Supports manual and pre-existing transcripts**
- ⚡ **Simple UI** built with Streamlit — no coding needed!

---

## 🚀 Demo

![App Screenshot](https://via.placeholder.com/800x400?text=Add+your+Streamlit+Cloud+link+here)

Try it live on [Streamlit Cloud](https://share.streamlit.io/...) (replace this link once deployed).

---

## 🛠️ Tech Stack

- `Python 3.8+`
- [`streamlit`](https://streamlit.io/)
- [`youtube-transcript-api`](https://pypi.org/project/youtube-transcript-api/)
- [`transformers`](https://huggingface.co/transformers/)
- [`facebook/bart-large-cnn`](https://huggingface.co/facebook/bart-large-cnn)

---

## 📥 Installation

### Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/youtube-transcript-summarizer.git
cd youtube-transcript-summarizer
