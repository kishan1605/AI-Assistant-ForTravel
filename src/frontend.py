import requests
import streamlit as st

FASTAPI_URL = "http://localhost:8000"  

st.title("AI Assistant for Travellers")
st.markdown("This is an AI Assistant to create trip itineraries.")


with st.sidebar:
    st.subheader("Upload files")
    file = st.file_uploader("Upload your travel documents(optional)", type="pdf")

    if file:
        if st.button("Process File"):
            with st.spinner("Processing the uploaded file..."):
                try:
                    files = {"file" : file}
                    response = requests.post(f"{FASTAPI_URL}/upload", files = files)
                    if response.status_code == 200:
                        st.success(response.json()["message"])
                    else:
                        st.error(f"Error: {response.json().get('message', 'unknown error')}")

                except Exception as e:
                    st.error(f"The error is {str(e)}")


st.subheader("Ask your travel questions")

question = st.text_input("Enter your question here")
if st.button("Ask"):
    if question.strip():
        with st.spinner("Thinking..."):
            try:
                response = requests.post(f"{FASTAPI_URL}/question", json={"qsn": question})
                if response.status_code == 200:
                    answer = response.json()["answer"]
                    st.success("Here’s your result:")
                    st.write(answer)
                else:
                    st.error("Server error! Try again later.")
            except Exception as e:
                st.error(f"Could not reach the FastAPI server: {e}")
    else:
        st.warning("Please enter a question to proceed.")


