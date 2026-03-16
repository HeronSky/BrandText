import streamlit as st,io
from styles import g,n

st.set_page_config(page_title="BrandText", layout="centered")
st.title("BrandText")

with st.container(border=True):
    col1,col2 = st.columns([2,1])
    text = col1.text_input("Enter text","BrandText")
    style = col2.radio("Style",["Netflix","Google"],horizontal=True)
    if style == "Netflix":
        size = col1.slider("Font Size",50,200,150)
        curve = col1.slider("Curve",0,100,30)
    else:
        size = col1.slider("Font Size",50,200,150)
        curve = 0
if style == "Netflix":
    img = n.render(text,size,curve)
elif style == "Google":
    img = g.render(text,size)

st.image(img,use_container_width=True)

buf = io.BytesIO()
img.save(buf, format="PNG")
st.download_button(
    label=f"Download",
    data=buf.getvalue(),
    file_name=f"{text}.png",
    mime="image/png"
)
