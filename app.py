import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components

BASE_DIR = Path(__file__).resolve().parent

#color and theme settings
st.markdown(
    """
    <style>
    .stApp {
        background-color: #F7F5EF;
        color: #34483E; 
    }
    .block-container {
        max-width: 1150px;
        padding-top: 3rem;
        padding-bottom: 3rem;
    }
    /*headings */
    h1, h2, h3 {
        color:#173F35 !important;
    }
    /*Body text*/
    p, li, label {
        color: #34483E !important;
    }
    /*Links*/
    a {
        color:#47765D !important;
    }
    /*Buttons and download buttons*/
    .stButton > button, 
    .stDownloadButton > button {
        background-color: #173F35; 
        color: #F7F5EF;
        border: 1px solid #173F35;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        transition: all 0.2s ease;
    }
    /*Button hover*/
    .st.Button . button:hover, 
    .stDownloadButton > button:hover {
    background-color: #47765D;
    color: #F7F5EF;
     border-color:#47765D; 
    }
    /*Sidebar*/
    section[data-testid="stSidebar"] {
        background-color:#E8EEE7;
    }
    /*Input fields*/
    .stTextInput input, 
    .stTextArea textarea {
        background-color: #FFFFFF;
        border-color: #B8CDBB;
    }
    /*Dividers*/
    hr {
    border-color:#DCE5DB;
    }
    /*Project cards*/
    div[data-testid='stVerticalBlockBorderWrapper'] {
        background-color:#FFFFFF;
        border: 1 px solid #DCE5DB;
        border-radius: 12px;
        padding: 1rem;
    }
    /*Captions*/
    small, 
    .stCaption {
        color:#68786D;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
<h1 style='text-align:center;color: #173F35;
'>Stephanie McClung
</h1>
""",
    unsafe_allow_html=True
)

st.markdown("""
<div style="text-align: center;">
    <h2 style="color: #173F35; font-weight: normal;">
        Human Performance | Sports Science
    </h2>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center;">
    <h3 style="color: #173F35; font-weight: normal; font-size: 18px;">
       Human Performance Specialist Skilled in Data Collection, Athlete Monitoring, Sports Science Technology, Strength and Conditioning, and Data Analytics.
    </h3>
</div>
""", unsafe_allow_html=True)


import base64

st.header('Resume')

resume_file = BASE_DIR / "resume for streamlit.pdf"

if resume_file.exists():

    resume_bytes = resume_file.read_bytes()


    st.download_button(
        label="Download Resume",
        data=resume_bytes,
        file_name="Stephanie_McClung_Resume.pdf",
        mime="application/pdf"
    )
    base64_pdf = base64.b64encode(resume_bytes).decode("utf-8")

    pdf_display = f"""
        <iframe
            src="data:application/pdf;base64,{base64_pdf}"
            width="100%"
            height="900"
            style="border: none;">
        </iframe>
    """

    st.markdown(pdf_display, unsafe_allow_html=True)

else:
    st.error("Resume PDF not found.")

st.divider()
st.header('Projects')

st.subheader('Athlete Monitoring')
st.markdown(
    """
        This project involved analyzing 4 travel-flagged
        football players and comparing their loads to
        their position average for each practice period
        to identify when exactly they are taking on too much. This allows SPT to understand how in season schedules influence the players workload and recovery.
  
    """,
    unsafe_allow_html=True
)

project_folder = BASE_DIR / "Athlete Flagging - Stephanie McClung"

projects = {
    "Athlete 1": "Athlete 1.html",
    "Athlete 2": "Athlete 2.html",
    "Athlete 3": "Athlete 3.html",
    "Athlete 4": "Athlete 4.html"
}

for name, filename in projects.items():
    with st.expander(name):
        file_path = project_folder / filename

        if file_path.is_file():
            html_content = file_path.read_text(encoding="utf-8")
            components.html(html_content, height=900, scrolling=True)
        else:
            st.error(f"File not found: {file_path}")

st.subheader('Statistical Analysis')
st.markdown(
    """
        A course project that involved importing a specific sports dataset and performing statistical analysis on it to find trends and insights. I have gained skills in identifying trends through regression charts, plots, and heatmaps. I have also learned how to use statistical analysis to make predictions and inform decision-making in sports performance.
    """,
    unsafe_allow_html=True
)

BASE_DIR = Path(__file__).resolve().parent    
html_file = BASE_DIR / "Simple heatmaps baseball.html"
with st.expander("Statistical Analysis"):
    if html_file.exists():
        html_content = html_file.read_text(encoding="utf-8")
        components.html(html_content, height=900, scrolling=True)
    else:
        st.error(f"File not found: {html_file}")

    pdf_display = f"""
        <iframe
            src="data:application/pdf;base64,{base64_pdf}#toolbar=1&navpanes=0&view=FitH"
            width="100%"
            height="950px"
            style="background-color: #FFFFFF; border: none;"
        ></iframe>
    """

    st.markdown(pdf_display, unsafe_allow_html=True)

st.subheader('Analyzing Data')
st.markdown(
    """
         A standard procedure to look over the testing we did on the athletes and check for any sudden changes of force power or asymmetry. This project demonstrates an applied approach to performance testing to support the athletes.
    """,
    unsafe_allow_html=True
)

project_folder = BASE_DIR / "DEVO Team 2026- Stephanie McClung"

projects = {
    "CMJ": "CMJ.html",
    "Nordic Curl": "Nordic Curl.html",
    "Nordic Isoprone": "Nordic Isoprone.html"
}

for name, filename in projects.items():
    with st.expander(name):
        file_path = project_folder / filename

        if file_path.is_file():
            html_content = file_path.read_text(encoding="utf-8")
            components.html(html_content, height=900, scrolling=True)
        else:
            st.error(f"File not found: {file_path}")

st.subheader('Master Tracker')
st.markdown(
    """
         As a regional team member for a franchise of four gym locations, I am in charge of auditing new member sign-ups. Through this role, I have used my Excel coding skills to create a master tracker that allows me to track the sales of each location and identify any discrepancies in the data.
    """,
    unsafe_allow_html=True
)


project_folder = BASE_DIR / "New Member Investment MASTER TRACKER"

projects = {
    "1st Phone Call": "1st Phone Call.html",
    "2nd Follow Up": "2nd Follow Up.html",
    "Master Tracker": "Master Tracker.html",
    "Sales Audit": "Sales Audit.html"
}

for name, filename in projects.items():
    with st.expander(name):
        file_path = project_folder / filename

        if file_path.is_file():
            html_content = file_path.read_text(encoding="utf-8")
            components.html(html_content, height=900, scrolling=True)
        else:
            st.error(f"File not found: {file_path}")