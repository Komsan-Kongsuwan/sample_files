import streamlit as st

with open("fake_380_materials_real.csv", "rb") as file:
    st.download_button(
        label="📥 Download 380 Materials (CSV)",
        data=file,
        file_name="fake_380_materials_real.csv",
        mime="text/csv",
    )
