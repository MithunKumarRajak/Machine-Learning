
import streamlit as st
st.title("Hello streamlit !") # to show title
# 
st.header("This is a header") # to show header
st.subheader("This is a sub header") # to show sub header

st.text("This is a text") # to show text


# uses st.markdown() to show formatted text.
# #### --> creates a level 3 header

st.markdown("# This is a markdown header")
st.markdown("## This is a markdown header")
st.markdown("### This is a markdown header")
st.markdown("#### This is a markdown header")
st.markdown("##### This is a markdown header")


# To shows how to display different types of messages and alerts in a Streamlit app using built-in functions like
# st.success(), st.info(), st.warning(), st.error() and st.exception().
# These functions help communicate status, information, warnings, errors and exceptions to users clearly.

st.success("this is a Success message")

st.info("this is a Information message")

st.warning("this is a Warning")

st.error("this is a Error message")

exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)

# st.write() that can display text, numbers, data structures and even charts.
st.write("This is a simple text message using st.write()")

# Writing python inbuilt function range()
st.write(range(10))



# Display Images
# to display an image using Pillow library.
# The image is opened with Image.open() and displayed with st.image(), where the width parameter controls its size.

from PIL import Image  # Import Image from Pillow
image = Image.open("streamlit.png") # Open the image file
st.image(image, width=200) # Display the image with a specified width



# Checkbox
# checkbox in Streamlit to toggle content visibility

# Display a checkbox with the label 'Show/Hide'
if st.checkbox("Show/Hide"):
    # Show this text only when the checkbox is checked
    st.text("this is Showing the widget when the checkbox is checked")

#  Radio Button
# use radio buttons to let users select one option from a list.

status = st.radio("Gender selection ",['Male', 'Female'])

# Display the selected option using success message
if status == 'Male':
    st.success("Male")
else:
    st.success("Female")


# Selection Box
# select box in Streamlit to let users choose one option from a dropdown list.

hobby = st.selectbox("Select a Hobby:", ['None','Dancing', 'Reading', 'Sports'])

# Display the selected hobby
st.write("Your hobby is:", hobby)


# Multi-Selectbox
# a multiselect box in Streamlit, allowing users to choose multiple options from a list.

hobbies = st.multiselect("Select Your Hobbies:", ['Dancing', 'Reading', 'Sports'])

# Display the number of selected hobbies
st.write("You selected", len(hobbies), "hobbies")


# Button
# use buttons in Streamlit. Buttons can trigger specific actions when clicked, such as displaying a message
# A simple button that does nothing
st.button("Click Me")

# A button that displays text when clicked
if st.button("About"):
    st.text("Welcome to streamlit !")


# Text Input
# Text input fields allow users to enter custom data. This example collects a user's name, formats it with proper capitalization and displays it when Submit button is clicked

name = st.text_input("Enter your name", "Type here...")
# Display the name after clicking the Submit button
if st.button("Submit"):
    st.success(name)
    

# Slider
# Sliders provide a way to select numeric values within a range. This example lets users choose a level between 1 and 5 and displays the selected value instantly.
level = st.slider("Select a level", 1, 5)
st.write("Selected level:", level)

    
    