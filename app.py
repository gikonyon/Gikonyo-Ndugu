import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="CIC Asset Management | BD Analytics Suite",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM BRANDING CSS ---
st.markdown("""
    <style>
    .main-header {
        color: #B81C24;
        font-size: 26px;
        font-weight: 700;
        margin-bottom: 2px;
    }
    .sub-header {
        color: #475569;
        font-size: 14px;
        margin-bottom: 20px;
    }
    .metric-card {
        background-color: #FFFFFF;
        border-left: 5px solid #B81C24;
        padding: 15px;
        border-radius: 6px;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_dict=True)

# --- HEADER SECTION ---
st.markdown('<p class="main-header">CIC ASSET MANAGEMENT (CICAM)</p>', unsafe_allow_dict=True)
st.markdown('<p class="sub-header">Business Development & Institutional Client Engagement Engine | Prepared for James Njagi</p>', unsafe_allow_dict=True)
st.divider()

# --- SIDEBAR FILTERS ---
st.sidebar.header("🎯 Target Product & Portfolio")
selected_fund = st.sidebar.selectbox(
    "Select Investment Vehicle",
    [
        "CIC Money Market Fund (MMF)",
        "CIC Wealth Fund",
        "CIC Fixed Income Fund",
        "CIC Dollar Fund",
        "Institutional Pension Scheme"
    ]
)

investment_horizon = st.sidebar.slider("Investment Horizon (Years)", 1, 10, 5)
initial_capital = st.sidebar.number_input("Proposed Initial Allocation (KES)", min_value=100000, value=25000000, step=1000000)

# Product Yield Benchmark Mapping
fund_yields = {
    "CIC Money Market Fund (MMF)": 0.135,
    "CIC Wealth Fund": 0.148,
    "CIC Fixed Income Fund": 0.152,
    "CIC Dollar Fund": 0.065,
    "Institutional Pension Scheme": 0.128
}

current_rate = fund_yields[selected_fund]

# --- TOP METRIC CARDS ---
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown('<div class="metric-card">', unsafe_allow_dict=True)
    st.metric("Effective Gross Yield", f"{current_rate*100:.2f}%", "+0.45% vs Industry")
    st.markdown('</div>', unsafe_allow_dict=True)

with c2:
    st.markdown('<div class="metric-card">', unsafe_allow_dict=True)
    st.metric("CICAM CIS Market Share", "13.50%", "Rank #1 Market Leader")
    st.markdown('</div>', unsafe_allow_dict=True)

with c3:
    st.markdown('<div class="metric-card">', unsafe_allow_dict=True)
    st.metric("Total Group AUM", "KES 194.0 B", "+11.2% YOY Growth")
    st.markdown('</div>', unsafe_allow_dict=True)

with c4:
    st.markdown('<div class="metric-card">', unsafe_allow_dict=True)
    projected_val = initial_capital * ((1 + current_rate) ** investment_horizon)
    st.metric(f"Projected {investment_horizon}-Yr Value", f"KES {projected_val/1e6:,.1f} M")
    st.markdown('</div>', unsafe_allow_dict=True)

st.markdown("<br>", unsafe_allow_dict=True)

# --- WORKFLOW TABS ---
tab1, tab2, tab3 = st.tabs(["📊 Yield Performance & Projections", "🤝 SACCO & Channel Growth", "📄 Executive Pitch Briefing"])

with tab1:
    st.subheader("Asset Growth & Compounding Trajectory")
    
    months = np.arange(1, (investment_horizon * 12) + 1)
    monthly_rate = (1 + current_rate) ** (1/12) - 1
    compound_values = initial_capital * ((1 + monthly_rate) ** months)
    
    df_chart = pd.DataFrame({
        "Month": months,
        "Projected Portfolio Value": compound_values,
        "Principal Capital": initial_capital
    })
    
    fig_comp = px.line(
        df_chart,
        x="Month",
        y=["Projected Portfolio Value", "Principal Capital"],
        labels={"value": "Value (KES)", "variable": "Portfolio Strategy"},
        title=f"Yield Growth Modeling over {investment_horizon} Years ({selected_fund})",
        color_discrete_sequence=["#B81C24", "#64748B"]
    )
    fig_comp.update_layout(template="plotly_white")
    st.plotly_chart(fig_comp, use_container_width=True)

with tab2:
    st.subheader("Distribution Channels & SACCO Pipeline")
    
    df_channels = pd.DataFrame({
        "Distribution Channel": ["Tier-1 SACCOs", "Agri-Cooperative Societies", "Corporate Pension Schemes", "High-Net-Worth Individuals", "Direct Retail"],
        "AUM Contribution (KES B)": [45.2, 28.4, 62.1, 38.0, 20.3],
        "YOY Growth (%)": [14.2, 18.5, 8.7, 12.1, 22.0]
    })
    
    col_g1, col_g2 = st.columns([3, 2])
    with col_g1:
        fig_bar = px.bar(
            df_channels,
            x="Distribution Channel",
            y="AUM Contribution (KES B)",
            color="YOY Growth (%)",
            title="AUM Breakdown Across Key Business Development Channels",
            color_continuous_scale="Reds"
        )
        st.plotly_chart(fig_bar, use_container_width=True)
    
    with col_g2:
        st.write("### Channel Metrics")
        st.dataframe(df_channels, hide_index=True, use_container_width=True)

with tab3:
    st.subheader("Generate Tailored Pitch Summary")
    
    client_name = st.text_input("Target Institution Name", "Stima SACCO / Corporate Client")
    proposed_allocation_pct = st.slider("Target Allocation to CICAM (%)", 10, 100, 50)
    
    if st.button("Generate Proposal Pitch Summary"):
        allocated_capital = (proposed_allocation_pct / 100.0) * initial_capital
        st.success(f"Proposal generated for **{client_name}**")
        st.code(f"""
======================================================================
EXECUTIVE PITCH BRIEFING: INSTITUTIONAL ASSET MANAGEMENT
Target Client: {client_name}
Selected Strategy: {selected_fund}
Total Portfolio Commitment: KES {initial_capital:,.2f}
Proposed CICAM Allocation ({proposed_allocation_pct}%): KES {allocated_capital:,.2f}

STRATEGIC HIGHLIGHTS FOR BD ENGAGEMENT:
1. Capital Preservation & Security: Underlying assets secured by top-tier Treasury instruments and bank deposits.
2. Yield Alpha: Yield benchmarked at {current_rate*100:.2f}% p.a. delivering competitive risk-adjusted returns.
3. Liquidity Support: Seamless withdrawal workflows and integration via M-Pesa Paybill 600118 and RTGS.
======================================================================
        """, language="text")

st.caption("CIC Asset Management Business Development Analytics Prototype | Ready for Streamlit Cloud")
