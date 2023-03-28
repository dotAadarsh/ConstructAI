import streamlit as st 

st.set_page_config(page_title="Construct.AI", page_icon="🐍", layout="wide")

st.write("""
# Construct
Constructing the Quality Education with AI

**Theme:** Quality Education

**Problem:**

Despite the availability of educational resources, many students struggle to access quality education that meets their individual needs and learning styles. Our app aims to address this issue by leveraging AI technology to provide personalized and engaging educational content in various formats including transcripts, audio, video, and AI-generated blogs for an internal knowledge database. By tailoring the learning experience to each student’s needs, our app strives to improve educational outcomes and promote lifelong learning.

In today’s fast-paced world, students are often overwhelmed by the sheer volume of educational content available in various formats. It can be challenging to sift through and comprehend all the information, leading to suboptimal learning outcomes. Our app aims to address this issue by leveraging AI technology to summarize text contents in various formats, providing students with concise and easily digestible information. By making educational content more accessible and manageable, our app strives to improve educational outcomes and promote lifelong learning.

**Solution:**

Our project Construct.AI implements two tools Internal knowledge database and a summarizer for the above problem statements. The main idea is to implement AI in education to solve various problems.

The Internal Knowledge database is designed so that the staff/faculties can add resources in google sheets (CSV file) which are then integrated with AI. It provides a transcript, AI-generated blog, and audio.

The summarizer tool extracts texts from various formats of input and provides a summary of it. It is also integrated with ChatGPT to ask content-related queries.
""")