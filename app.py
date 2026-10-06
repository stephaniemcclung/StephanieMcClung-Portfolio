import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Stephanie McClung Portfolio", 
    page_icon=":bar_chart:",
    layout='wide'
)

st.title('Stephanie McClung')
st.subheader('Sports Science | Human Performance')

st.write('Human Performance Specialist Skilled in Sports Science, Data Collection, Athlete Monitoring, Strength and Conditioning, and Data Analytics')

st.header('Resume')
with open("Sports resume.docx", "rb") as file:
    st.download_button(
     "Download Resume",
     file,
        file_name="Sports resume.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        use_container_width=True
)
st.divider()


st.header('Projects')

st.divider()
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader('Athlete Monitoring')
    st.write('This project involved analyzing 4 travel flagged football players and comparing their loads to their position average of each practice period to look closer into when exactly they are taking on too much.')
    with open("Athlete Flagging - Stephanie McClung.zip", "rb") as file:
        st.download_button(
         "Download Project",
         file,
            file_name="Athlete Flagging - Stephanie McClung.zip",
            mime="application/zip",
            use_container_width=True
    )
    with col2:
        st.subheader('Statistical Analysis')
        st.write('A course project that involved importing a specific sports dataset and performing statistical analysis on it to find trends and insights.')
        with open("Simple heatmaps baseball.html", "rb") as file:
            st.download_button(
             "Download Project",
             file,
                file_name="Simple heatmaps baseball.html",
                mime="text/html",
                use_container_width=True
        )
            with col3:
                st.subheader('Analyzing Testing Data')
                st.write('A standard procedure to look over the testing we did on the athletes and check for any sudden changes of force power or asymmetry')
                with open(r"C:\Users\Stephanie McClung\Downloads\DEVO Team 2026- Stephanie McClung.zip", "rb") as file:
                    st.download_button(
                     "Download Project",
                     file,
                        file_name="Devo Team 2026- Stephanie McClung.zip",
                        mime="application/zip",
                        use_container_width=True
                )