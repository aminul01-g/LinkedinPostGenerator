# LinkedIn Post Generator for Beginners

A simple, easy-to-understand AI-powered LinkedIn post generator that helps create professional posts from your ideas.

## 🌟 What Does This Project Do?

This project helps you:
1. Write professional LinkedIn posts using AI
2. Preview your posts before publishing
3. Post directly to LinkedIn

## 🔧 How to Set Up (Step by Step)

1. Install Python (3.8 or higher)
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your configuration:
   - Add your OpenAI API key
   - Add your LinkedIn credentials

4. Start the application:
   ```bash
   # Start the backend (in one terminal)
   python -m app.backend.main

   # Start the frontend (in another terminal)
   python -m app.frontend.main
   ```

## 📁 Project Structure Explained

```
app/
├── frontend/        # The user interface (what you see)
├── backend/         # Handles requests and LinkedIn posting
└── ai/             # AI magic happens here!
```

## 🎓 Learning Points

This project teaches you:
1. How to use AI (GPT) to generate content
2. How to create a web interface (Streamlit)
3. How to build an API (FastAPI)
4. How to connect with LinkedIn's API

## 🚀 How to Use

1. Open the web interface (http://localhost:8501)
2. Type your post idea
3. Click "Generate Post"
4. Review the generated post
5. Click "Post to LinkedIn" if you like it

## 💡 Example Usage

Check the `examples/sample_posts.md` file for sample inputs and outputs!

## 📚 For Beginners

Each file in this project has detailed comments explaining:
- What the code does
- Why we wrote it that way
- How you can modify it

Take your time to read through the comments and understand each part!
# LinkedinPostGenerator
