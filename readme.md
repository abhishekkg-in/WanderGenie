# 🌍 WanderGenie - Your AI-Powered Travel Companion  

Welcome to **WanderGenie**, an intelligent travel recommendation system designed for **Holiday Tribe**.  
This project leverages cutting-edge technologies like **LLMs**, **RAG**, and **Embeddings** to provide personalized travel recommendations.  

---

## 🚀 Features  

- 🗺️ **Comprehensive Travel Database**: Includes descriptions, details, and metadata for various destinations.  
- 🧠 **AI-Powered Recommendations**: Uses LLMs to generate personalized travel suggestions.  
- 🔍 **Efficient Similarity Search**: Implements FAISS for quick and accurate document retrieval.  
- 💬 **Fallback Support**: Handles queries for destinations not present in the database.  

---

## 📂 Project Structure  

```plaintext
📦 WanderGenie  
├── 📁 data               # SQL scripts and sample data  
├── 📁 embeddings         # Code for generating embeddings  
├── 📁 retrieval          # FAISS-based similarity search  
├── 📁 response_generator # LLM-based response generation  
├── 📄 requirements.txt   # Project dependencies  
└── 📄 app.py             # Main application  
