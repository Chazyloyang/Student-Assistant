import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables from the .env file
load_dotenv()

class GeminiService:
    """
    Handles all interactions with the Google Gemini API, including 
    initialization, system instruction setting, and chat management.
    """
    
    # FIX APPLIED HERE: Changed default model to the current, correct name
    def __init__(self, model_name: str = 'gemini-2.5-flash'):
        """
        Initializes the Gemini client and starts a chat session.
        
        Args:
            model_name: The Gemini model to use. Defaults to 'gemini-2.5-flash' 
                        for speed and capability in chat/RAG applications.
        """
        # 1. API Client Configuration
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found. Please set it in your .env file.")

        self.client = genai.Client(api_key=api_key)
        
        # 2. System Instruction for the Student Assist Chatbot
        system_instruction = (
            "You are the Student Assist AI, an expert, encouraging, and highly helpful study partner. "
            "Your main goal is to assist students with their documents and queries. "
            "If the user provides context from a file, prioritize that information to answer their questions (this is called RAG). "
            "If the question is general, use your general knowledge. "
            "Always maintain a professional, academic, and supportive tone."
        )

        # 3. Model Configuration and Chat Initialization
        config = types.GenerateContentConfig(
            system_instruction=system_instruction
        )
        
        # Start a chat session, which automatically manages conversation history
        # Ensure 'model_name' here is a valid, available model. 'gemini-2.5-flash' is correct.
        self.chat = self.client.chats.create(
            model=model_name,
            config=config,
        )

    def generate_response(self, user_query: str, document_context: str = None) -> str:
        """
        Sends the user query and optional document context to the Gemini model.

        Args:
            user_query: The question or message from the user.
            document_context: Extracted text from an uploaded file (optional).

        Returns:
            The model's generated text response.
        """
        # Construct the full prompt for the model
        if document_context:
            # RAG Prompt Template: Inject the document context 
            full_prompt = (
                f"DOCUMENT CONTEXT (use this to answer the user's question): \n---\n"
                f"{document_context}\n---\n\n"
                f"USER QUESTION (answer based ONLY on the context if possible, otherwise use general knowledge): {user_query}"
            )
        else:
            # Standard Chat Prompt
            full_prompt = user_query
            
        try:
            # Send the message to the chat session (maintaining history)
            response = self.chat.send_message(full_prompt)
            return response.text
        except Exception as e:
            # Return the error message clearly to the user
            return f"An error occurred while calling the Gemini API: {e}"

# Example Usage (for testing only, remove before deploying Streamlit app)
if __name__ == '__main__':
    try:
        # NOTE: Make sure you have a .env file with GEMINI_API_KEY="YOUR_API_KEY"
        service = GeminiService()
        
        # 1. Chat without context
        print("--- General Chat Test ---")
        general_response = service.generate_response("What is the Pythagorean theorem?")
        print(f"AI: {general_response}\n")

        # 2. RAG test with simulated document context
        print("--- RAG Test with Context ---")
        context_text = "The Udacity AWS AI & ML Scholarship covers three courses: AI Programming with Python, AWS Machine Learning Fundamentals, and Introducing Generative AI with AWS."
        rag_response = service.generate_response(
            user_query="How many courses are covered in the Udacity scholarship?", 
            document_context=context_text
        )
        print(f"AI: {rag_response}")

    except ValueError as e:
        print(f"Setup Error: {e}")
