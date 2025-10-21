import streamlit as st

st.set_page_config(page_title="Sprint42 Valuation", layout="wide")

st.title("💼 Sprint42 Valuation System")
st.caption("Founder-first clarity for beauty & wellness brands preparing for investment or acquisition.")

# Sidebar navigation
module = st.sidebar.radio("📦 Choose Module", [
    "Discovery & Scope",
    "Financial Deep Dive",
    "Valuation Logic",
    "Strategic Brief",
    "Presentation Layer"
])

# Module 1: Discovery
if module == "Discovery & Scope":
    st.header("🧠 Module 1: Discovery & Scope Alignment")
    brand_name = st.text_input("Brand Name")
    model_type = st.selectbox("Business Model", ["Product", "Service", "Hybrid"])
    revenue = st.number_input("Annual Revenue ($M)", min_value=0.0, step=0.1)
    objective = st.text_area("Valuation Objective (e.g. acquisition, investment, strategic planning)")
    st.markdown("💬 *“We start with clarity—what’s the story, who’s the buyer, and what’s the goal.”*")

# Module 2: Financial Deep Dive
elif module == "Financial Deep Dive":
    st.header("📊 Module 2: Financial Normalization")
    reported_income = st.number_input("Reported Net Income ($M)", min_value=0.0, step=0.1)
    adjusted_income = st.number_input("Adjusted Net Income ($M)", min_value=0.0, step=0.1)
    sde = st.number_input("Normalized SDE ($M)", min_value=0.0, step=0.1)
    adjustments = st.text_area("Adjustments Applied (e.g. owner salary, one-time fees, travel)")
    st.markdown("💬 *“We don’t just clean the numbers—we decode them.”*")

# Module 3: Valuation Logic
elif module == "Valuation Logic":
    st.header("📐 Module 3: Valuation Methodology")
    method = st.selectbox("Valuation Method", ["SDE", "EBITDA"])
    normalized_earnings = st.number_input("Normalized Earnings ($M)", min_value=0.0, step=0.1)
    multiple_low = st.slider("Industry Multiple (Low)", 1.0, 5.0, 2.5)
    multiple_high = st.slider("Industry Multiple (High)", multiple_low, 6.0, 3.5)

    valuation_low = normalized_earnings * multiple_low
    valuation_high = normalized_earnings * multiple_high

    st.subheader("💰 Valuation Range")
    st.success(f"${valuation_low:.2f}M – ${valuation_high:.2f}M")

    st.markdown("💬 *“Valuation is a negotiation tool, not a math problem.”*")

# Module 4: Strategic Brief
elif module == "Strategic Brief":
    st.header("🧠 Module 4: Strategic Positioning")
    margin_strength = st.text_input("Margin Strength (e.g. 62% gross margin from proprietary product line)")
    scalability = st.text_input("Scalability Potential (e.g. franchising, licensing, DTC expansion)")
    buyer_profile = st.text_input("Ideal Buyer Profile")
    exit_narrative = st.text_area("Exit Narrative")
    st.markdown("💬 *“We frame the narrative founders will pitch and investors will believe.”*")

# Module 5: Presentation Layer
elif module == "Presentation Layer":
    st.header("🎙️ Module 5: Presentation & Delivery")
    st.file_uploader("Upload Loom Walkthrough (optional)")
    founder_summary = st.text_area("Founder Summary (for async delivery or investor handoff)")
    st.markdown("💬 *“We make valuation founder-first—clear, kinetic, and pitch-ready.”*")

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("Built by **Ken** | MBBB & UK Hospitality Partners")

