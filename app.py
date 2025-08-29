import streamlit as st

st.markdown("<h2 style='text-align:left; font-size:28px;'>Download link as below</h2>", unsafe_allow_html=True)

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

with open("Warehouse 3D Design - sample.png", "rb") as file:
    st.download_button(
        label="📥 Download Warehouse 3D Design - sample",
        data=file,
        file_name="Warehouse 3D Design - sample.png",
        mime="image/png"
    )

st.write("*These files generated from mockup data")
st.write("If you have any comment, please feel free to send me your comment to komsan.kongsuwan@gmail.com")
