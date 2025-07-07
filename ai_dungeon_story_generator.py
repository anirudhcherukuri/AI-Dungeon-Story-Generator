# ai_dungeon_story_generator.py

import streamlit as st
from transformers import pipeline

# -----------------------------
#  AI Dungeon Story Generator – Final Optimised Version
# -----------------------------

# 🔷 Phase 1: Setup
st.set_page_config(page_title="AI Dungeon Story Generator", page_icon="", layout="wide")

# Title
st.title(" AI Dungeon Story Generator")
st.write("Generate fantasy stories with the power of AI. Enter a prompt to continue the adventure!")

# 🔷 Phase 2: Load model with caching
@st.cache_resource()
def load_model():
    # For development/testing use distilgpt2 (fast, light)
    # For better outputs, uncomment gpt2-medium if RAM allows
    generator = pipeline("text-generation", model="distilgpt2")
    # generator = pipeline("text-generation", model="gpt2-medium")
    return generator

generator = load_model()

# 🔷 Phase 3: User input
prompt = st.text_area(" Enter your story prompt here:", height=120)

# 🔷 Phase 4: Generate and display output
if st.button(" Generate Story"):
    if prompt:
        with st.spinner("Generating your adventure..."):
            story = generator(
                prompt,
                max_length=200,   # Increase length for richer stories
                do_sample=True,
                top_k=50,
                top_p=0.95,
                temperature=1.0   # Increase temperature for creativity
            )[0]['generated_text']

        # Display generated story with enhanced styling
        st.markdown("###  **Generated Story**")
        st.markdown(
            f"""
            <div style='background-color:#f8f9fa; padding:15px; border-radius:10px; color:#222222; font-size:16px;'>
                {story}
            </div>
            """,
            unsafe_allow_html=True
        )

# 🔷 Phase 5: Footer
st.markdown("""
---
 *Built using [Hugging Face Transformers](https://huggingface.co/transformers/) and Streamlit.*
""")
