import streamlit as st

st.set_page_config(
    page_title="My School Portal",
    page_icon="🏫"
)

st.title("🏫 My School Management Portal")
st.write("Welcome to your school portal!")

st.subheader("Add Student")

with st.form("student_form"):
    name = st.text_input("Student Name")
    class_name = st.selectbox(
        "Class",
        ["6", "7", "8", "9", "10"]
    )
    roll_no = st.text_input("Roll Number")

    submitted = st.form_submit_button(
        "Add Student"
    )

    if submitted:
        if name.strip() and roll_no.strip():
            st.success(
                f"Student {name} is ready to be saved."
            )
            st.write("Class:", class_name)
            st.write("Roll Number:", roll_no)
        else:
            st.warning("Please enter the name and roll number.")
