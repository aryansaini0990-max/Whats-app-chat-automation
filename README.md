# 🤖 WhatsApp AI Chatbot Automation

## 📌 Project Overview

This project is a **Python-based AI chatbot automation tool** that reads messages from a chat screen (like WhatsApp Web), detects incoming messages, and automatically replies using an AI model.

It simulates human-like conversations in **Hinglish (Hindi + English)** and behaves like a real person instead of a bot.

---

## 🚀 Features

* 📥 Automatically reads chat messages from screen
* 🤖 Generates AI-based replies using OpenAI API
* 💬 Responds in natural Hinglish tone
* 🧠 Maintains conversational context from chat history
* ⚡ Fully automated (no manual typing needed)
* 🎯 Detects last sender before replying

---

## 🛠️ Tech Stack

* **Python**
* **PyAutoGUI** – for screen automation
* **Pyperclip** – for clipboard handling
* **OpenAI API** – for generating responses
* **Regex (re)** – for message parsing

---

## 📂 Project Workflow

1. **Click on Chat Window**

   * The bot focuses on the chat area using screen coordinates.

2. **Capture Chat History**

   * Selects and copies chat text from screen.

3. **Identify Sender**

   * Checks whether the last message is from the target sender (e.g., "Brother").

4. **Generate AI Response**

   * Sends chat history to OpenAI API.
   * Generates a human-like reply.

5. **Send Message**

   * Pastes the response into the chat box.
   * Presses Enter to send automatically.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-chatbot-automation.git
cd ai-chatbot-automation
```

### 2. Install Dependencies

```bash
pip install pyautogui pyperclip openai
```

### 3. Set API Key

Replace this line:

```python
api_key="Api key"
```

with your actual OpenAI API key.

---

## ▶️ Usage

1. Open **WhatsApp Web / Chat Window**
2. Make sure screen coordinates match your system
3. Run the script:

```bash
python chatbot.py
```

⚠️ **Important:**
Do not move your mouse while the bot is running.

---

## 📍 Customization

### Change Sender Name

```python
def is_last_message_from_sender(chat_log, sender_name="Brother"):
```

### Change Chat Personality

Modify system prompt:

```python
"You act as a chatbot..."
```

You can:

* Change tone (formal / flirty / funny)
* Change language (Hindi / English / Hinglish)
* Customize personality

---

## ⚠️ Limitations

* Works based on **fixed screen coordinates**
* Requires proper screen resolution setup
* Not officially supported by WhatsApp (use responsibly)
* May fail if UI layout changes

---

## 🔐 Disclaimer

This project is for **educational purposes only**.
Use automation responsibly and respect privacy & platform policies.

---

## 💡 Future Improvements

* 📸 OCR-based message detection (no coordinates needed)
* 🧠 Memory-based conversation tracking
* 🌐 Multi-platform support (Telegram, Instagram)
* 🎛️ GUI dashboard for control

---

## 👨‍💻 Author

**Aryan**
Aspiring Data Scientist & AI Developer

---

## ⭐ Support

If you like this project:

* Give it a ⭐ on GitHub
* Share with friends 🚀

---
