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
