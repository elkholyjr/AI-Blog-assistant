import streamlit as st
from google import genai
from google.genai import types
from apikey import google_gemini_api_key  

def generate(blog_title, blog_keywords, number_words):
    client = genai.Client(
        api_key = google_gemini_api_key,
    )

    model = "gemini-2.5-pro"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=f"""Generate a comprehensive, engaging blog post relevant to the given title \"{blog_title}\" and keywords \"{blog_keywords}\". Make sure to incorporate these keywords in the blog post. The blog should be approximately {number_words} words in length, suitable for an online audience. Ensure the content is original, informative, and maintains a consistent tone throughout."""),
            ],
        )
    ]

    tools = [
        types.Tool(googleSearch=types.GoogleSearch())
    ]

    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=-1),
        tools=tools,
    )

    response_text = ""
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        response_text += chunk.text

    return response_text


st.set_page_config(layout="wide")

st.title("AI Blog Assistant")

st.subheader("Generate blog posts with AI")

with st.sidebar:
    st.header("Enter your blog details")
    st.subheader("Enter details")
    blog_title = st.text_input("Enter the blog title:")
    blog_keywords = st.text_area("Keywords (comma-separated):")
    number_words = st.slider("Number of words:", min_value=100, max_value=3000, value=100)
    num_images = st.number_input("Number of images:", min_value=1, max_value=10, step=1)
    submit_button = st.button("Generate Blog Post")

if submit_button:
    if not blog_title or not blog_keywords:
        st.error("Please enter both the blog title and keywords.")
    else:
        # Call your generate function
        response_text = generate(blog_title, blog_keywords, number_words)

        # Show output
        st.write("### Blog Post Generated Successfully!")
        st.write(f"**Title**: {blog_title}")
        st.markdown("---")
        st.title("Generated Blog Post")
        st.markdown(response_text) 
