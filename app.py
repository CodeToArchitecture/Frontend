import streamlit as st

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

def get_api_response(repo_link):
    # Your actual API call to get the iframe or relevant information
    path = './rick.png'
    return path

def chat_with_bot(user_message):
    # Your actual chatbot backend call
    return "Echo: " + user_message

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

def send_message():
    user_message = st.session_state.user_message
    if user_message:  # Check if the message is not empty
        st.session_state.chat_history.append(f"You: {user_message}")
        bot_response = chat_with_bot(user_message)
        st.session_state.chat_history.append(f"Bot: {bot_response}")
        # Clear the input
        st.session_state.user_message = ""

st.title("Code To Architecture")

repo_link = st.text_input("Enter GitHub repository link:", key="repo_link")
submit_repo = st.button("Submit GitHub Link")

if submit_repo and repo_link:
    st.session_state.iframe_html = get_api_response(repo_link)

if 'iframe_html' in st.session_state and st.session_state.iframe_html:
    st.image('./rick.png')


# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
