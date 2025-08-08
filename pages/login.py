import streamlit as st
from auth_db import csr, conn

def logout_this():
    st.session_state.authenticated = False
    st.session_state.username = ""
    st.rerun()

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "username" not in st.session_state:
    st.session_state.username = ""

if st.session_state.authenticated:
    st.success(f"Already Login as: {st.session_state.username}")
    st.write("Click on Logout to end the session.....!")
    if st.button("Logout"):
        logout_this()


else:
    st.title("Login page")

    username = st.text_input("Enter your username")

    password = st.text_input("Enter your password", type="password")

    btn = st.button("Login")


    if btn:
        if username == "" or password == "":
            st.error("Please fill all the fields")
            st.snow()

        else:
            csr.execute(f"select * from signup_user where username = '{username}';") 
        
            check_username = csr.fetchone()

            if check_username is None:
                st.warning("Username does not found.")
        
            else:

                if password != check_username[4]:
                    st.warning("Please enter valid password.")
            
                else:
                    st.session_state.authenticated = True
                    st.session_state.username = check_username[0]
                    st.session_state.full_name = check_username[1]
                    st.write(check_username)
                    st.write(f"you successfully login as {check_username[1]}")
                    st.success("Login successful done")
                    st.balloons()
                    st.rerun()
        

        st.write(check_username)
    

