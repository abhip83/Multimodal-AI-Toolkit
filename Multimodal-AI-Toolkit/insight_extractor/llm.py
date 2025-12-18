import ollama
import json
llm_model = 'llama3.2:1b'
def run_ollama_prompt(prompt, llm_model):
    response = ollama.generate(llm_model, prompt)
    response_text = response['response']
    return response_text

def extract_keywords(transcription, llm_model):
    print("=" * 100)
    print("Extracting keywords and topics...")

    extract_kwrds_prompt = f"""
    From the following text, extract and return the following two categories of information:
        1. keywords: Keywords, Named Entities, names of people, dates, events, products, objects, tools or physical items or important keyword.
        2. topics: extract the main topics in transcription. Ensure that the topics are broad.

        Do not give any explanations or additional information. Only return the results in the following JSON format:
        Also kindly note, give cleaned values, there should not be \ or junk chars inside it. 
        Return the JSON in a compact format without any extra spaces or newlines.

        {{
            "keywords": ["keyword1", "keyword2", ...],
            "topics": ["automobile", "IT", "AI",...]
        }}

        Text: {transcription}
    """
        
    keywords_topics_res = run_ollama_prompt(extract_kwrds_prompt, llm_model)
    keywords_topics_res = keywords_topics_res.replace("\n", "").replace(" ", "")
    print("Extracted keywords and topics:", keywords_topics_res)

    try:
        keywords_topics_dict = json.loads(keywords_topics_res)
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        keywords_topics_dict = {"keywords": [], "topics": []}

    return keywords_topics_dict

def extract_brands_and_locations(transcription, llm_model):
    print("=" * 100)
    print("Extracting brands and locations...")

    extract_brands_locations_prompt = f"""
        From the following text, extract and return the following two categories of information:
        1. Brands: Names of companies, manufacturers, or organizations (e.g., NVIDIA, Microsoft, Google, Toyota).
        2. Locations: Physical or functional places (e.g., factory, datacenter, workstation).

        Do not give any explanations or additional information. Only return the results in the following JSON format:
        Also kindly note, give cleaned values, there should not be \ or junk chars inside it. 
        Return the JSON in a compact format without any extra spaces or newlines.

        {{
            "brands": ["brand1", "brand2", ...],
            "locations": ["location1", "location2", ...]
        }}

        Text: {transcription}
        """

    brands_locations_res = run_ollama_prompt(extract_brands_locations_prompt, llm_model)

    # Preprocess the response to remove unwanted characters
    brands_locations_res = brands_locations_res.replace("\n", "").replace(" ", "")

    print("Extracted brands and locations:", brands_locations_res)

    # Convert the response string to a dictionary
    try:
        brands_locations_dict = json.loads(brands_locations_res)
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        brands_locations_dict = {"brands": [], "locations": []}

    return brands_locations_dict


def summarize_transcription(transcription, llm_model):
    print("=" * 100)
    print("Summarizing transcription...")
    summarization_prompt = f"""
    Summarize the following text in a short and clear manner as simple paragraph. Return only the summarized text 
    without any explanations or additional information, Nothing else.: {transcription}
    
    summary:"""
    summarized_transcription = run_ollama_prompt(summarization_prompt, llm_model)
    print("Summarized Text:", summarized_transcription)
    return summarized_transcription


def find_sentiments(transcription, llm_model):
    print("=" * 100)
    print("Finding sentiments...")
    sentiment_prompt = f"Please analyze the sentiment (positive, negative, neutral) of the following text:\n{transcription}. Also note we need single word answer either positive or negative or neutral. Important is do not give any explaination\n\nSentiment:"
    sentiment = run_ollama_prompt(sentiment_prompt, llm_model)
    print("Sentiment:", sentiment)
    return sentiment

transcription = """In the following visualization, each pulse for the encoder or
    decoder is that RNN processing its inputs and generating an output for that time step.
    Since the encoder and decoder are both RNNs, each time step one of the RNNs does some processing,
    it updates its hidden state based on its inputs and previous inputs it has seen.
    Let’s look at the hidden states for the encoder. Notice how the last hidden state is 
    actually the context we pass along to the decoder."""
key = extract_keywords(transcription,llm_model)