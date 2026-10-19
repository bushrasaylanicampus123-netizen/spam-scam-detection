
import streamlit as st

st.title("AI Spam and Scam Detection")
st.write("Enter a message to check for suspicious signs.")

message = st.text_area("Enter your message")

words = [
    "won", "free", "prize", "urgent",
    "click here", "verify your account",
    "password", "otp", "bank details"
]

if st.button("Check Message"):
    if not message.strip():
        st.warning("Please enter a message.")
    else:
        found = []

        for word in words:
            if word in message.lower():
                found.append(word)

        if found:
            st.error("Suspicious signs found!")
            st.write("Warning words:", ", ".join(found))
        else:
            st.success("No suspicious phrases found.")

        st.subheader("Safety Advice")
        st.write("- Do not click unknown links.")
        st.write("- Never share your password or OTP.")
        st.write("- Verify messages from official sources.")
