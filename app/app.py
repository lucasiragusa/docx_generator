import streamlit as st
from datetime import date

st.set_page_config(
    page_title="Landing Permit Generator",
    page_icon=":airplane:",
    layout="wide",
    initial_sidebar_state="expanded",
)

def main():
    st.sidebar.title("Choose a page")
    page = st.sidebar.radio("", ["New SSIM", "SSIM Compare"])

    if page == "New SSIM":
        new_ssim_page()
    else:
        ssim_compare_page()

def new_ssim_page():
    st.title("Generate Landing Permit Applications from New SSIM")
    st.write("Upload a new SSIM file to generate landing permit applications.")
    uploaded_ssim = st.file_uploader("Upload SSIM file", type="ssim")
    if uploaded_ssim:
        if not uploaded_ssim.name.endswith(".ssim"):
            st.error("Please upload a valid SSIM file.")
        else:
            st.success(f"Uploaded {uploaded_ssim.name}")

    st.button("Generate")

def ssim_compare_page():
    st.title("Generate Landing Permit Application from SSIM Compare")
    st.write("Upload two SSIM files to generate landing permit applications by comparing them.")
    base_ssim = st.file_uploader("Upload Base SSIM file", type="ssim")
    alt_ssim = st.file_uploader("Upload Alt SSIM file", type="ssim")

    start_date = st.date_input("Start date", value=date.today())
    end_date = st.date_input("End date", value=date.today())

    if end_date < start_date:
        st.error("End date should be greater than or equal to the start date.")
    else:
        st.success(f"Selected date range: {start_date} to {end_date}")

    service_type = st.multiselect("Service type", ["A", "B", "C"])
    country = st.multiselect("Country", ["Country 1", "Country 2", "Country 3"])

    st.button("Generate")

if __name__ == "__main__":
    main()
