import streamlit as st

FASTAPI_URL = "https://localhost:8000"  

st.title("AI Assistant for Travellers")
st.markdown("This is an AI Assistant to create trip itineraries.")
st.subheader("Ask your travel questions")

question = st.text_input("Enter your question here")
if st.button("Ask"):
    if question.strip():
        with st.spinner("Processing your question..."):
            st.success("your question is: " + question) 
    else:
        st.warning("Please enter a question to proceed.")


with st.sidebar:
    st.subheader("Upload files")
    file = st.file_uploader("Upload your travel documents(optional)", type="pdf")

    if file:
        if st.button("Process File"):
            with st.spinner("Processing the uploaded file..."):
                st.success("File processed successfully! (This is a placeholder message)")

