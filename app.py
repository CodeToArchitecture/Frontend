import requests
import streamlit as st


####################
# DOM
####################
st.title("Codebase Explainer")

repo_link = st.text_input("Enter GitHub repository link:", key="repo_link")
submit_repo = st.button("Submit GitHub Link")

if "messages" not in st.session_state:
    st.session_state.messages = []

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []


####################
# Behaviour
####################
def populate_files():
    # Call Node populate_files
    pass

def get_architecture_diagram():
    # Generate prompt from files
    # Send context and prompt to get_image 
    pass


if submit_repo and repo_link:
    populate_files()
    st.image(get_architecture_diagram())











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
