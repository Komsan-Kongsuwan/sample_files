import streamlit as st

# Page config
st.set_page_config(page_title="Warehouse Dashboard Solutions", layout="centered")

# Inject custom CSS for card styling
st.markdown("""
    <style>
        .card {
            background-color: #f9f9f9;
            padding: 25px;
            margin: 20px 0;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        .card h2 {
            color: #333;
        }
        .card p {
            color: #555;
        }
        .card ul {
            padding-left: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Card: Hero Section
st.markdown("""
<div class="card">
    <h2>📦 Turn Warehouse Data into Profit</h2>
    <p>Dashboards built by a logistics insider — not just another IT team.</p>
    <p>Real-time insights into inventory movement, cost, and profitability.</p>
</div>
""", unsafe_allow_html=True)
st.button("Request a Free Demo")
st.button("Explore Dashboard Samples")

# Card: Problem Section
st.markdown("""
<div class="card">
    <h2>❌ Are You Struggling to Make Decisions from Scattered Reports?</h2>
    <ul>
        <li>Inventory data spread across multiple Excel files and systems</li>
        <li>No clear view of cost per SKU or storage efficiency</li>
        <li>Limited visibility into product movement and aging stock</li>
        <li>Manual reporting that takes hours and still misses key insights</li>
        <li>Difficulty tracking profitability across clients or warehouse zones</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Card: Solution Section
st.markdown("""
<div class="card">
    <h2>✅ Dashboards That Speak Your Language</h2>
    <p>Built for warehouse managers, not just IT teams:</p>
    <ul>
        <li>Visualize inbound/outbound transactions, stock aging, and turnover</li>
        <li>Monitor cost per unit, storage days, and labor productivity</li>
        <li>Export multi-sheet Excel reports with clean, column-based views</li>
        <li>Filter by client, SKU, warehouse zone, or time period</li>
        <li>Powered by Python and pandas for speed, accuracy, and flexibility</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Card: Dashboard Preview
st.markdown("""
<div class="card">
    <h2>📊 See What You’ll Get</h2>
    <ul>
        <li>Inventory accuracy and movement</li>
        <li>Profit & loss by client or zone</li>
        <li>Monthly trends and performance KPIs</li>
    </ul>
</div>
""", unsafe_allow_html=True)
st.button("View Live Demo")
st.button("Download Sample Report")

# Card: About Section
st.markdown("""
<div class="card">
    <h2>👤 Built by Someone Who’s Been in Your Shoes</h2>
    <p>I'm a former 3PL warehouse manager with hands-on experience in inventory control, client operations, and cost analysis.</p>
    <p>Now I build data-driven dashboards that help warehouse teams make faster, smarter decisions — without needing a technical background.</p>
</div>
""", unsafe_allow_html=True)

# Card: Call to Action
st.markdown("""
<div class="card">
    <h2>🚀 Ready to See Your Warehouse in a Whole New Light?</h2>
</div>
""", unsafe_allow_html=True)
st.button("Request a Free Consultation")
st.button("Try It With Your Own Data")

# Footer
st.markdown("---")
st.caption("© 2025 Warehouse Dashboard Solutions | Built with Streamlit")
