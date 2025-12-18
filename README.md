# Multimodal-AI-Toolkit
Ai-Tools

# 🤖 Multimodal AI Toolkit

A comprehensive suite of AI tools integrating **Google Gemini 1.5 Flash** for multimedia processing and **Ollama (Llama 3.2)** for local NLP tasks. This project demonstrates how to bridge cloud-based vision/audio models with local, private text analysis.

---

## 📂 Project Structure

This repository is organized into three specialized modules:

### 1. Prompt Engineering Lab (`/prompt_lab`)
* **Purpose**: A laboratory for testing and demonstrating various Large Language Model (LLM) prompting techniques.
* **Techniques**: Includes Zero-Shot, One-Shot, Few-Shot, and Chain-of-Thought (CoT) implementations.
* **Core Model**: Optimized for `llama3.2:1b` via Ollama.

### 2. Transcription Engine (`/transcription_engine`)
* **Purpose**: Converts video and audio into structured text data using Gemini 1.5 Flash.
* **Features**: 
    * **Video Audio Extraction**: Automatically extracts audio from `.mp4` files using `MoviePy`.
    * **Speaker Diarization**: Identifies and labels multiple speakers (e.g., Speaker 1, Speaker 2).
    * **Timestamped JSON**: Generates structured output containing start times, end times, and text for every utterance.

### 3. Insight Extractor (`/insight_extractor`)
* **Purpose**: An analysis engine that turns raw transcriptions into actionable data using local LLMs.
* **Capabilities**:
    * **Keyword & Topic Extraction**: Identifies named entities, dates, and broad topics in JSON format.
    * **Brand & Location Tracking**: Specifically isolates company names and physical locations.
    * **Sentiment Analysis**: Classifies the overall tone as Positive, Negative, or Neutral.
    * **Summarization**: Condenses long transcripts into clear, simple paragraphs.

---

## 🛠️ Quick Start

### Prerequisites
1. **Ollama**: Install from [ollama.com](https://ollama.com) and pull the required model:
   ```bash
   ollama run llama3.2:1b
