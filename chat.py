import streamlit as st

st.title("ChatGPT-like clone")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to simulate chatbot response
def simulate_chatbot_response(user_input):
    # Placeholder for a function that generates a chatbot response
    # Replace this with your actual logic or API call to get a response
    return f"Simulated response for: {user_input}"

# Function to handle chat input submission
def handle_chat_input():
    user_input = st.session_state.chat_input
    if user_input:  # Check if the input is not empty
        # Append user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        # Simulate getting a response from the chatbot
        chatbot_response = simulate_chatbot_response(user_input)
        # Append chatbot response to chat history
        st.session_state.messages.append({"role": "bot", "content": chatbot_response})

# Accept user input
user_input = st.text_input("What is up?", key="chat_input", on_change=handle_chat_input)

# Ensure the chat_input is reset after submission
if "chat_input" in st.session_state:
    st.session_state.chat_input = ""

# Display chat messages from history
for message in st.session_state.messages:
    with st.expander(f"{message['role'].capitalize()} says:", expanded=True):
        st.markdown(message["content"])
