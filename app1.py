from pathlib import Path
import streamlit as st
import pandas as pd
from PIL import Image


# path settings
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile_pic.png"




#  general settings
PAGE_TITLE = "Digital CV | Nishant Zemse"
PAGE_ICON =":wave:"
NAME = "Nishant Zemse"
DESCRIPTION = """
A Dedicated and Motivated Computer Science Student
"""
EMAIL = "zemsenishant.twitter@outlook.com"
SOCIAL_MEDIA = {
    "LinkedIn" : "https://www.linkedin.com/in/zemse-nishant/",
    "Twitter" : "https://twitter.com/@zemse_Nishant",
    "Instagram":"https://www.instagram.com/imnot__nishant/",
}


st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON)


st.title("HELLO THERE!!")




#  load css , pdf and pfp
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html = True)
with open(resume_file,"rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)



#  heroo sectionnn

col1, col2 = st.columns(2,gap="small")
with col1:
    st.image(profile_pic,width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label = " 📄 Download Resume",
        data =PDFbyte,
        file_name =resume_file.name,
        mime = "application/octet-stream",
    )
    st.write("📫",EMAIL)



#  social linkss

st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")




#  key interests
st.write("#")
st.subheader("KEY INTERESTS")
st.write("""
 - ✔️ With a growing passion for technology, I'm currently focusing on PYTHON PROGRAMMING and exploring the dynamic field of WEB DEVELOPMENT. 
 - ✔️ I enjoy problem-solving and continuously making great efforts to expand my skills through hands-on learning and real-world projects
 - ✔️ Web Development (HTML, CSS, JavaScript basics)
 - ✔️ Python Programming
 - ✔️ Software Engineering Fundamentals
"""
)



#skills

st.write("#")
st.subheader("SKILLS")
st.write("""
 - 🐍💻 Programming: Python &  HTML
 - 🧠🧩 Problem-solving & logical thinking
 - 🚀📚 Self-motivated & eager to learn
 - 🤝👥 Teamwork and collaboration
 - ⏰📅 Time management

""")



# education details

st.write("#")
st.subheader("EDUCATION HISTORY")
st.write("----")

st.write("** ★ **""📘","**__SSC__**")
st.write("**passed in year 2023**")
data = {
 "SUBJECTS" : ["ENGLISH","MARATHI","HINDI","MATHEMATICS","SCIENCE AND TECHNOLOGY","SOCIAL SCIENCES","TOTAL MARKS"],
 "MARKS OBTAINED" : [80,86,85,92,89,90,442],
 "MAX MARKS" : [100,100,100,100,100,100,500]
 }
df = pd.DataFrame(data)
st.dataframe(df)

st.write("**★**""📗✏️ ","**__HSC__**")
st.write("**passed in year 2025**")

data2 ={
"SUBJECTS" : ["ENGLISH","MATHEMATICS AND STATISTICS","PHYSICS","CHEMISTRY","COMPUTER SCIENCE","TOTAL MARKS"],
"MARKS OBTAINED" : [79,65,50,79,193,476],
"MAX MARKS" : [100,100,100,100,200,600]
}
df2 = pd.DataFrame(data2)
st.dataframe(df2)

st.write("** ★ **📗🎓 BSC")
st.write("2025 - PRESENT")














