import os

import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt
from langchain_openai import ChatOpenAI

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    st.warning("Missing OPENAI_API_KEY. Add it to your .env file or environment variables and restart the app.")
    st.stop()

model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7, max_tokens=200)

st.header("Researcher Tool")

with st.form("research_form"):
    paper_input = st.selectbox(
        "Select Research Paper Name",
        [
            "Attention Is All You Need",
            "BERT: Pre-training of Deep Bidirectional Transformers",
            "GPT-3: Language Models are Few-Shot Learners",
            "Diffusion Models Beat GANs on Image Synthesis",
        ],
    )

    style_input = st.selectbox(
        "Select Explanation Style",
        ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"],
    )

    length_input = st.selectbox(
        "Select Explanation Length",
        ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"],
    )

template = load_prompt("template.json")

# fill the placeholder

if st.button("Summarize"):
        chain = template | model
        result = chain.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input
        })
        st.write(result.content)
