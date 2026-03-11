llamaindex-simple-RAG-system# LlamaIndex Simple RAG System

This project demonstrates a **Retrieval Augmented Generation (RAG)** pipeline using **LlamaIndex and Google Gemini**.

It allows users to ask questions from:

* Local documents
* Webpages

## Features

* Load documents from a local directory
* Extract and process webpage content
* Convert text into embeddings
* Store vectors using a vector index
* Query the data using Gemini AI

## Technologies Used

* Python
* LlamaIndex
* Google Gemini API
* Embedding Models
* dotenv

## Installation

Clone the repository:

```
git clone https://github.com/Sriram611/llamaindex-simple-RAG-system.git
cd llamaindex-simple-RAG-system
```

Create a virtual environment:

```
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Create a `.env` file:

```
GOOGLE_API_KEY=your_api_key_here
```

## Running the Project

### Document Question Answering

```
python directoryreader.py
```

### Webpage Question Answering

```
python webreader.py
```

Example query:

```
What is variational autoencoder?
```

## Architecture

```
Webpage / Documents
        ↓
   LlamaIndex
        ↓
   Embeddings
        ↓
 Vector Store Index
        ↓
 Gemini LLM
        ↓
     Answer
```

## Author

AI & Data Science student exploring **LLMs and Retrieval Augmented Generation systems**.
