import streamlit as st
import requests

# Placeholder for the function to call your backend API.
# Replace with actual API call logic.
def get_api_response(repo_link):
    # Example: response = requests.get(f'YOUR_API_ENDPOINT?repo={repo_link}')
    # return response.json()
    return {"response": "This is a simulated response for " + repo_link}

# Streamlit UI layout
st.title("Code To Architecture")

# Input field for GitHub repository link
repo_link = st.text_input("Enter GitHub repository link:")

# Submit button
submit = st.button("Submit")

# Displaying the response below the search field upon submit
if submit:
    if repo_link:
        # Making a call to your backend API with the repo_link
        response = get_api_response(repo_link)
        # Displaying the API response
        st.write(response)
    else:
        st.write("Please enter a valid GitHub repository link.")

