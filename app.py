import streamlit as st

# --- Page CSS ---
st.markdown("""
    <style>
        .block-container {padding: 1.5rem 1rem 0 1rem;}
        section[data-testid="stSidebar"] div.stButton > button {
            font-size: 12px !important; padding: 0.1rem 0.25rem !important;
            min-height: 40px !important; border-radius: 6px !important; line-height:1.2;
        }
        section[data-testid="stSidebar"] div.stButton p { font-size: 12px !important; margin:0 !important; }
        [data-testid="stMetric"] { padding: 0.25rem 0.5rem; min-height: 60px; margin:0 !important;}
        [data-testid="stMetricLabel"] { font-size: 14px !important; font-weight: 600 !important; color: #333333; }
        [data-testid="stMetricValue"] { font-size: 16px !important; font-weight: 700 !important; color: #0055aa; }
        div.block-container > div {margin-bottom: 0rem !important;}
    </style>
""", unsafe_allow_html=True)

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

with open("Warehouse 3D Design - sample.png", "rb") as file:
    st.download_button(
        label="📥 Download Warehouse 3D Design - sample",
        data=file,
        file_name="Warehouse 3D Design - sample.png",
        mime="image/png"
    )

