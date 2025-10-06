import streamlit as st
import pickle
import numpy as np
model = pickle.load(open("student_model.pkl", 'rb'))
st.title("Student Performance Predictor")

Hours_Studied= st.number_input("Hours Studied = ",min_value=0,max_value=100)
Attendance= st.number_input("Attendance (1-100) = ",min_value=0,max_value=100)
Parental_Involvement=st.selectbox("Parental Involvement = ", ["LOW","MEDIUM","HIGH"])
Access_to_Resources=st.selectbox("Access to Resources = ", ["LOW","MEDIUM","HIGH"])
Extracurricular_Activities=st.selectbox("Extracurricular Activities =", ["YES","NO"])
Sleep_Hours= st.number_input("Sleep Hours = ",min_value=0,max_value=100)
Previous_Scores= st.number_input("Previous Scores = ",min_value=0,max_value=100)
Motivation_Level=st.selectbox("Motivation Level = ", ["LOW","MEDIUM","HIGH"])
Internet_Access=st.selectbox("Internet Access =", ["YES","NO"])
Tutoring_Sessions= st.number_input("Tutoring Sessions = ",min_value=0,max_value=100)
Family_Income=st.selectbox("Family Income = ", ["LOW","MEDIUM","HIGH"])
Teacher_Quality=st.selectbox("Teacher Quality = ", ["LOW","MEDIUM","HIGH"])
School_Type=st.selectbox("School Type =", ["PUBLIC","PRIVATE"])
Peer_Influence=st.selectbox("Peer Influence = ", ["NEGATIVE","NEUTRAL","POSITIVE"])
Physical_Activity= st.number_input("Physical Activity = ",min_value=0,max_value=100)
Learning_Disabilities=st.selectbox("Learning Disabilities =", ["YES","NO"])
Parental_Education_Level=st.selectbox("Parental Education Level = ", ["HIGH SCHOOL","COLLEGE","POST GRADUATE"])
Distance_from_Home=st.selectbox("Distance from Home = ", ["NEAR","MODERATE","FAR"])
Gender=st.selectbox("Gender =", ["MALE","FEMALE"])

map_1 = {"LOW": 1, "MEDIUM": 2, "HIGH": 3}
Parental_Involvement_val = map_1[Parental_Involvement]
Access_to_Resources_val = map_1[Access_to_Resources]
Motivation_Level_val = map_1[Motivation_Level]
Family_Income_val = map_1[Family_Income]
Teacher_Quality_val = map_1[Teacher_Quality]

map_2 = {"YES": 1, "NO": 0}
Extracurricular_Activities_val = map_2[Extracurricular_Activities]
Internet_Access_val = map_2[Internet_Access]
Learning_Disabilities_val = map_2[Learning_Disabilities]

map_3 = {"PUBLIC": 1, "PRIVATE": 0}
School_Type_val = map_3[School_Type]

map_4 = {"MALE": 1, "FEMALE": 0}
Gender_val = map_4[Gender]

map_5 = {"NEGATIVE": 1, "NEUTRAL": 2, "POSITIVE": 3}
Peer_Influence_val = map_5[Peer_Influence]

map_6 = {"HIGH SCHOOL": 1, "COLLEGE": 2, "POST GRADUATE": 3}
Parental_Education_Level_val = map_6[Parental_Education_Level]

map_7 = {"NEAR": 1, "MODERATE": 2, "FAR": 3}
Distance_from_Home_val = map_7[Distance_from_Home]

if st.button("Predict"):
    input_data = np.array([[Hours_Studied,Attendance,Parental_Involvement_val,Access_to_Resources_val,Extracurricular_Activities_val,Sleep_Hours,Previous_Scores,Motivation_Level_val,Internet_Access_val,Tutoring_Sessions,Family_Income_val,Teacher_Quality_val,School_Type_val,Peer_Influence_val,Physical_Activity,Learning_Disabilities_val,Parental_Education_Level_val,Distance_from_Home_val,Gender_val]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Exam Score: {prediction[0]:.2f}")
