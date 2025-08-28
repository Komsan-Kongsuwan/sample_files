import streamlit as st
st.write("Download link for sample files")
with open("Profit and Loss - sample.xlsx", "rb") as file:
    st.download_button(
        label="📥 Profit and Loss - sample",
        data=file,
        file_name="Profit and Loss - sample.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

with open("Simulation Selective Rack - sample.xlsx", "rb") as file:
    st.download_button(
        label="📥 Simulation Selective Rack - sample",
        data=file,
        file_name="Simulation Selective Rack - sample.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

with open("WH space mapping - sample.xlsx", "rb") as file:
    st.download_button(
        label="📥 WH space mapping - sample",
        data=file,
        file_name="WH space mapping - sample.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

with open("In-Out-Stock-History-sample.xlsx", "rb") as file:
    st.download_button(
        label="📥 In-Out-Stock-History-sample",
        data=file,
        file_name="In-Out-Stock-History-sample.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

with open("Monthly Customer Revenue - sample.xlsx", "rb") as file:
    st.download_button(
        label="📥 Monthly Customer Revenue - sample",
        data=file,
        file_name="Monthly Customer Revenue - sample.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
