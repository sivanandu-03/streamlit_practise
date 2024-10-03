import streamlit as st
st.title("Text Title")
st.caption("No Caption Needed!!!")
st.header("Heading section")
st.subheader("Sub-Heading section")
st.warning("Warning you entered the prohibited zone")
st.info("Information section")
st.error("this is an error message")
st.success("Your code run successfully")

# widgets - taking inputs from the user 


st.checkbox("Accept all")
st.radio("Gender",["Male","Female","Others"])
st.button("click me")
st.selectbox("choose your Branch",['Aiml','Cse','Mech'])
st.multiselect("choose the depatment: ",["content","sales","marketing"])
st.text_input("enter your email")
st.text_area("write your suggestions(optional)")
st.date_input("enter date of birth")
st.time_input("Hey What's the Time")

# Congratulation Balloons 

st.balloons()

#sidebar
st.sidebar.title("Details")
st.sidebar.text_input("Enter Your E-Mail")
st.sidebar.text_input("Password")
st.sidebar.button("Submit")