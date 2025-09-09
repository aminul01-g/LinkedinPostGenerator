import streamlit as st
import requests
from typing import Dict, Optional

def setup_page():
    """
    Configure the Streamlit page with a title and description.
    This makes our app look professional!
    """
    st.set_page_config(
        page_title="LinkedIn Post Generator",
        page_icon="✍️",
        layout="centered"
    )
    st.title("✨ LinkedIn Post Generator")
    st.write("Turn your ideas into professional LinkedIn posts!")

def get_user_input() -> str:
    """
    Get the user's post idea through a text area.
    Returns:
        str: The user's input text
    """
    return st.text_area(
        "What would you like to post about?",
        placeholder="Example: Share my experience learning Python and AI",
        height=100
    )

def generate_post(idea: str) -> Optional[Dict]:
    """
    Send the user's idea to our backend API and get a generated post.
    
    Args:
        idea (str): The user's post idea
    
    Returns:
        dict: The generated post data or None if there's an error
    """
    try:
        # Send request to our backend
        response = requests.post(
            "http://localhost:8000/generate",
            json={"user_prompt": idea}
        )
        return response.json()
    except Exception as e:
        st.error(f"Oops! Something went wrong: {str(e)}")
        return None

def main():
    # Set up the page
    setup_page()
    
    # Get user's idea
    idea = get_user_input()
    
    # Add a Generate button
    if st.button("Generate Post 🚀") and idea:
        with st.spinner("Creating your post..."):
            result = generate_post(idea)
            
            if result and result.get("content"):
                # Show the generated post
                st.subheader("Your Generated Post:")
                st.write(result["content"])
                
                # Add a button to post to LinkedIn
                if st.button("Post to LinkedIn 🌟"):
                    # Here we would add the LinkedIn posting logic
                    st.success("Posted to LinkedIn successfully!")
    
    # Add helpful tips in the sidebar
    with st.sidebar:
        st.subheader("Tips for Better Posts:")
        st.markdown("""
        - Be specific about your topic
        - Mention your target audience
        - Include keywords from your industry
        """)

if __name__ == "__main__":
    main()
