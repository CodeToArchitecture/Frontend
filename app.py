import requests
import streamlit as st


node_api_url = "http://localhost:3000/process-repo"

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
def populate_files(github_url):
    return
    # Call Node populate_files
    data = {
    "githubUrl": str(github_url)
    }
    params = {
    "downloadAll": "false"  # or "true" if you want to download all files
    }

    response = requests.post(node_api_url, json=data, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        print("Success:", response.json())
    else:
        print("Error:", response.status_code, response.json())


def get_architecture_diagram():
    # Generate prompt from files
    # Send context and prompt to get_image 
    return './rick.png'


if submit_repo and repo_link:
    populate_files(repo_link)
    st.session_state.image_path = get_architecture_diagram()


if 'image_path' in st.session_state and st.session_state.image_path:
    st.image(st.session_state.image_path)

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
