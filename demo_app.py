import streamlit as st
import pandas as pd
import time

st.set_page_config(layout="wide")

# Function to process the analysis
def analyze_audio(df, audio_name, progress_container):
    # Simulate analysis (replace with actual analysis logic)
    
    for i in range(13):
        time.sleep(1)
        progress_container.progress((i + 1) / 13)

    # Fetch transcript and insights from the dataframe
    row = df[df['audio_name'] == audio_name].iloc[0]
    transcript = row['transcription']
    insights = row['insights']

    return transcript, insights

# Main Streamlit app
def main():
    st.title("Audio Analysis App")

    # Load dataframe from Excel file (replace with your actual file path)
    # excel_path = "demo_openai_output.xlsx"
    excel_path = "demo_openai_output_masked.xlsx"
    df = pd.read_excel(excel_path)


    # Create dropdown for audio names
    selected_audio = st.selectbox("Select Audio File", df['audio_name'])

    # Load audio and display player
    audio_path = "demo_audios/" + selected_audio  # Replace with actual path
    
    st.audio(audio_path, format='audio/mp3', start_time=0)

    # Analyze button
    if st.button("Analyze"):
        with st.spinner("Analyzing..."):
            progress_container = st.empty()
            transcript, insights = analyze_audio(df, selected_audio, progress_container)

        # Display transcript and insights side by side
        col1, col2 = st.columns(2)
        col1.subheader("Transcript")
        # col1.text(transcript)
        # col1.text_area(" ", transcript)
        col1.markdown(f"```{transcript}```", unsafe_allow_html=True)

        col2.subheader("Insights")
        col2.text(insights)


if __name__ == "__main__":
    main()
