from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "shivam_Java_stack_resume.pdf"
profile_pic = current_dir / "assets" / "photoshivam.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Shivam Singh"
PAGE_ICON = ":wave:"
NAME = "Shivam Singh"
DESCRIPTION = """
I am complete my graduation in math and diploma in information technology. i am looking software developer job thanks.
"""
SUMMARY = """
    I have 2 years of experience as a software developer, contributing to open-source projects, participating in
Hacktoberfest since 2023, and working on real-world projects. I am seeking a software developer position.
"""
EMAIL = "shiva850681@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/shivamsaeeam/",
    "GitHub": "https://github.com/shivamkumarsingh28",
}
Certificate = {
    "Android Developer(Google)": "https://g.dev/shivamkumarsingh",
    "Soft Skills": "https://drive.google.com/file/d/1c6Jmt26WhcXvwObN4DRQ9sHwPowt52or/view",
    "Digital Marketing(Google)": "https://drive.google.com/file/d/1Jswln7JTAzA6Sg5ZfLihStLIPj-eVGx9/view",
    "DSA(NPTEL)": "https://drive.google.com/file/d/1S31oXu1wztHfg5ZMLfJFucB2b3bLvBWN/view",
}
PROJECTS = {
    "🏆 InternCollab - Internship website backend in java, springboot, mysql, api": "https://github.com/shivamkumarsingh28/InternCollab-SpringBoot",
    "🏆 Car selling website - car selling website in react, javascript": "https://shivamkumarsingh28.github.io/React_tesla_app/",
    "🏆 School management system - online education managing website in python, django, mysql": "https://github.com/shivamkumarsingh28/Python_Django_School_Management_Project",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")



# summary 
st.write('\n')
st.subheader("Summary")
st.write(SUMMARY)

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Education")


st.write("Diploma")
st.write("09/2022 - 10/2024")
st.write(
    """
- ✔️ I am complete my diploma in information technology from nsti bengaluru
- ✔️ In diploma i learn hardware & networking, cloud engineer, or software developer
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)

st.write("Graduation")
st.write("03/2019 - 05/2022")
st.write(
    """
- ✔️ I am complete my graduation in bscg from ignou delhi
- ✔️ My bsc subject is math and optional subject is botany and zoology
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Languages:- Java, springBoot, hibernate, Oops, ReactJs, JavaScript, Python, API, Postman
- 📊 Developer Tools:- VS Code, GCP, AWS, Android Studio, Window, Linux, GitHub, CI/CD, Agile/Scrum methodologies
- 🗄️ Databases:- MongoDB, MySQL
"""
)

# Certifications/Training
st.write('\n')
st.subheader("Certifications/Training")
cols = st.columns(len(Certificate))
for index, (platform, link) in enumerate(Certificate.items()):
    cols[index].write(f"[{platform}]({link})")



# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**FUll Stack Java Developer Intern | IBM Pvt. Ltd | Bengaluru, Karnataka**")
st.write("March 2024 – October 2024")
st.write(
    """
- ► Led the team in developing projects spanning app, web, and software domains over 6 months.
- ► Achieved 100% accuracy and bug-free delivery, with 90% clean code and 90% SEO-friendliness.
- ► Successfully built and launched 4 projects, showcasing commitment to 4 excellence in Java development.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Software Developer | CrudAster pvt. Ltd. | Delhi**")
st.write("September 2021 – August 2022")
st.write(
    """
- ► built and maintained over 10 software systems, collaborating with cross-functional teams during design reviews to select optimal technologies, reducing development time by 15%.
- ► Provided technical feedback to enhance 4 project efficiency and ensure alignment with business requirements.
- ► Ensured adherence to best practices in coding standards, version control, and performance optimization, improving code
quality by 20%.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**App Developer | Yellowsense pvt. Ltd. (Hybrid) | Bengaluru, Karnataka**")
st.write("March 2021 – August 2021")
st.write(
    """
- ► Developed and maintained mobile applications using React Native for both Android and iOS platforms, delivering 5+
high-performance apps.
- ► Focused on 100% scalability and responsiveness to enhance user engagement and satisfaction.
- ► Optimized application performance and reduced app load time by 20% through effective performance tuning and code
optimization.

"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
