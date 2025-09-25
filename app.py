# app.py (Full Beautiful Gemini Chat Landing Page)
import streamlit as st
from google import genai
import os

# =============================
# Page Config
# =============================
st.set_page_config(
    page_title="Gemini AI Chat",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================
# Custom CSS & Animations
# =============================
st.markdown(
    """
    <style>
    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(10px);}
        to {opacity: 1; transform: translateY(0);}
    }
    * {font-family: 'Segoe UI', sans-serif;}

    .main-title {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 0.5rem;
        background: linear-gradient(90deg, #06beb6, #48b1bf);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: fadeIn 1s ease-in-out;
    }

    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #555;
        margin-bottom: 2rem;
        animation: fadeIn 1.5s ease-in-out;
    }

    .stButton button {
        background: linear-gradient(90deg, #667eea, #764ba2);
        color: white;
        border-radius: 10px;
        padding: 0.6rem 1.2rem;
        font-size: 1.1rem;
        font-weight: bold;
        transition: 0.3s;
        border: none;
    }
    .stButton button:hover {
        background: linear-gradient(90deg, #764ba2, #667eea);
        transform: scale(1.05);
    }

    textarea {
        border-radius: 12px !important;
        border: 2px solid #667eea !important;
    }

    .response-box {
        background: #f9f9f9;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 6px solid #667eea;
        animation: fadeIn 1s ease-in-out;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =============================
# Sidebar
# =============================
st.sidebar.header("⚙️ Settings")
st.sidebar.write("Enter your Google Gemini API key below:")
api_key_input = st.sidebar.text_input(
    "Google API Key", type="password", placeholder="Paste your API key here"
)

theme_choice = st.sidebar.selectbox("Theme", ["🌞 Light", "🌙 Dark"], index=0)

# =============================
# Gemini Client Setup
# =============================
client = None
if api_key_input:
    try:
        client = genai.Client(api_key=api_key_input.strip())
    except Exception as e:
        st.sidebar.error(f"Error initializing Gemini client: {e}")
else:
    st.sidebar.warning("⚠️ No API key provided. Enter one above.")

# =============================
# Main UI
# =============================
st.markdown("<h1 class='main-title'>🤖 Gemini AI Chat</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Experience the power of Google Gemini with a smooth Streamlit UI ✨</p>", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])
with col1:
    prompt = st.text_area("💡 Enter your prompt:", placeholder="Explain quantum computing in simple terms...", height=120)
with col2:
    model_name = st.selectbox("🧠 Choose Gemini model:", ["gemini-2.5-flash", "gemini-2.0-pro-exp-02-05", "gemini-1.5-pro"])

if st.button("🚀 Generate Response"):
    if client is None:
        st.error("❌ Gemini client not initialized. Please provide a valid API key in the sidebar.")
    elif not prompt.strip():
        st.warning("⚠️ Please write a prompt before generating a response.")
    else:
        with st.spinner("✨ Generating response..."):
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt,
                )
                st.markdown("### ✅ Gemini Response:")
                st.markdown(f"<div class='response-box'>{response.text}</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"❌ Error from Gemini API: {e}")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:gray;'>Made with ❤️ using Streamlit & Gemini</p>",
    unsafe_allow_html=True
)
