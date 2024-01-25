from utils import run , remove_markdown , translate
from text2speech import text2speech
import streamlit as st 
import PIL

icon = PIL.Image.open("icon.png")
st.set_page_config(page_title='MedVision',
                   page_icon=icon,
                     layout="wide")

with st.sidebar : 
    st.write("Created By **Kirouane Ayoub**\nLinkedIn:**@ayoub-kirouane3**")
    st.image("icon.png" , width=150)
    use_voice =  st.checkbox("Use output voice")
    if use_voice == True : 
        voice_id = st.selectbox("Select Voice :" , ["Man" ,
                                                    "Women"])
    language = st.selectbox("Select Your Preferred Language :" , 
                            ["English" , "Arabic" , "French"] , 
                            index=0) 


st.title("Welcome to MedVision 👋")

st.info("""
**Project Overview:**
 *MedVision* project aims to develop a cutting-edge Vision Medical AI Assistant capable of analyzing medical
    images with unparalleled accuracy and efficiency. It seeks to revolutionize the field of medical 
    diagnostics and treatment by empowering healthcare professionals with detailed insights and 
    valuable information derived from various medical imaging modalities.
""")
img = st.sidebar.file_uploader("Upload Your Image : " , type=['png' , 'jpeg' , 
                                                              'jpg' , 'webp'])

if img : 
    if st.sidebar.button(":arrow_right: Click To start :arrow_left:") : 
        with st.spinner("🔎 Analysis is in progress...") : 
            image_bytes = img.getvalue()
            with open("output.png", "wb") as file:
                file.write(image_bytes)
            img = PIL.Image.open('output.png')
            responce = run(img=img)
            st.title("The Analysis' Results")
            st.image("output.png" , width=400)
            if language == "Arabic" or  language == "French" : 
                responce = translate(language=language , text=responce)
                st.write(responce)
                st.success("Done!")
            else : 

                st.write(responce)
                st.success("Done!")
            try : 
                if voice_id: 
                    with st.spinner("🗣️ Generating audio ..") : 
                        text = remove_markdown(responce)
                        text2speech(text=text , 
                                    voice_id=voice_id)
                        st.title("Audio Output : ")
                        st.audio("output.mp3")
                        st.success("Done!")
                else : 
                    pass
            except : 
                pass