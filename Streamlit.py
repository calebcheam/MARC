import cv2
import numpy as np
import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2,preprocess_input as mobilenet_v2_preprocess_input


model = tf.keras.models.load_model("/Users/caleb/Desktop/caleb.h5")
### load file

st.title("WELCOME TO THE M.A.R.C BIN!!!")

st.title("PLEASE THROW YOUR TRASH BELOW")
uploaded_file = st.file_uploader("BIN", type="jpg")


map_dict = {0: 'cardboard',
            1: 'glass',
            2: 'metal',
            3: 'paper',
            4: 'plastic',
            5: 'trash'
            }



if uploaded_file is not None:
    # Convert the file to an opencv image.
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)
    opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
    resized = cv2.resize(opencv_image,(224,224))
    # Now do something with the image! For example, let's display it:
    st.image(resized, channels="RGB")

    
    img_reshape = resized[np.newaxis,...]

    Genrate_pred = st.button("Classify")    
    if Genrate_pred:
        prediction = model.predict(img_reshape).argmax()
        if prediction!= 5:
            st.title("You have just disposed {}, thank you so much!".format(map_dict[prediction]))
        else:
            st.title("Fuck you, you tried to throw something unrecycable inside, please go home and reflect")
