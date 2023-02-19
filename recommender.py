import streamlit as st

st.set_page_config(
    page_title="Pocket Plots",
    # page_icon='https://i.imgur.com/VOJb5at.png',
    initial_sidebar_state="expanded",
)

with st.sidebar:
    min_number = st.number_input('Insert min price', min_value = 900, max_value = 44999, value = 5000)
    max_number = st.number_input('Insert max price', min_value = 901, max_value = 45000, value = 15000)

    min_number2 = st.number_input('Insert min size (acres)', min_value = 0, max_value = 41, value = 5)
    max_number2 = st.number_input('Insert max size (acres)', min_value = 1, max_value = 42, value = 10)
    
    user_input = st.text_input('Describe your desired land plot.', 'i want grassy land with water nearby')
    
st.markdown(
    """
    <img src="https://media.discordapp.net/attachments/1072641353030320219/1075635642056319016/pocket_plots.png?width=935&height=246
" alt="image" style = "max-width: 60vw"> """,
    unsafe_allow_html=True )


st.write("We filter all land parcels against your price and size ranges. Then, your parcel description is compared with our own AI generated captions from land images, to find your best parcel match!")
submit = st.button("Recommend a parcel!")

if submit:

    st.markdown(
        """
        <img src="https://i.imgur.com/iCDyPAt.jpg" alt="image" style = "max-height: 50vh"> """,
        unsafe_allow_html=True )

    st.markdown(":green[*a forest filled thin trees and bushes*]")

