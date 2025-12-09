# Simple Retrieval-Augmented Generation (RAG) Application

This project is a simple Retrieval-Augmented Generation (RAG) application built using Flask. It allows users to upload documents, integrates with LangSmith for monitoring, and utilizes Gemini for language model functionality.

## Project Structure

```
simple-rag-app
├── app.py            # Main application code
├── requirements.txt  # Project dependencies
├── index.html        # User interface
└── README.md         # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd simple-rag-app
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```
   python app.py
   ```

5. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000`.

## Usage Guidelines

- Use the provided interface to upload documents.
- The application will process the documents and return results based on the RAG methodology.
- Monitor the application performance and logs through LangSmith.

## Additional Information

- Ensure you have the necessary API keys and configurations for LangSmith and Gemini.
- For any issues or contributions, please refer to the project's issue tracker.
