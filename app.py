# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import streamlit as st
import pandas as pd
import numpy as np

st.title('Dicey Tech - Predicting Student Responses')

tab1, tab2, tab3 = st.tabs(["ABOUT THE PROJECT", "PART 1", "PART 2"])

with tab1:
    st.write(r''' About the Project Aim: 
    Accurately predict which answers the students will choose  Part 1: To predict whether the student will get an answer right or wrong Part 2: To predict the exact option the student will choose in a test
    Some factors to consider:

    Student's Age and Time of Completion
    There is a huge difference between students who have just turned 10 and those who have been 10 for nearly a year. It's important to consider the student's age in detail as there can be substantial differences in knowledge based on a student’s age. Exams are generally standardised by how old a student is in terms of year and month.

    As the children age, it is also to consider their progress through the two years. It may be useful to see if you can calculate or predict their rate of improvement.

    Student's Skills
    Students may have different skill sets. You can consider analysing students by literary skills, such as vocabulary, punctuation, knowledge of idioms etc.

    Question Topic
    This is quite similar to assessing the student's skills but more so their application of them. The majority of questions have been labelled with their topic. You can consider analysing a student's comprehensive ability in terms of factual recall, inference, SPaG (spelling, punctuation and grammar), vocabulary, purpose etc.

    Difficulty of Question
    You can also consider the difficulty of each question. There are easier factual recall questions and harder factual recall questions. You can consider calculating each question's Difficulty Index and Discrimination Index.

    Text
    You may consider the genre of the text (Fiction, Non-Fiction, Poetry etc), length of the text, the complexity of the text (vocabulary, sentence structures), and time in which it was written. All of these factors influence a student's ability to comprehend the text. Just because they know all the words in a passage does not necessarily mean they understand what is happening. Some metrics that may be useful include the Lexile score of a text, or its ATOS level etc.

    Worksheet vs Mock Exam
    Students will generally perform worse under timed conditions so it is important to differentiate between whether the student has completed the work under timed conditions or not. Some texts such as Jane Eyre and Dorian Gray have been assessed under both conditions so it may be worth comparing the performance of the two.

    Worksheet data is completed at home.
    Mock exam data is completed in timed conditions.

    Children

    The students are children between 8-11. Depending on their engagement levels at the time of completion, they may not put in their full effort or concentration when completing their homework.''')

with tab2:
   st.header("PART 1")
   with st.form("my_form"):
       st.write("Write your prompt")
       passagetype = st.radio(
           "Please select",
           ["Worksheet", "Mockup Test"])
       passage = st.selectbox(
           'Select passage',
           ('PassageName','bluebird','dorian gray','jane eyre','notre-dame','metamorphosis','sleepy hollow','the hobbit','those winter','1984','anne','alice','baskervilles','black beauty','brazilian','charlottes','court life','DORIAN','dreams of a giant life','economics','fauntleroy','frankenstein','friendship','frost','gatsby','gibson','growth','gulliver','homing pigeon','honeybees','huck','i have a dream','jabberwocky','JANE EYRE','jekyll','lion','little women','lochinvar','lost treasure','magic city','marathon','matilda','meg','no enemies','nothing gold','NOTRE DAME','oliver twist -master','oliver twist -room','sense','patagonia','peter','rebecca','sea fever','secret garden','shiba','snowy river','sonnet 18','stopping by','this is going to hurt','THOSE WINTER','tom sawyer','treasure island','tyger','umami','van','voyage','war of the worlds','when u r old','wind in the willows','wizard','lost_in_the_woods','northern_lights','pollyanna'))
       grade = st.selectbox(
           'Student Grade',
           ('2', '3', '4', '5', '6', '7', '8', '9', '10'))
       hour = st.selectbox(
           'Hour of Time',
           ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17',
            '18', '19', '20', '21', '22', '23', '24'))

       #prompt = st.text_input('Prompt')
       prompt = passagetype + ' ' + passage + ' ' + grade + ' ' + hour
       url = 'http://chattinc.com/dicey/part1'

       data = {"text": f"{prompt}"}
       response = requests.post(url, json=data)

       # Every form must have a submit button.
       submitted = st.form_submit_button("Submit")
       if submitted:
           st.write("prompt", response.json())



with tab3:
   st.header("PART 2")
   st.write("Under Process")