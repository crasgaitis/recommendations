import streamlit as st

st.set_page_config(
    page_title="Pocket Plots",
    # page_icon='https://i.imgur.com/VOJb5at.png',
    initial_sidebar_state="expanded",
)

with st.sidebar:
    min_number = st.number_input('Insert min price')
    max_number = st.number_input('Insert max price')

    min_number2 = st.number_input('Insert min size (acres)')
    max_number2 = st.number_input('Insert max size (acres)')
    
    user_input = st.text_input('Describe your desired land plot.', 'i want grassy land with water nearby')
    
st.markdown('###Pocket Plots <MATCH>')

st.write("We filter all land plots against your price and size ranges. Then, your plot description is compared with our own AI generated captions from land plot images, to find the best match!")

st.markdown(
    """
    <img src="https://i.imgur.com/iCDyPAt.jpg" alt="image"> """,
    unsafe_allow_html=True )

st.markdown("*a forest filled thin trees and bushes*")

