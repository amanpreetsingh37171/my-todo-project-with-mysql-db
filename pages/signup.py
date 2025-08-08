import streamlit as st
from auth_db import csr, conn

st.title("My signup page")

col1, col2 =st.columns(2)

with col1:
    username = st.text_input("Enter unique username...")

with col2:
    full_name = st.text_input("Enter your full name")

phon = st.number_input("Enter your phone number")

email = st.text_input("Enter your email address")

password = st.text_input("Enter your password", type="password")

confirm_password = st.text_input("Confirm your password", type="password")


btn = st.button("Sign Up")

if btn:
    if username == full_name == "" or phon == "" or email == "" or password == "" or confirm_password == "":
        st.error("Please fill all the fields")
        st.snow()

    else:
        if password == confirm_password:
           try:
                csr.execute("INSERT INTO signup_user (username, full_name, phone_number, email, password) VALUES (%s, %s, %s, %s, %s)", 
                        (username, full_name, phon, email, password))
                conn.commit()
                st.success("You have successfully signed up!")
                st.balloons()

                st.markdown("[Go to Login Page](./login)")

           except Exception as e:
                st.error("Please check username must be unique")

        else:
            st.error("Passwords do not match. Please try again.")
