# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 19:58:25 2022

@author: LENOVO
"""

import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('Spyder/trained_model.sav', 'rb'))


# creating a function for prediction

def h_d_prediction(i_d):

    # changing the input data to a numpy array
    i_d_n = np.asarray(i_d)

    # reshape the numpy array as we are predicting for only one instane
    i_d_rp = i_d_n.reshape(1,-1)

    prediction = loaded_model.predict(i_d_rp)
    print(prediction)

    if(prediction[0]==0):
      return 'the Person Does Not Have Heart Disease'
    else:
      return 'The Person Has Heart Disease'
  

def main():
    
    # giving a title 
    st.title('Heart Disease Prediction Web App')
    
    # getting the input data from input user
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age Of The Person')
    with col2:    
        sex = st.number_input('Gender')
    with col3:
        cp = st.number_input('Chest Pain')
    with col1:
        trestbps = st.number_input('Resting Blood Pressur')
    with col2:    
        chol = st.number_input('Serum Cholestrol')
    with col3:
        fbs = st.number_input('Fasting Blood Sugar')
    with col1:
        restecg = st.number_input('Resting Electrocardiographic Results')
    with col2:
        thalach = st.number_input('Maximun Heart Rate Achieved')
    with col3:
        exang = st.number_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.number_input('ST Depression')
    with col2:
        slope = st.number_input('The Slope Of The Peak Exercise ST Segment ')
    with col3:
        ca = st.number_input('No Of Major Vessels')
    with col1:
        thal = st.number_input('Thal')
    
    
    # code for prediction
    diagnosis = ''
    
    # creating a button for prediction
    if st.button('Heart Disease Result'):
        diagnosis = h_d_prediction([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
        
    st.success(diagnosis)
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    