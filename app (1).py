
import streamlit as st

st.title("AI Spam and Scam Detection")
st.write("Enter a message to check for suspicious signs.")

message = st.text_area("Enter your message")

suspicious_words = [
    "won", "free", "prize", "urgent",
    "click here", "verify your account",
    "password", "otp", "bank details"
]

if st.button("Check Message"):
    if message.strip() == "":
        st.warning("Please enter a message.")
    else:
        found = []

        for word in suspicious_words:
            if word in message.lower():
                found.append(word)

        if found:
            st.error("Warning: Suspicious signs found!")
            st.write("Suspicious phrases:", ", ".join(found))
        else:
            st.success("No suspicious phrases found.")

        st.subheader("Safety Advice")
        st.write("- Avoid clicking unknown links.")
        st.write("- Never share your password or OTP.")
        st.write("- Verify messages through official sources.")
