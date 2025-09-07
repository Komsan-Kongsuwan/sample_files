import streamlit as st

# Page config
st.set_page_config(page_title="Warehouse Dashboard Solutions", layout="centered")

# Hero Section
st.title("📦 Turn Warehouse Data into Profit")
st.subheader("Dashboards built by a logistics insider — not just another IT team.")
st.markdown("Real-time insights into inventory movement, cost, and profitability.")
st.button("Request a Free Demo")
st.button("Explore Dashboard Samples")

# Problem Section
st.markdown("---")
st.header("❌ Are You Struggling to Make Decisions from Scattered Reports?")
st.markdown("""
- Inventory data spread across multiple Excel files and systems  
- No clear view of cost per SKU or storage efficiency  
- Limited visibility into product movement and aging stock  
- Manual reporting that takes hours and still misses key insights  
- Difficulty tracking profitability across clients or warehouse zones  
""")

# Solution Section
st.markdown("---")
st.header("✅ Dashboards That Speak Your Language")
st.markdown("""
Built for warehouse managers, not just IT teams:
- Visualize inbound/outbound transactions, stock aging, and turnover  
- Monitor cost per unit, storage days, and labor productivity  
- Export multi-sheet Excel reports with clean, column-based views  
- Filter by client, SKU, warehouse zone, or time period  
- Powered by Python and pandas for speed, accuracy, and flexibility  
""")

# Dashboard Preview
st.markdown("---")
st.header("📊 See What You’ll Get")
st.markdown("""
Interactive dashboards tailored to your operations:
- Inventory accuracy and movement  
- Profit & loss by client or zone  
- Monthly trends and performance KPIs  
""")
st.button("View Live Demo")
st.button("Download Sample Report")

# About Section
st.markdown("---")
st.header("👤 Built by Someone Who’s Been in Your Shoes")
st.markdown("""
I'm a former 3PL warehouse manager with hands-on experience in inventory control, client operations, and cost analysis.  
Now I build data-driven dashboards that help warehouse teams make faster, smarter decisions — without needing a technical background.
""")

# Call to Action
st.markdown("---")
st.header("🚀 Ready to See Your Warehouse in a Whole New Light?")
st.button("Request a Free Consultation")
st.button("Try It With Your Own Data")

# Footer
st.markdown("---")
st.caption("© 2025 Warehouse Dashboard Solutions | Built with Streamlit")




"""
import streamlit as st

st.markdown("<h2 style='text-align:left; font-size:28px;'>Sample files for viewing, click for download.</h2>", unsafe_allow_html=True)

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

st.write("*These files generated from mockup data.")
st.write("")
st.write("")


subject = "Feedback from Streamlit app"
body = "Hello Komsan,%0A%0AI would like to share my comment:%0A"

st.markdown(
    f"""
    <div style="background-color:#1E90FF; padding:10px; border-radius:8px;">
        <p style="color:white; font-size:16px;">
            Thank you for your interesting, if you have any comment, please feel free to send me your comment to: 
            <a href="mailto:komsan.kongsuwan@gmail.com?subject={subject}&body={body}" style="color:white; font-weight:bold; text-decoration:underline;">
                komsan.kongsuwan@gmail.com
            </a>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
"""
