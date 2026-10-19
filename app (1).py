
import streamlit as st
import pickle
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

st.title("AI Spam and Scam Detection")
st.write("Check a message for possible spam and warning signs.")

@st.cache_resource
def load_files():
    model = load_model("spam_model.keras")

    with open("tokenizer.pkl", "rb") as file:
        tokenizer = pickle.load(file)

    return model, tokenizer

model, tokenizer = load_files()

message = st.text_area("Enter your message")

if st.button("Check Message"):
    if message.strip() == "":
        st.warning("Please enter a message.")
    else:
        sequence = tokenizer.texts_to_sequences([message])
        padded = pad_sequences(sequence, maxlen=50)

        prediction = model.predict(padded, verbose=0)[0][0]

        if prediction >= 0.5:
            st.error("Prediction: SPAM")
        else:
            st.success("Prediction: NORMAL MESSAGE")

        st.subheader("Safety Advice")
        st.write("- Avoid clicking unknown links.")
        st.write("- Never share your password or OTP.")
        st.write("- Verify messages through official sources.")

        st.caption("Predictions may be incorrect. Always check the sender.")
