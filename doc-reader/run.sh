#!/bin/bash

echo "🚀 Starting Document Chatbot..."

echo "iniating the server :)"
uvicorn app:app --reload  

# Go to project root (safe even if already there)
cd "$(dirname "$0")"

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Ingest documents
echo "📄 Ingesting documents..."
python3 ingest.py


echo "iniating the server :)"
uvicorn app:app --reload  

# # Start chatbot
# echo "🤖 Starting chatbot..."
# python3 answer.py

