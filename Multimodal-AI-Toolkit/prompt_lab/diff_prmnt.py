# pip install ollama
# https://www.promptingguide.ai/
import ollama

# Change this to your model name if different
MODEL_NAME = "llama3.2:1b"

# 1. Zero-Shot Prompting
def zero_shot_prompt(input_text):
    prompt = f"Summarize the following text:\n{input_text}"
    response = ollama.chat(model=MODEL_NAME, messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

# 2. One-Shot Prompting
def one_shot_prompt(input_text):
    prompt = (
        "Text: The Great Wall of China is one of the Seven Wonders of the World.\n"
        "Summary: The Great Wall of China is a famous Wonder of the World.\n\n"
        f"Text: {input_text}\nSummary:"
    )
    response = ollama.chat(model=MODEL_NAME, messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

# 3. Few-Shot Prompting
def few_shot_prompt(input_text):
    prompt = (
        "Text: The Taj Mahal is a white marble mausoleum in India.\n"
        "Summary: The Taj Mahal is a white marble tomb located in India.\n\n"
        "Text: Mount Everest is the highest mountain above sea level.\n"
        "Summary: Mount Everest is the tallest mountain on Earth.\n\n"
        "Text: The Great Barrier Reef is the largest coral reef system.\n"
        "Summary: The Great Barrier Reef is the world's largest coral reef system.\n\n"
        f"Text: {input_text}\nSummary:"
    )
    response = ollama.chat(model=MODEL_NAME, messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

# 4. Chain-of-Thought Prompting
def chain_of_thought_prompt(input_text):
    prompt = (
        f"Let's think step by step to summarize the following text:\n\n"
        f"Text: {input_text}\n\n"
        "Step 1: Identify the main subject of the sentence.\n"
        "Step 2: Understand what is being said about the subject.\n"
        "Step 3: Combine the subject and key information into one concise sentence.\n"
        "Final Summary:"
    )
    response = ollama.chat(model=MODEL_NAME, messages=[{"role": "user", "content": prompt}])
    return response['message']['content']


# --- Example Usage ---
if __name__ == "__main__":
    input_text = """Prompt engineering is a relatively new discipline for developing and optimizing prompts to 
    efficiently use language models (LMs) for a wide variety of applications and research topics. 
    Prompt engineering skills help to better understand the capabilities and limitations of large language 
    models (LLMs).
    Researchers use prompt engineering to improve the capacity of LLMs on a wide range of common and complex 
    tasks such as question answering and arithmetic reasoning. Developers use prompt engineering to design robust
      and effective prompting techniques that interface with LLMs and other tools.
    Prompt engineering is not just about designing and developing prompts. 
    It encompasses a wide range of skills and techniques that are useful for interacting and developing with LLMs.
     It's an important skill to interface, build with, and understand capabilities of LLMs. 
     You can use prompt engineering to improve safety of LLMs and build new capabilities like augmenting LLMs 
     with domain knowledge and external tools.
"""

    print("=== Zero-Shot ===")
    print(zero_shot_prompt(input_text), "\n")

    print("=== One-Shot ===")
    print(one_shot_prompt(input_text), "\n")

    print("=== Few-Shot ===")
    print(few_shot_prompt(input_text), "\n")

    print("=== Chain of Thought ===")
    print(chain_of_thought_prompt(input_text), "\n")
