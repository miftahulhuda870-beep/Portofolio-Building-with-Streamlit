import streamlit as st
import pandas as pd
import numpy as np 
import pickle
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import seaborn as sns


st.set_page_config(
    page_title="Assignment Portofolio Building with Streamlit",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Membuat fungsi Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("Data/Telco_customer_churn.csv")

# Load data
df_telco = load_data()

# Sidebar
st.sidebar.header("Pengaturan & Navigasi")

pilihan_halaman = st.sidebar.radio(
    "Pilih Halaman:",
    ("Profil", "Visualisasi")
)

if pilihan_halaman == "Profil":
    st.title("About Us")
    st.markdown("*Info Dataset*")

    st.write("Dataset ini berisi informasi sekitar 7.043 pelanggan dengan 21 fitur")
    st.image("assets/cust.jpg")

    st.write("Fitur-fitur ini dibagi menjadi beberapa kategori utama:")
    st.markdown("""
        *  Informasi Demografis
            * Gender
            * Senior Citizen
            * Partner & Dependents
        * Informasi Layanan (Services)
            * Phone Service & Multiple Lines
            * Internet Service
            * Security
        * Informasi Akun Pelanggan
            * Tenure
            * Contract
            * Paperless Billing
            * Payment Method
            * Monthly Charges
            * Total Charges   
    """)

elif pilihan_halaman == "Visualisasi":
    st.title("Visualisasi Dataset")
    st.markdown("---")

    st.header("Churn Distribution")
    st.markdown("")
    fig = px.histogram(
    df_telco,
    x="Churn Label",
    color="Churn Value",
    title="Distribusi Churn Customer")
    st.plotly_chart(fig, use_container_width=True)

    st.header("Churn vs Contract")
    st.markdown("")
    fig = px.histogram(
    df_telco,
    x="Contract",
    color="Churn Value",
    barmode="group",
    title="Churn berdasarkan Contract")
    st.plotly_chart(fig, use_container_width=True)

    st.header("Tenure vs Churn")
    st.markdown("")
    fig = px.box(
    df_telco,
    x="Churn Value",
    y="Tenure Months",
    title="Tenure vs Churn")
    st.plotly_chart(fig, use_container_width=True)


    

