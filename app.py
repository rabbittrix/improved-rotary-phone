import streamlit as st
import requests
from ghosttrack_wrapper import run_ip_lookup, run_phone_lookup, run_username_lookup

# Page configuration
st.set_page_config(page_title="GhostTrack Dashboard", layout="centered", page_icon="🕵️‍♂️")

# Custom CSS Styling
st.markdown("""
<style>
body {
    background-color: #111;
    color: white;
}
input[type="text"] {
    background-color: #222;
    color: #0f0;
    border: 1px solid #0f0;
    padding: 8px;
}
.stTextInput input {
    font-family: monospace;
}
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("🕵️‍♂️ GhostTrack")
option = st.sidebar.selectbox("Choose a tracker", [
    "Show My IP",
    "IP Tracker",
    "Phone Tracker",
    "Username Tracker",
    "Clean Dashboard"
])

# Helper function to mask input (visually only)
def masked_input(label):
    return st.text_input(label, type="password", placeholder="••••••••")


# --- MAIN LOGIC ---
if option == "IP Tracker":
    st.subheader("🌐 Enter IP Address to Track")
    ip = masked_input("IP Address:")
    if ip:
        with st.spinner("🔍 Looking up IP information..."):
            result = run_ip_lookup(ip)
            st.markdown("### 🧾 IP Information")
            st.json(result)

elif option == "Show My IP":
    st.subheader("📍 Your Public IP Address")
    try:
        res = requests.get("https://api.ipify.org?format=json", timeout=5)
        my_ip = res.json()['ip']
        st.code(my_ip)
    except Exception as e:
        st.error(f"⚠️ Could not retrieve public IP: {e}")

elif option == "Phone Tracker":
    st.subheader("📞 Phone Number Lookup")
    phone = masked_input("Phone Number (e.g. +628123456789):")
    if phone:
        with st.spinner("🔍 Looking up phone number..."):
            result = run_phone_lookup(phone)
            st.markdown("### 🧾 Phone Information") 
            st.json(result)

elif option == "Username Tracker":
    st.subheader("👤 Username Search")
    username = masked_input("Username to search:")
    if username:
        with st.spinner("🔍 Searching social media platforms..."):
            result = run_username_lookup(username)
            st.markdown("### 🧾 Username Results")
            st.json(result)

elif option == "Clean Dashboard":
    st.markdown("""
    ## 🧹 Dashboard Cleaned!

    Select a tracker from the **sidebar** to begin.
    """)
    st.image("https://via.placeholder.com/800x300.png?text=GhostTrack+Ready", use_container_width=True)

# Footer 
# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center;'>"
    "Built with ❤️ using "
    "<a href='https://github.com/HunxByts/GhostTrack'  target='_blank'>GhostTrack</a> + Streamlit"
    "</p>",
    unsafe_allow_html=True
)