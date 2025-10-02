import streamlit as st
import os
import tempfile
from dotenv import load_dotenv

# Import the core logic from the src directory
from src.gemini_service import GeminiService
from src.doc_processor import process_uploaded_file

# Load environment variables from .env (including GEMINI_API_KEY)
load_dotenv()

# --- 1. CONFIGURATION AND STYLING ---

st.set_page_config(
    page_title="Student Assist AI Chatbot",
    layout="wide"
)

# Define the custom CSS for the purple/white theme and UI adjustments
CUSTOM_CSS = """
<style>
/* Main Background and Text */
.stApp {
    background-color: #F8F8FF; /* Ghost White - very light, clean background */
}
/* Header and Title (Dark Purple) */
h1 {
    color: #4B0082; /* Indigo - deep, academic purple */
    text-align: center;
    font-weight: 700;
}
/* Sidebar background */
[data-testid="stSidebar"] {
    background-color: #E6E6FA; /* Lavender - light purple sidebar */
    border-right: 2px solid #9370DB; /* Medium Purple border */
}

/* User chat messages */
[data-testid="stChatMessage"][data-testid="stChatMessage"] div.stMarkdown > div {
    background-color: #FFFFFF; /* White background for user input */
    border-left: 5px solid #6A5ACD; /* Slate Blue marker */
    border-radius: 10px;
}

/* AI chat messages */
[data-testid="stChatMessage"][data-testid="stChatMessage"]:nth-child(even) div.stMarkdown > div {
    background-color: #F0F8FF; /* Alice Blue for AI */
    border-left: 5px solid #4B0082; /* Indigo marker */
    border-radius: 10px;
}

/* General button styling */
.stButton>button {
    background-color: #9370DB; /* Medium Purple */
    color: white;
    font-weight: bold;
    border-radius: 8px;
    padding: 10px 15px;
    transition: background-color 0.3s;
}
.stButton>button:hover {
    background-color: #6A5ACD; /* Slate Blue on hover */
    color: white;
}

/* --- FILE UPLOADER ICON & CUSTOMIZATION --- */

/* Hide the default Streamlit label and box text of the file uploader */
[data-testid="stFileUploader"] label {
    display: none;
}
[data-testid="stFileUploaderDropzone"] p {
    display: none;
}
[data-testid="stFileUploaderDropzone"] {
    /* Hide the entire drop zone */
    border: none !important;
    background-color: transparent !important;
}

/* Make the file uploader container itself very small to look like an icon */
#file_upload_trigger {
    height: 38px; /* Match typical input height */
    width: 38px;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 0;
    margin-top: 5px; /* Adjust alignment with chat input */
}

/* Style the file uploader label (which we repurpose as the icon) */
[data-testid="stFileUploaderDropzone"] label {
    display: flex !important; /* Make label visible again */
    justify-content: center;
    align-items: center;
    width: 38px;
    height: 38px;
    cursor: pointer;
    border-radius: 50%;
    background-color: #E6E6FA; /* Light purple circle */
    font-size: 20px; /* Icon size */
    color: #4B0082; /* Dark purple icon color */
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    transition: background-color 0.2s;
    overflow: hidden; /* Hide the default button text */
}

[data-testid="stFileUploaderDropzone"] label:hover {
    background-color: #9370DB; /* Medium Purple on hover */
    color: white;
}

/* When the file uploader is clicked, we want to show the 'Browse files' text */
/* This is tricky in pure CSS without JS, but the native browser prompt handles it visually */

</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


# --- 2. SESSION STATE & INITIALIZATION (No Change) ---

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize document context variables
if "uploaded_context" not in st.session_state:
    st.session_state.uploaded_context = None

if "file_name" not in st.session_state:
    st.session_state.file_name = None

@st.cache_resource(show_spinner="Initializing AI Model...")
def initialize_service():
    """Initializes the GeminiService, handling API key errors."""
    try:
        service = GeminiService()
        return service
    except ValueError as e:
        st.error(f"Configuration Error: {e}. Please ensure your GEMINI_API_KEY is set in the .env file.")
        return None

# Initialize the Gemini service once
gemini_service = initialize_service()

if gemini_service:
    st.session_state.gemini_service = gemini_service
else:
    st.stop()


# --- 3. SIDEBAR (Chat Management Only)---

with st.sidebar:
    st.header("Chat Management")
    st.markdown("Use this to clear the current conversation history.")

    if st.button("Start New Chat", key="clear_chat"):
        st.session_state.messages = []
        st.session_state.uploaded_context = None
        st.session_state.file_name = None
        st.rerun()


# --- 4. RAG DOCUMENT PROCESSING FUNCTION (No Change) ---

def handle_file_upload(uploaded_file):
    """Processes the uploaded file and updates session state."""
    
    if uploaded_file and uploaded_file.name != st.session_state.file_name:
        st.session_state.file_name = uploaded_file.name
        
        # Use a temporary file to save the uploaded content
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_file_path = tmp_file.name

        with st.spinner(f"Processing '{uploaded_file.name}'..."):
            extracted_text = process_uploaded_file(tmp_file_path)
        
        # Clean up the temporary file
        os.unlink(tmp_file_path)

        if extracted_text.startswith("ERROR"):
            st.error(f"Document processing failed: {extracted_text}")
            st.session_state.uploaded_context = None
            st.session_state.file_name = None
        else:
            st.session_state.uploaded_context = extracted_text
            st.success(f"Successfully loaded context from: **{uploaded_file.name}**")
            
            char_count = len(extracted_text)
            st.caption(f"Context loaded (Approx. {char_count:,} characters).")
            st.rerun() # Rerun to show success message and context status
            
    elif uploaded_file and uploaded_file.name == st.session_state.file_name:
        st.info(f"Context from **{uploaded_file.name}** is already loaded.")


# --- 5. MAIN APPLICATION INTERFACE ---

st.title("Student Assist AI Chatbot")

# Context Status Display
if st.session_state.uploaded_context:
    st.info(f"**File Successfully Uploaded**.")



# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# --- 6. CUSTOM CHAT INPUT AND FILE UPLOAD ---

input_container = st.container()

with input_container:
    # Use columns for layout: [Icon (small), Input (large)]
    col1, col2 = st.columns([1, 10])

    # Column 1: File Uploader Icon
    with col1:
        uploaded_file = st.file_uploader(
            label="📄", 
            type=['pdf', 'docx', 'jpg', 'jpeg', 'png', 'tiff', 'bmp'],
            accept_multiple_files=False,
            label_visibility="visible", 
            key="file_upload_trigger"
        )
        
        if uploaded_file:
            # Handle file upload immediately
            handle_file_upload(uploaded_file)
            
    # Column 2: Chat Input - THIS IS THE CRUCIAL PART
    # By placing st.chat_input here, it is processed on every rerun
    # before the response generation logic below, ensuring it stays visible.
    with col2:
        prompt = st.chat_input("Ask your question here...", key="user_input_prompt")


# --- 7. RESPONSE GENERATION ---

if prompt:
    # 1. Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message in chat container
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response_text = st.session_state.gemini_service.generate_response(
                user_query=prompt,
                document_context=st.session_state.uploaded_context
            )
            st.markdown(response_text)

    # 3. Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response_text})
    st.rerun()
