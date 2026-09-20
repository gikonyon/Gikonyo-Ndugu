import streamlit as st

st.set_page_config(
    page_title="Gikonyo Ndugu | Solutions Provider — Development Finance, ESG & Digital Tools",
    page_icon="🧩",
    layout="wide",
)

# ---------- Sidebar Navigation ----------
st.sidebar.image("Gikonyo.jfif", use_container_width=True)
st.sidebar.title("Gikonyo Ndugu")
st.sidebar.caption("Development Finance, ESG & Digital Solutions")

page = st.sidebar.radio(
    "Navigate",
    [
        "Home",
        "1. Governance & ESG Intelligence",
        "2. Macro-Financial & Risk Analytics",
        "3. Rapid Prototyping & Automation",
        "4. Institutional Strategy & Advisory",
        "Credentials",
        "Contact",
    ],
)

st.sidebar.markdown("---")
st.sidebar.markdown("📍 Nairobi, Kenya")
st.sidebar.markdown("📧 [Ndugu.Gikonyo@hotmail.com](mailto:Ndugu.Gikonyo@hotmail.com)")
st.sidebar.markdown("🔗 [LinkedIn](https://linkedin.com/in/gikonyo-ndugu)")


# ---------- Home ----------
if page == "Home":
    col_img, col_title = st.columns([1, 4])
    with col_img:
        st.image("Gikonyo.jfif", use_container_width=True)
    with col_title:
        st.title("Gikonyo Ndugu")
        st.subheader("I build what I recommend.")

    st.write(
        """
        I sit at the intersection of **development finance, ESG governance, and applied data
        engineering** — 10+ years across the UN system and cooperative banking, with a track
        record of turning strategic problems into working software rather than just slide decks.

        Below is my product suite: four ways I can plug into an institution's problem, each backed
        by real, delivered work — not just a services list.
        """
    )

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("### 1️⃣ Governance & ESG")
        st.caption("Audit-ready ESG & regulatory data integrity")
    with col2:
        st.markdown("### 2️⃣ Macro-Financial Analytics")
        st.caption("Risk models & executive dashboards")
    with col3:
        st.markdown("### 3️⃣ Rapid Prototyping")
        st.caption("Streamlit tools & automation, shipped fast")
    with col4:
        st.markdown("### 4️⃣ Strategy & Advisory")
        st.caption("Boardroom-to-build-team bridging")

    st.markdown("---")
    st.metric("ESG Data Accuracy Boost (UNSOS)", "+31%")
    c1, c2, c3 = st.columns(3)
    c1.metric("Decision Efficiency (Power BI)", "+26%")
    c2.metric("Vehicle-Financing Wait Time Cut", "6 → 3 months")
    c3.metric("Sales Revenue via New Service Line", "+13%")


# ---------- Product 1 ----------
elif page == "1. Governance & ESG Intelligence":
    st.title("1️⃣ Sovereign Governance & ESG Intelligence Engine")
    st.write(
        "**What it is:** Policy, ESG, and regulatory compliance frameworks that audit data "
        "integrity (IFRS S1/S2) and mitigate institutional risk.\n\n"
        "**Value:** Replaces vague sustainability claims with verifiable, audit-ready data "
        "structures for institutions and cooperatives."
    )
    st.markdown("### Proof of work")
    with st.expander("🔎 Uujuzi Forensic ESG & Assurance Engine", expanded=True):
        st.write(
            """
            Python/Streamlit RegTech tool implementing a peer-reviewed forensic algorithm for
            verifying governance and environmental data integrity under IFRS S1/S2. Five-module
            pipeline: Ingestion → Audit/Standards Cross-Reference → Quantitative Reconciliation →
            GIS Spatial Audit → Report Synthesizer, with evidence-tier scoring (Tier 1–4) and
            attribution risk assessment for sustainability claims. Tested against Standard
            Chartered, KCB, and NCBA.
            """
        )
        st.markdown(
            "📄 **Journal Article:** [View Publication on EAJBE](https://journals.eanso.org/index.php/index/search/authors/view?firstName=Gikonyo&middleName=&lastName=Ndugu&affiliation=Independent%20Researcher&country=KE)"
        )
    with st.expander("🌫️ NBO-AirPulse-ESG"):
        st.write(
            "Automated pipeline tracking real-time pollution indicators across Nairobi, "
            "translating environmental data into actionable ESG and sustainability insights."
        )
        st.markdown(
            "🚀 [Launch Live Application](https://nbo-airpulse-esg-giegbbgvbu9eziq8aibd2d.streamlit.app/) | "
            "🐙 [View on GitHub](https://github.com/gikonyo-ndugu/NBO-AirPulse-ESG)"
        )


# ---------- Product 2 ----------
elif page == "2. Macro-Financial & Risk Analytics":
    st.title("2️⃣ Macro-Financial & Risk Analytics Matrix")
    st.write(
        "**What it is:** Macroeconomic forecasting models, liquidity/risk analysis, and "
        "automated financial dashboards (Power BI, Python, SQL).\n\n"
        "**Value:** Converts raw economic and financial data into executive-level decision "
        "matrices."
    )
    st.markdown("### Proof of work")
    with st.expander("📊 UN Support Office Somalia — Power BI Dashboards", expanded=True):
        st.write(
            "Designed and automated Power BI dashboards giving real-time visibility of risk and "
            "performance indicators — lifted management decision-making efficiency by 26% and "
            "ESG-related data accuracy by 31%."
        )
    with st.expander("💳 Stima SACCO Creditworthiness Model"):
        st.write(
            "Pioneered a data-driven creditworthiness model using AI and Big Data to evaluate "
            "member risk, supporting a vehicle-financing pilot that cut wait times from 6 to 3 "
            "months and a repayment/joint-ownership structure for Uber drivers."
        )
    with st.expander("📄 Kenyan Fiscal Decentralization Paper"):
        st.write(
            "Two-phase analytical research on county budget execution across Kenya's devolved "
            "system, delivered as a submission-ready academic paper with 33 verified references."
        )


