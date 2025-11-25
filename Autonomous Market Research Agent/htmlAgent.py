from typing import TypedDict
from client import client
from state import State






def htmlConverterAgent(state:State)->dict:
    text=state['summarizedResult']
    completion = client.chat.completions.create(
    extra_body={},
    model="mistralai/mistral-7b-instruct:free",
    messages=[
            {
  "role": "system",
  "content": (
    "You are an expert at writing raw HTML code for rendering content dynamically using innerHTML.\n"
    "Your goal is to **analyze the given text** and **convert it into valid, structured raw HTML**.\n\n"
    " Important Rules:\n"
    "1. Use only standard HTML tags that are safe and allowed within `innerHTML` (e.g., <div>, <p>, <ul>, <li>, <strong>, <em>, <a>, <h1>-<h6>, etc.).\n"
    "2. Do not include <html>, <head>, <body>, or <script> tags — only use tags valid inside the body of a page.\n"
    "3. Preserve the **semantic meaning and formatting** of the original text — use headings, lists, bold, etc. as needed.\n"
    "4. If there are URLs or references in the text, convert them into clickable <a> tags.\n"
    "5. Do not skip any important part of the text.\n\n"
    
    " Step-by-step reasoning:\n"
    "1. Carefully read and understand the structure and purpose of the input text.\n"
    "2. Break the text into meaningful blocks — paragraphs, headings, bullet points, etc.\n"
    "3. Map each block to appropriate HTML tags.\n"
    "4. Ensure proper nesting and clean formatting.\n"
    "5. Output **only the raw HTML content** as your final answer.\n"
  )
},
{
  "role": "system",
  "content": f"""
This is the plain text to convert. Follow the reasoning steps above and output only raw HTML:
--- START OF TEXT ---
{text}
--- END OF TEXT ---

Now provide the structured HTML output (no explanation, just raw HTML):
"""
},

    ]
    )
    htmlResponse=completion.choices[0].message.content
    return{
         "htmlResponse":htmlResponse
    }


