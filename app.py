import streamlit as st
from api_calling import note_generator,audio_generator,quiz_generator
from PIL import Image 

st.title("Note Summery and Quiz Generator",anchor = False)
st.markdown("Upload upto 3 images to generate Note Summary and Quizes")
st.divider()

with st.sidebar:
    images = st.file_uploader("Upload the photos of your note:",
        type=['jpg','jpeg','png'],
        accept_multiple_files=True
    )
    pil_images = []
    for img in images:
        pil_img = Image.open(img)
        pil_images.append(pil_img)
    
    if len(images) > 3:
        st.error("Upload at max 3 images")
    else:
        if images:
            st.subheader("Uploaded Images")
            col = st.columns(len(images))
            for i,per_image in enumerate(images):
                with col[i]:
                    st.image(per_image)

    select_options = st.selectbox("Enter Difficulity",("Easy","Medium","Hard"),index = None)

    pressed = st.button("Click here to generate AI",type = "primary")

if pressed :
    if not images:
        st.error("You must upload atleast 1 image") 
    if not select_options:
        st.error("You must select a difficulity")
        
    if images and select_options:
        with st.container(border = 2):
                st.subheader("Your Note :")
                with st.spinner("AI is generating your Note..."):
                    notes = note_generator(pil_images)
                    st.markdown(notes)

        with st.container(border = 2):
                st.subheader("Audio Transcript:")
                with st.spinner("AI is generating your Audio..."):
                    audio = audio_generator(notes)
                    st.audio(audio)

        with st.container(border = 2):
                st.subheader(f"Quiz({select_options}) Difficulity:")
                with st.spinner("AI is generating your Quiz..."):
                        quizzes = quiz_generator(pil_images,select_options)
                        st.markdown(quizzes)
                    
       





    
