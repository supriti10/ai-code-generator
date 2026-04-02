import streamlit as st
from llama_api import generate_code
from utils.prompt_templates import code_prompt, explain_prompt, debug_prompt

st.set_page_config(page_title="AI Code Assistant", layout="wide")

# 🎨 Header
st.title("💻 AI Code Generator (LLaMA 3)")
st.markdown("Generate, Explain & Debug code using LLaMA 3 via Groq")

# 🔲 Layout: 2 columns
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📝 Input")

    mode = st.selectbox(
        "Choose Mode",
        ["Generate Code", "Explain Code", "Debug Code"]
    )

    user_input = st.text_area("Enter your input:", height=250)

    run_btn = st.button("🚀 Run")

with col2:
    st.subheader("💡 Output")

    if run_btn:
        if user_input.strip() == "":
            st.warning("Please enter something")
        else:
            if mode == "Generate Code":
                prompt = code_prompt(user_input)
            elif mode == "Explain Code":
                prompt = explain_prompt(user_input)
            else:
                prompt = debug_prompt(user_input)

            with st.spinner("Processing..."):
                output = generate_code(prompt)

            st.markdown(output)

            # 📥 Download button
            st.download_button(
                label="📥 Download Code",
                data=output,
                file_name="generated_code.txt",
                mime="text/plain"
            )
