import streamlit as st
st.title(":red[A simple e-commerce website prototype]")
st.subheader("This is a simple e-commerce website prototype built using Streamlit.")
st.write("You can use this prototype to add products to the cart and allow users to browse and purchase them.")
st.image("C:\\Users\\Harshil Gandhi\\OneDrive\\Pictures\\modiji-17605779 (1).png", caption="Modiji")
buttoninput=st.button("Modiji is the best")
audiofile = open("C:\\Users\\Harshil Gandhi\\Downloads\\modih_ringtone.mp3", "rb")
audio_bytes = audiofile.read()

if buttoninput:
    st.write("Yes, Modiji is the best!")
    st.audio(audio_bytes, format="audio/mp3",autoplay=True)