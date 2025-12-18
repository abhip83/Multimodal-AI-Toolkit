# Automated Text Insights Engine

This script processes raw transcriptions to extract structured intelligence using **Ollama**. It is designed to be a "plug-and-play" module for any text analysis pipeline.

## 📊 Extraction Capabilities
* **Keyword & Topic Extraction**: Identifies named entities, dates, and broad topics in JSON format.
* **Brand & Location Tracking**: Specifically isolates company names and physical locations.
* **Sentiment Analysis**: Classifies the overall tone of the text as Positive, Negative, or Neutral.
* **Summarization**: Condenses long transcriptions into clear, simple paragraphs.

## 🛠️ Configuration
* **Model**: Defaults to `llama3.2:1b`.
* **Output**: All functions return cleaned JSON or string data, stripped of junk characters.

## 🚀 Example
```python
from llm import extract_keywords
data = extract_keywords("Your transcription text here", "llama3.2:1b")
print(data["keywords"])
