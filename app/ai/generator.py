from typing import Dict, Optional
import openai
from .prompts import LINKEDIN_POST_PROMPT
import os
from dotenv import load_dotenv

# Load our environment variables
load_dotenv()

# Set up OpenAI with our API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_linkedin_post(user_idea: str) -> str:
    """
    Generate a professional LinkedIn post from a user's idea using AI.
    
    Args:
        user_idea (str): The user's post idea or topic
    
    Returns:
        str: The generated LinkedIn post
    
    Example:
        idea = "Share my experience learning Python"
        post = generate_linkedin_post(idea)
        # Returns a professionally written post about Python learning
    """
    try:
        # Combine our base prompt with the user's idea
        full_prompt = LINKEDIN_POST_PROMPT.format(user_idea=user_idea)
        
        # Ask GPT to generate a post
        response = openai.ChatCompletion.create(
            model="gpt-4",  # You can use gpt-3.5-turbo for a cheaper option
            messages=[
                {"role": "system", "content": "You are a professional LinkedIn content creator."},
                {"role": "user", "content": full_prompt}
            ],
            temperature=0.7,  # Makes the output somewhat creative but still professional
            max_tokens=500    # Limits the response length
        )
        
        # Get the generated post from the response
        generated_post = response.choices[0].message.content.strip()
        
        return generated_post
    
    except Exception as e:
        # If something goes wrong, we want to know what happened
        print(f"Error generating post: {str(e)}")
        raise

def format_post(content: str) -> str:
    """
    Format the generated post to look good on LinkedIn.
    
    Args:
        content (str): The raw generated post
    
    Returns:
        str: The formatted post
    """
    # Add line breaks between paragraphs
    formatted = content.replace("\n\n", "\n\n")
    
    # Make sure we have hashtags
    if not any(word.startswith('#') for word in content.split()):
        formatted += "\n\n#career #professional #growth"
    
    return formatted
