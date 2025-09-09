from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.ai.generator import generate_linkedin_post
from app.backend.linkedin import post_to_linkedin

# Create a FastAPI app with helpful documentation
app = FastAPI(
    title="LinkedIn Post Generator API",
    description="A simple API that generates and posts LinkedIn content",
    version="1.0.0"
)

# Define what our request data looks like
class PostRequest(BaseModel):
    user_prompt: str

# Define what our response data looks like
class PostResponse(BaseModel):
    content: str
    status: str
    message: Optional[str] = None

@app.post("/generate", response_model=PostResponse)
async def generate_post(request: PostRequest):
    """
    Generate a LinkedIn post from the user's idea.
    
    Args:
        request (PostRequest): Contains the user's post idea
    
    Returns:
        PostResponse: The generated post and status
    """
    try:
        # Generate the post using our AI module
        generated_content = generate_linkedin_post(request.user_prompt)
        
        return PostResponse(
            content=generated_content,
            status="success",
            message="Post generated successfully!"
        )
    
    except Exception as e:
        # If something goes wrong, tell the user
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate post: {str(e)}"
        )

@app.post("/post-to-linkedin")
async def create_linkedin_post(request: PostRequest):
    """
    Post the generated content to LinkedIn.
    
    Args:
        request (PostRequest): Contains the post content
    
    Returns:
        dict: Status of the LinkedIn post
    """
    try:
        # Use our LinkedIn module to post
        success = post_to_linkedin(request.user_prompt)
        
        if success:
            return {"status": "success", "message": "Posted to LinkedIn!"}
        else:
            raise HTTPException(
                status_code=500,
                detail="Failed to post to LinkedIn"
            )
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error posting to LinkedIn: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
