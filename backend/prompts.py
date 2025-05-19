import google.generativeai as genai

genai.configure(api_key="AIzaSyCppIg9EHb3J3YbgAypw0DFESr3Te2j8")

chatbot_prompt = """You are a helpful AI assistant for supply chain management.
You understand inventory, logistics, and procurement. Be concise and data-driven.
"""

def generate_response(user_query):
    model = genai.GenerativeModel('gemini-pro')
    convo = model.start_chat(history=[])
    convo.send_message(chatbot_prompt)
    response = convo.send_message(user_query)
    return response.text