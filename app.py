import streamlit as st
def main():
    st.title("chatbot")
    st.markdown(
        """
        <style>
            .st-emotion-cache-janbn0 {
                background-color: #2b313e;
            }
            .st-emotion-cache-4oy321 {
                background-color: #475063;
            }
            section[data-testid="stSidebar"] {
                width: 380px !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.sidebar.title("Chat Sessions")
    pdf_toggle_col, voice_rec_col = st.sidebar.columns(2)
    pdf_chat = pdf_toggle_col.checkbox("PDF Chat", key="pdf_chat", value=False)
    st.session_key = "new_session"
    uploaded_audio = st.sidebar.file_uploader("Upload an audio file", type=["wav", "mp3", "ogg"])
    uploaded_image = st.sidebar.file_uploader("Upload an image file", type=["jpg", "jpeg", "png"])
    uploaded_pdf = st.sidebar.file_uploader("Upload a pdf file", accept_multiple_files=True)
    user_input = st.chat_input("Type your message here", key="user_input")
if __name__ == "__main__":
    main()
