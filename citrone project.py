import numpy as np
import pickle
import streamlit as st 

# loading the saved model
loaded_model = pickle.load(open(r'C:\Users\HomePC\Mr temitope class\Intro to ML\deployment_model.pkl', 'rb'))

# A function that will process the user input
def performance_prediction(input_data):
    
    # converted to array
    input_data_array = np.asarray(input_data)
    # reshape the so the model will understand it
    input_data_reshaped = input_data_array.reshape(1, -1)

    # Getting a prediction
    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 0:
        return("This student is not eligible")
    else:
        return("Passed")
    

def main():
    # giving the app a title
    st.title('Citrone performance Web App')

    # getting the input data from user

    Quiz_summary = st.text_input('Quiz Summary score')
    Assignment_Summary = st.text_input('Assignment Summary score')
    Grade_Point_Average = st.text_input('Learner\'s Grade point Average')
    Age = st.text_input('Learner\'s Age')
    Children = st.text_input('Does learner have child/children ? 1 for Yes/ 0 for No')
    Completed_Nysc = st.text_input('Completed Nysc ? 1 for Yes/ 0 for No')
    Gender = st.text_input('Is learner\'s gender ? 1 for Male/ 0 for Female')

    # code for prediction
    performance = ''

    # creating a button for prediction
    if st.button('Eligibility Result'):
        performance = performance_prediction([float(Quiz_summary), float(Assignment_Summary), float(Grade_Point_Average),
                                              int(Age), int(Children), int(Completed_Nysc), int(Gender)])
        st.success(performance)


if __name__ == '__main__':
    main()
