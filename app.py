import requests
import anthropic
import streamlit as st


node_api_url = "http://localhost:3000/process-repo"
client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="your-api-key",
)
with open('./system_prompt_for_chat.txt', 'r') as file:
    system_prompt_for_chat = file.read()

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

def get_bot_response():
    return client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        temperature=0,
        system=system_prompt_for_chat,
        messages=st.session_state.messages
    )



if submit_repo and repo_link:
    populate_files(repo_link)
    st.session_state.image_path = get_architecture_diagram()


if 'image_path' in st.session_state and st.session_state.image_path:
    st.image(st.session_state.image_path)

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"][0]["text"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": [{"type": "text", "text": prompt}]})
    bot_response = get_bot_response()
    st.session_state.messages.append({"role": "system", "content": [{"type": "text", "text": bot_response}]})

    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display user message in chat message container
    with st.chat_message("system"):
        st.markdown(bot_response)
