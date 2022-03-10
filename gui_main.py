import streamlit as stream


stream.title("Medical Image(MedMNIST) Analysis and Classification")
stream.info("Classification of DermaMnist and RetinaMnist datasets using various models")
genre = stream.radio(
     "Select the dataset",
     ('DermaMnist', 'RetinaMnist'))

if genre == 'DermaMnist':
    stream.write('You selected DermaMnist.')
else:   
    stream.write("You selected RetinaMnist.")

stream.selectbox("Select the DNN model for classification", ["DermaMnist_1","DermaMnist_2","RetinaMnist_1","RetinaMnist_2"])

stream.file_uploader("Upload image here", type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)
stream.button("Classify")