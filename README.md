# Student Assist AI Chatbot: Retrieval-Augmented Study Partner

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-brightgreen.svg)](https://streamlit.io/)

A powerful, multimodal AI chatbot built with **Google Gemini** and **Streamlit** to help students study. This application uses **Retrieval-Augmented Generation (RAG)** to allow students to upload their own study materials (PDFs, notes, images) and ask specific, contextual questions about them.

##  Features

The Student Assist AI Chatbot acts as an expert tutor, capable of handling various academic documents:

* **Multimodal RAG (Retrieval-Augmented Generation):** Upload your own files, and the chatbot will use the content to provide highly contextual and accurate answers.
* **Document Support:** Supports text extraction from **PDF** (`.pdf`), **Word** (`.docx`), and general text files.
* **Image-to-Text (OCR):** Uses **pytesseract** to perform Optical Character Recognition on uploaded images (e.g., photos of handwritten notes, whiteboard snapshots, or scanned book pages).
* **Persistent Chat History:** Maintains conversation context for natural, multi-turn interactions.
* **Supportive Persona:** The AI is instructed to maintain an encouraging, academic, and professional tone.
* **Simple UI:** Built with Streamlit for a clean, user-friendly interface.

##  Project Structure
##  Quick Setup

### 1. Prerequisites

Before running the application, you need to:

* **Python:** Install Python 3.9 or higher.
* **Gemini API Key:** Get your key from [Google AI Studio](https://aistudio.google.com/app/apikey).
* **Tesseract OCR:** Install the Tesseract engine on your operating system (required for the image/OCR feature).

### 2. Installation

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/student-chatbot-assistt.git](https://github.com/YOUR_USERNAME/student-chatbot-assistt.git)
    cd student-chatbot-assistt
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate     # On Windows
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### 3. API Key Configuration

1.  Create a file named **`.env`** in the root directory of the project.
2.  Add your API key to the file as follows:

    ```ini
    # .env file
    GEMINI_API_KEY="YOUR_ACTUAL_GEMINI_API_KEY_HERE"
    ```

    > **Security Warning:** The `.env` file is listed in `.gitignore` and must **never** be committed to your repository.

## Running the Chatbot

Start the Streamlit application from your terminal:

```bash
streamlit run app.py

The README.md file is the face of your project. It needs to clearly and attractively explain what the project does, its features, and how to set it up and run it.

Here is a comprehensive, structured README.md content for your Student Assist AI Chatbot project.

README.md
Markdown

# Student Assist AI Chatbot: Retrieval-Augmented Study Partner

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-brightgreen.svg)](https://streamlit.io/)

A powerful, multimodal AI chatbot built with **Google Gemini** and **Streamlit** to help students study. This application uses **Retrieval-Augmented Generation (RAG)** to allow students to upload their own study materials (PDFs, notes, images) and ask specific, contextual questions about them.

## ✨ Features

The Student Assist AI Chatbot acts as an expert tutor, capable of handling various academic documents:

* **Multimodal RAG (Retrieval-Augmented Generation):** Upload your own files, and the chatbot will use the content to provide highly contextual and accurate answers.
* **Document Support:** Supports text extraction from **PDF** (`.pdf`), **Word** (`.docx`), and general text files.
* **Image-to-Text (OCR):** Uses **pytesseract** to perform Optical Character Recognition on uploaded images (e.g., photos of handwritten notes, whiteboard snapshots, or scanned book pages).
* **Persistent Chat History:** Maintains conversation context for natural, multi-turn interactions.
* **Supportive Persona:** The AI is instructed to maintain an encouraging, academic, and professional tone.
* **Simple UI:** Built with Streamlit for a clean, user-friendly interface.

## 📁 Project Structure

student-chatbot-assistt/
├── .gitignore         # Ignores secrets (.env) and environment folders
├── README.md          # This file
├── requirements.txt   # List of all Python dependencies
├── https://www.google.com/search?q=LICENSE            # MIT Open Source License
├── .env               # Stores GEMINI_API_KEY (IGNORED by Git)
├── app.py             # Streamlit UI application
└── src/               # Core Python logic modules
├── init.py

├── doc_processor.py   # Handles PDF, DOCX, and Image extraction
└── gemini_service.py  # Handles all Gemini API calls and RAG context injection


## ⚙️ Quick Setup

### 1. Prerequisites

Before running the application, you need to:

* **Python:** Install Python 3.9 or higher.
* **Gemini API Key:** Get your key from [Google AI Studio](https://aistudio.google.com/app/apikey).
* **Tesseract OCR:** Install the Tesseract engine on your operating system (required for the image/OCR feature).

### 2. Installation

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/student-chatbot-assistt.git](https://github.com/YOUR_USERNAME/student-chatbot-assistt.git)
    cd student-chatbot-assistt
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate     # On Windows
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### 3. API Key Configuration

1.  Create a file named **`.env`** in the root directory of the project.
2.  Add your API key to the file as follows:

    ```ini
    # .env file
    GEMINI_API_KEY="YOUR_ACTUAL_GEMINI_API_KEY_HERE"
    ```

    > ⚠️ **Security Warning:** The `.env` file is listed in `.gitignore` and must **never** be committed to your repository.

## Running the Chatbot

Start the Streamlit application from your terminal:

```bash
streamlit run app.py
Your web browser should automatically open to the Streamlit interface (usually at http://localhost:8501).

## Contribution
Contributions are welcome! If you have suggestions for new features, bug fixes, or performance improvements, please feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.







