import streamlit as st

st.set_page_config(page_title="Sprint42 Valuation", layout="wide")

st.title("💼 Sprint42 Valuation System")
st.caption("Founder-first clarity for beauty & wellness brands preparing for investment or acquisition.")

# Sidebar navigation
module = st.sidebar.selectbox("📦 Choose Module", [
    "Discovery & Scope",
    "Financial Deep Dive",
    "Valuation Logic",
    "Strategic Brief",
    "Presentation Layer"
])

# Module 1: Discovery
if module == "Discovery & Scope":
    st.header("🧠 Module 1: Discovery & Scope Alignment")
