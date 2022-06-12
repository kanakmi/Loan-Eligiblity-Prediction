import streamlit as st
import pickle

st.sidebar.title("Loan Eligibility Prediction")
text = '''
Loan Eligibility Prediction uses Random Forest Classifier to predict whether a person is eligible for a loan or not.

It uses the principle of Responsible AI and keeps the predictions transparent to the user. Responsible AI is the practice of designing, developing, and deploying AI with good intention to empower employees and businesses, and fairly impact customers and society—allowing companies to engender trust and scale AI with confidence.

If the user is not eligible for a loan, the AI will tell you why.

Many banks have not been able to provide transparency into the process of their loan eligibility prediction systems, which can lead to some awkward conversations between clients and bank employees. Our app will help banks give a more appropriate answer to why an application was rejected, so that people are able to learn from mistakes and submit better applications next time.
'''
st.sidebar.write(text)
x = False

profession = [
    'Air Traffic Controller',
    'Analyst',
    'Architect',
    'Army Officer',
    'Artist',
    'Aviator',
    'Biomedical Engineer',
    'Chartered Accountant',
    'Chef',
    'Chemical Engineer',
    'Civil Engineer',
    'Civil Servant',
    'Comedian',
    'Computer Hardware Engineer',
    'Computer_operator',
    'Consultant',
    'Dentist',
    'Design Engineer',
    'Designer',
    'Drafter',
    'Economist',
    'Engineer',
    'Fashion Designer',
    'Financial Analyst',
    'Firefighter',
    'Flight_attendant',
    'Geologist',
    'Graphic Designer',
    'Hotel Manager',
    'Industrial Engineer',
    'Lawyer',
    'Librarian',
    'Magistrate',
    'Mechanical Engineer',
    'Microbiologist',
    'Official',
    'Petroleum_Engineer',
    'Physician',
    'Police Officer',
    'Politician',
    'Psychologist',
    'Scientist',
    'Secretary',
    'Software Developer',
    'Statistician',
    'Surgeon',
    'Surveyor',
    'Technical writer',
    'Technician',
    'Technology Specialist',
    'Web Designer'
]

states = [
    'Andhra Pradesh',
    'Assam',
    'Bihar',
    'Chandigarh',
    'Chhattisgarh',
    'Delhi',
    'Gujarat',
    'Haryana',
    'Himachal Pradesh',
    'Jammu and Kashmir',
    'Jharkhand',
    'Karnataka',
    'Kerala',
    'Madhya Pradesh',
    'Maharashtra',
    'Manipur',
    'Mizoram',
    'Odisha',
    'Puducherry',
    'Punjab',
    'Rajasthan',
    'Sikkim',
    'Tamil Nadu',
    'Telangana',
    'Tripura',
    'Uttar Pradesh',
    'Uttarakhand',
    'West Bengal'
]

def predict(income, age, exp, mat, house, car, proff, state, cJY, cHY):
    model = pickle.load(open('model.pkl', 'rb'))
    if mat=='Single':
        mat=0
    else:
        mat=1
    if house=='Rented':
        house=0
    else:
        house=1
    if car=='Yes':
        car=1
    else:
        car=0
    data = [income, age, exp, mat, house, car, cJY, cHY]
    prof_array = [0]*len(profession)
    state_array = [0]*len(states)
    prof_array[profession.index(proff)] = 1
    state_array[states.index(state)] = 1
    data.extend(prof_array)
    data.extend(state_array)
    ans = model.predict([data])
    return ans[0]

def parsePrediction(prediction):
    if prediction==0:
        st.balloons()
        st.header("Congratulations! You are Eligible for the loan.")
    else:
        st.header("Sorry! You are not eligible for the loan.")

with st.form("input form"):
    col1, col2 = st.columns(2)
    income = col1.number_input("Annual Income (in ₹)", value=0, step=1, key="income", min_value=0)
    age = col2.number_input("Age", value=21, step=1, key="age", min_value=21)
    exp = col1.number_input("Experience (in Years)", value=0, step=1, key="exp", min_value=0)
    mat = col2.selectbox("Marital Status", ["Single", "Married"], key="mat")
    house = col1.selectbox("House Ownership", ["Rented", "Owned"], key="house")
    car = col2.selectbox("Do you own a Car?", ["Yes", "No"], key="car")
    proff = col1.selectbox("Profession", profession, key="proff")
    state = col2.selectbox("State", states, key="state")
    cJY = col1.number_input("Years in Current Job", value=0, step=1, key="cJY", min_value=0)
    cHY = col2.number_input("Years in Current Home", value=0, step=1, key="cHY", min_value=0)

    _, cent, _ = st.columns([4,1,4])
    submitted = cent.form_submit_button("Submit")

    if submitted:
        prediction = predict(income, age, exp, mat, house, car, proff, state, cJY, cHY)
        x = True

def getInsight():
    if age<=30:
        st.write("People with age less than 30 are 3% less likely to be eligible for the loan.")

    if exp<=4:
        st.write("People with less than 5 years of experience are 4% less likely to be eligible for the loan.")
    elif exp<16:
        st.write("People with less than 16 years of experience are 2% less likely to be eligible for the loan.")
    
    if mat=='Single':
        st.write("People who are married are 3% more likely to be eligible for the loan.")

    if house=='Rented':
        st.write("People who own a house are 3% more likely to be eligible for the loan.")

    if car=='No':
        st.write("People who own a car are 2% more likely to be eligible for the loan.")
    
    if cJY<=2:
        st.write("People who have less than 3 years of experience in current job are 4% less likely to be eligible for the loan.")
    if cJY<5:
        st.write("People who have less than 5 years of experience in current job are 2% less likely to be eligible for the loan.")

    if cHY<=11:
        st.write("People who have less than 12 years of time in current home are 2% less likely to be eligible for the loan.")

if x:
    parsePrediction(prediction)
    if prediction==1:
        with st.expander("Want to know more?"):
            getInsight()
    x = False
