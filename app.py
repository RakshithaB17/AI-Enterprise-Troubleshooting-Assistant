import streamlit as st
from prompts import troubleshooting_prompt
from ai_service import analyze_issue

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Enterprise API Troubleshooting Assistant",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.title("🤖 AI Support Assistant")

    st.markdown("---")

    st.markdown("### About")

    st.write(
        """
This AI assistant helps Technical Support Engineers analyze REST API issues using Google's Gemini LLM.

Features:

✅ Root Cause Analysis

✅ API Troubleshooting

✅ Best Practices

✅ Customer-Friendly Response
"""
    )

    st.markdown("---")

    st.info(
        "Built using Python, Streamlit and Google Gemini."
    )

# -----------------------------
# Main Title
# -----------------------------
st.title("🤖 Enterprise API Troubleshooting Assistant")

st.caption(
    "AI-powered troubleshooting for REST API integrations."
)

st.markdown("---")

# -----------------------------
# Input Form
# -----------------------------
st.subheader("📝 Enter API Details")

col1, col2 = st.columns(2)

with col1:

    endpoint = st.text_input(
        "🌐 API Endpoint",
        placeholder="POST /payment"
    )

with col2:

    status_code = st.text_input(
        "📡 HTTP Status Code",
        placeholder="401"
    )

request_body = st.text_area(
    "📤 Request Payload",
    height=180,
    placeholder='{\n    "amount":100\n}'
)

response_body = st.text_area(
    "📥 Response Payload",
    height=180,
    placeholder='{\n    "message":"Invalid API Key"\n}'
)

logs = st.text_area(
    "📄 Application Logs",
    height=180,
    placeholder="Paste application logs..."
)

st.markdown("")

analyze = st.button(
    "🔍 Analyze Issue",
    use_container_width=True,
    key="analyze_button"
)

st.markdown("---")

# Analyze Button
if analyze:

    # Basic Validation
    if not endpoint or not status_code:
        st.warning("Please provide at least the API Endpoint and HTTP Status Code.")
        st.stop()

    # Generate Prompt
    prompt = troubleshooting_prompt(
        endpoint,
        status_code,
        request_body,
        response_body,
        logs
    )

    # Call Gemini
    with st.spinner("🤖 AI is analyzing the issue..."):

        answer = analyze_issue(prompt)

    # Display Result
    st.divider()

    st.subheader("📋 Analysis Report")

    st.markdown(answer)