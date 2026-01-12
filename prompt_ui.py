from dotenv import load_dotenv
import streamlit as st
import os
from groq import Groq

load_dotenv()

# Debug: Check if key is loaded
groq_key = os.getenv("GROQ_API_KEY")
if not groq_key:
    st.error("GROQ_API_KEY not found in environment variables!")
    st.stop()

# Initialize Groq client
client = Groq(api_key=groq_key)

def get_summary(paper, style, length):
    """Call Groq API to get paper summary"""
    prompt = f"""You are an expert research assistant. Summarize the research paper titled "{paper}" according to the following constraints.

Explanation style: {style}
Explanation length: {length}

Requirements:
1. Mathematical details: Include relevant equations and explain concepts simply
2. Analogies: Use clear, real-world analogies to simplify complex ideas
3. If information is missing, state "Insufficient information available"

Ensure the summary is accurate, technically sound, and easy to understand."""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # ✅ Updated model
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=1024
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="Research Tool", layout="centered")
st.header("Research Tool")

paper = st.selectbox(
    "Select Research Paper Name",
    ["Attention Is All You Need", 
     "BERT: Pre-training of Deep Bidirectional Transformers", 
     "GPT-3: Language Models are Few-Shot Learners", 
     "Diffusion Models Beat GANs on Image Synthesis"]
)

style = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length = st.selectbox(
    "Select Explanation Length",
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)

if st.button("Summarize"):
    with st.spinner("Generating summary..."):
        summary = get_summary(paper, style, length)
        st.subheader("Summary")
        st.write(summary)