# ---------- Product 3 ----------
elif page == "3. Rapid Prototyping & Automation":
    st.title("3️⃣ Rapid Prototyping & Automation Suite")
    st.write(
        "**What it is:** End-to-end digital tools, custom Streamlit applications, and workflow "
        "automation built to solve operational bottlenecks.\n\n"
        "**Value:** Delivers lightweight, high-impact software without waiting on lengthy "
        "enterprise IT development cycles."
    )
    st.markdown("### Proof of work")
    with st.expander("🤖 Stima Mshirika Bot", expanded=True):
        st.write(
            "NLTK/Keras neural-network chatbot for Stima SACCO member services, with a "
            "production-ready intents design covering 18 intents and escalation routing to "
            "customer care."
        )
        st.markdown("[View on GitHub](https://github.com/gikonyo-ndugu/stima-mshirika-bot)")
    with st.expander("🇰🇪 Kenya 2060 Framework Dashboard"):
        st.write(
            "Interactive Streamlit dashboard mapping all 47 counties across nine functional "
            "regions of a national industrial co-reliance framework — industrial specializations, "
            "social infrastructure targets, and an ESG/data governance layer."
        )
    with st.expander("🛒 Click N Buy"):
        st.write(
            "Live consumer e-commerce and price-comparison platform for Chinese commodities in "
            "Kenya, with vendor onboarding and a payment settlement framework."
        )
        st.markdown("[Visit clicknbuy.shop](https://clicknbuy.shop)")


# ---------- Product 4 ----------
elif page == "4. Institutional Strategy & Advisory":
    st.title("4️⃣ Institutional Strategy & Advisory Retainer")
    st.write(
        "**What it is:** Strategic advisory covering digital enablement, cooperative-sector "
        "policy development, and cross-functional leadership.\n\n"
        "**Value:** Bridges the gap between executive boardrooms, field operations, and "
        "technical software engineering teams."
    )
    st.markdown("### Proof of work")
    with st.expander("🇰🇪 Kenya 2060 Regional Industrial Co-Reliance Framework", expanded=True):
        st.write(
            "A national economic development framework spanning industrial specialization, "
            "partner-country alignment, social infrastructure targets, and an ESG/data "
            "governance layer — drafted for direct engagement with national policymakers."
        )
    with st.expander("🌍 Somalia Cooperative Finance Initiative (SCSRA/SHERF)"):
        st.write(
            "Proposing a SASRA-equivalent regulatory body for Somalia's Sharia-compliant "
            "cooperative sector, with an active funder and partner network spanning FSD Africa, "
            "ACCOSCA, WOCCU, USAID, and the World Bank/IFAD."
        )
    with st.expander("🏛️ Elected Delegate, Stima SACCO Chamaa Nairobi Zone"):
        st.write(
            "Represents member interests at board level, engaging with SACCO leadership on "
            "strategic and governance matters — direct experience translating field-level "
            "concerns into institutional decisions."
        )


# ---------- Credentials ----------
elif page == "Credentials":
    st.title("Credentials & Background")
    st.markdown("### Experience")
    st.write(
        """
        - **Business Relation Management Assistant** — CTG (UN Support Office Somalia), May 2024–Present
        - **Business Analyst (Delegate, Chamaa Nairobi Zone)** — Stima SACCO, March 2023–Present
        - **Infrastructure Technician** — Trigyn Technologies (UN Support Office Somalia), Apr 2022–May 2024
        - **Business Analyst** — Farmers Basket Kenya, Jul 2016–Oct 2022
        """
    )
    st.markdown("### Education")
    st.write(
        """
        - MSc Development Finance — KCA University, 2024
        - Professional Master's Degree in Visual Analytics & Big Data — TECH Global University, 2024
        - BSc (Hons) Applied Business Computing — University of Sunderland, 2017
        """
    )
    st.markdown("### Tools")
    st.write("Power BI, SQL Server, Python, ETL Tools, Tableau, SAP, Google Cloud, Office 365, Streamlit, Git")


# ---------- Contact ----------
elif page == "Contact":
    st.title("Available for Engagements")
    st.write("I take on consulting retainers, project-based builds, and institutional partnerships.")

    st.markdown("---")

    col_photo, col_details, col_qr = st.columns([1.2, 2.5, 1.3])

    with col_photo:
        st.image("Gikonyo.jfif", use_container_width=True)

    with col_details:
        st.markdown("### **Gikonyo Ndugu**")
        st.markdown("**Solutions Provider — Development Finance, ESG & Digital Tools**")
        st.markdown("📍 Nairobi, Kenya")
        st.markdown("📧 [Ndugu.Gikonyo@hotmail.com](mailto:Ndugu.Gikonyo@hotmail.com)")
        st.markdown("📱 [+254 723 462 232](tel:+254723462232)")
        st.markdown("🔗 [linkedin.com/in/gikonyo-ndugu](https://linkedin.com/in/gikonyo-ndugu)")

    with col_qr:
        st.image("QR CODE GIKONYO.jpg", use_container_width=True, caption="Scan for Live Portfolio")

    st.markdown("---")
