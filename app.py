import streamlit as st
from auth_db import csr, conn
import pandas as pd

st.header("My Todo App")

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "username" not in st.session_state:
    st.session_state.username = ""

if st.session_state.authenticated:
    st.subheader(f"Add Todo ({st.session_state.username})")

    todo_title = st.text_input("Enter todo Title")

    desc = st.text_area("Brief about toto..")

    addin = st.button("Add Todo")
    
    if addin:
        if todo_title == "" or desc == "":
            st.error("Please fill all the fields")
    
        else:
            csr.execute(f"INSERT INTO mytodos(todo_added, todo_title, todo_desc) VALUES ('{st.session_state.username}', '{todo_title}', '{desc}')")

            conn.commit()

            st.success("Todo added successfully")
            st.balloons()

    st.header("My All Todos..")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.write("Todo ID")

    with col2:
        st.write("Todo Title")

    with col3:
        st.write("Todo Description")

    with col4:
        st.write("Delete Todo")

    

    csr.execute(f"select * from mytodos where todo_added = '{st.session_state.username}';")

    all_todo = csr.fetchall()

    for id, title, dec, done in all_todo:
        todo_id, til, desc, dlt = st.columns(4)

        with todo_id:
            checked = st.checkbox("Done", key = {id}, value = bool(done))

            if checked != bool(done):
                csr.execute(f"update mytodos set todo_done = {int(checked)} where todo_id = {id}")
                conn.commit()

        with til:
            st.write(f"{title}")

        with desc:
            st.write(f"{dec}")

        with dlt:
            x = st.button("x Delete", key = f"{id}")

            if x:
                csr.execute(f"delete from mytodos where todo_id = {id}")
                conn.commit()
                st.snow()
                st.rerun()


        st.write("---------------------------")
else:
    st.warning("Please Login first.!")

    st.markdown("[Go to Login Page](./login)")


#1 query = "SELECT * FROM signup_user;"

# df = pd.read_sql(query, conn)

# st.dataframe(df)

#2 my_file = st.file_uploader("upload your file to view data", type = ['csv'])

# if my_file != None:
#     data = pd.read_csv(my_file, encoding ='latin1')
#     st.dataframe(data)