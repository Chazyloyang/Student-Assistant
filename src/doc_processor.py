import os
import io
import PyPDF2
from docx import Document
from PIL import Image
import pytesseract

# 🛑 THE FIX: SET THE TESSERACT EXECUTABLE PATH 🛑
# Use the path relevant to your environment. For Colab/Jupyter, use:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_pdf(file_path: str) -> str:
    """Extracts text content from a PDF file."""
    text = ""
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() or ""
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return f"ERROR: Could not read PDF file. {e}"


def extract_text_from_docx(file_path: str) -> str:
    """Extracts text content from a DOCX file."""
    text = ""
    try:
        document = Document(file_path)
        for paragraph in document.paragraphs:
            text += paragraph.text + '\n'
        return text
    except Exception as e:
        print(f"Error reading DOCX: {e}")
        return f"ERROR: Could not read DOCX file. {e}"


def extract_text_from_image(file_path: str) -> str:
    """Performs Optical Character Recognition (OCR) on an image file."""
    try:
        # Opening the image using Pillow (PIL)
        img = Image.open(file_path)
        
        # Using pytesseract to extract text
        text = pytesseract.image_to_string(img)
        
        return text
    except pytesseract.TesseractNotFoundError:
        return "ERROR: Tesseract is not installed or not in PATH. OCR is unavailable."
    except Exception as e:
        print(f"Error reading Image for OCR: {e}")
        return f"ERROR: Could not process image. {e}"


def process_uploaded_file(file_path: str) -> str:
    """
    Determines the file type and calls the appropriate extraction function.
    Returns the extracted text or an error message.
    """
    # Getting the file extension
    file_extension = os.path.splitext(file_path)[1].lower()

    if file_extension == '.pdf':
        return extract_text_from_pdf(file_path)
    
    elif file_extension == '.docx':
        return extract_text_from_docx(file_path)

    elif file_extension in ['.jpg', '.jpeg', '.png', '.tiff', '.bmp']:
        # For images, I will use OCR
        return extract_text_from_image(file_path)
    
    else:
        return f"ERROR: Unsupported file type: {file_extension}. Please upload a PDF, DOCX, or common image format."
