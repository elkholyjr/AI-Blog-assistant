# ✍️ AI Blog Assistant
Link: https://ai-blog-assistant.streamlit.app/
<img width="1206" height="684" alt="image" src="https://github.com/user-attachments/assets/e877f374-edb2-4255-873a-c5e6617b972e" />


An intelligent, interactive **AI-powered blog post generator** built with **Streamlit** and **Google Gemini Pro (gemini-2.5-pro)**.

## 📌 Project Overview

This tool allows users to generate engaging, informative, and keyword-rich blog posts simply by entering a blog title, keywords, and desired word count. It leverages Google's Gemini Pro LLM via API to generate high-quality blog content in real time.

---

## 🚀 Features

- Input blog title and keywords
- Choose word count (100 to 3000)
- Interactive Streamlit UI with real-time blog generation
- Keyword integration into content
- Sidebar form for input, main screen for output
- Configurable number of images (feature-ready)

---

## 🧠 How It Works

1. The user provides:
   - Blog Title
   - Keywords (comma-separated)
   - Desired word count
   - Number of images (UI support)

2. The app builds a prompt and sends it to Google Gemini Pro using the `google.genai` Python SDK.

3. The response is streamed and displayed in the app with formatting.

4. The tone is designed to be engaging, consistent, and SEO-friendly.

---

## 🔧 Technologies Used

- `Python`
- `Streamlit`
- `Google Gemini Pro (via google.genai)`
- `GoogleSearch Tool` integration for context (optional tool)

---

## 🛠️ Challenges Faced & How I Solved Them

| Challenge | Solution |
|----------|----------|
| **Getting Gemini API working with Streamlit** | Properly managed API key using a separate `apikey.py` file to keep credentials secure |
| **Ensuring streaming content display** | Used `generate_content_stream` to stream response for better UI experience |
| **Prompt design for keyword integration** | Crafted a custom prompt template that ensures all keywords are naturally integrated |
| **Handling empty inputs** | Added form validation logic to prevent submission without required fields |

---

## 🧪 Example Prompt

**Title**: "The Future of AI in Content Creation"  
**Keywords**: "AI blogging, content automation, Gemini Pro"  
**Word Count**: 500

The app will generate a full blog post based on this setup.

---

## 🗂️ File Structure

```
📁 AI-Blog-Assistant
├── apikey.py              # Your secure Google Gemini API key
├── main.py                # Main Streamlit app file
├── README.md              # This file
├── requirements.txt       # Dependencies
```
---
