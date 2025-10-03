# 📰 Text Summarizer 

This is a Streamlit web app that generates a concise 3-sentence summary of any news article, blog post, or long text.
It uses Hugging Face Transformers with the facebook/bart-large-cnn model for text summarization.
---
# 🚀 Features
- Paste any text (news, blogs, articles).
- Get an AI-generated summary in 3 sentences.
- Runs on CPU (no GPU required).
- Simple and interactive Streamlit UI.
---
# 🛠️ Installation
1. Install Python
    ```bash
   pip install python
   ``` 
2. Create a virtual environment (recommended):
    ```bash
    python -m venv venv
    venv\Scripts\activate 
   ```
3. Install the required dependencies:
   ```bash
    pip install -r requirements.txt
   ```
4. Run chatbot
   ```bash
    streamlit run app.py  
   ```  
---
## 📦 Requirements
- streamlit 
- transformers
- torch
---
# 💻 Example
   ## Enter the text:
   ```
Climate change is one of the most pressing challenges of our time. Rising global temperatures have led to melting glaciers, rising sea levels, and unpredictable weather patterns across the world. Scientists warn that if greenhouse gas emissions are not reduced, the planet could face severe consequences including food shortages, water scarcity, and mass displacement of people. Governments and organizations are working to adopt renewable energy, improve sustainability, and create international agreements to combat the crisis. However, significant efforts from individuals are also needed, such as reducing waste, conserving energy, and supporting eco-friendly initiatives. The combined action of communities, industries, and policymakers will determine how effectively humanity can tackle this global issue.
```
   ## Output:
   ```
Rising global temperatures have led to melting glaciers, rising sea levels, and unpredictable weather patterns across the world Scientists warn that if greenhouse gas emissions are not reduced, the planet could   face severe consequences including food shortages, water scarcity, and mass displacement of people.
```
---
#📌 Notes
- The summarizer is cached for faster performance using @st.cache_resource.
- The model runs on CPU.
- The app ensures the summary is limited to 3 sentences.
