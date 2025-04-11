import gradio as gr
from transformers import pipeline

# Load sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]
    return f"Sentiment: {result['label']} (Confidence: {result['score']:.2f})"

# Create Gradio interface
iface = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.Textbox(placeholder="Enter text here..."),
    outputs=gr.Textbox(),
    title="Sentiment Analysis",
    Description: Enter a sentence to determine its sentiment, whether it is positive or negative.
)

# Launch the app
iface.launch(inline = False)