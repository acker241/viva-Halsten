import streamlit as st

st.set_page_config(layout='wide')

img = 'pages\\logo.png'
st.image(img)



st.header('Seu ambiente de facilidades no nosso universo.')
ic1, ic2, ic3 = st.columns([0.1, 0.3, 0.6])

with ic1:
    st.image('pages\\perfilTransp.png', width=120)
with ic2:
    st.write('Como está hoje Fulano de Tal?')