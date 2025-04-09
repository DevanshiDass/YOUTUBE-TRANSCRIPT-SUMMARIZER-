import re
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
import torch

st.set_page_config(page_title="🎥 YouTube Transcript Summarizer", layout="wide")

# Show Torch info for debug
st.sidebar.title("🔧 Debug Info")
st.sidebar.write(f"**Torch Version:** {torch.__version__}")

@st.cache_resource(show_spinner=False)
def load_summarizer():
    try:
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=-1)
        return summarizer
    except Exception as e:
        st.error(f"❌ Error loading summarizer model: {e}")
        return None

summarizer = load_summarizer()

def extract_video_id(url):
    regex = r'(?:v=|\/)([0-9A-Za-z_-]{11}).*'
    match = re.search(regex, url)
    if match:
        return match.group(1)
    return None

def get_transcript_text(video_id):
    try:
        # Try manual or auto-generated English transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        return "\n".join([entry['text'] for entry in transcript])
    except Exception as e:
        return f"❌ Error fetching transcript: {e}"

def summarize_text(text, length="short"):
    if not summarizer:
        return "Summarizer not available."
    
    chunks = [text[i:i+1024] for i in range(0, min(len(text), 5000), 1024)]
    summaries = []

    for chunk in chunks:
        try:
            summary = summarizer(chunk, max_length=150 if length == "detailed" else 60,
                                 min_length=50 if length == "detailed" else 30, do_sample=False)[0]['summary_text']
            summaries.append(summary)
        except Exception as e:
            return f"❌ Error summarizing: {e}"
        
        if length == "short" and len(summaries) >= 2:
            break

    return "\n\n".join(summaries)

# UI Layout
st.title("🎓 YouTube Transcript Summarizer")

video_url = st.text_input("📥 Enter a YouTube Video URL")

if video_url:
    video_id = extract_video_id(video_url)

    if not video_id:
        st.error("❌ Invalid YouTube link. Please check and try again.")
    else:
        with st.spinner("📄 Extracting transcript..."):
            transcript = get_transcript_text(video_id)

        if transcript.startswith("❌"):
            st.error(transcript)
        else:
            st.success("✅ Transcript fetched successfully!")

            summary_type = st.radio("📌 Choose summary length:", ["Short", "Detailed"])

            if st.button("📝 Generate Summary"):
                with st.spinner("✍️ Summarizing..."):
                    summary = summarize_text(transcript, length="detailed" if summary_type == "Detailed" else "short")
                st.subheader("🧾 Summary")
                st.write(summary)
                with st.expander("📜 Full Transcript"):
                    st.write(transcript)

st.markdown("---")
st.markdown("Made with ❤️ by Devanshi | [📧 Email](mailto:dasdevanshi7@gmail.com)")

