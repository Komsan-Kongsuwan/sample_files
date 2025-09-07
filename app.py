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
