import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="MACO Calculation App By Gopal Mandloi", layout="wide")

# --- SUPER ATTRACTIVE MODERN HEADER ---
st.markdown(
    """
    <div style="
        margin: 0 auto 36px auto; 
        padding: 28px 2vw 18px 2vw;
        max-width: 900px;
        background: linear-gradient(90deg, #FFF8E1 65%, #E3F2FD 100%);
        border-radius: 22px; 
        box-shadow: 0 8px 36px #ffe0b270, 0 2px 8px #90caf9b0;
        border: 2.5px solid #ffd54f;
        position: relative;
        overflow: hidden;
    ">
        <img src="https://cdn-icons-png.flaticon.com/512/2910/2910829.png" 
             style="position:absolute;left:24px;top:24px;width:64px;height:64px;opacity:0.13;z-index:0;" />
        <img src="https://cdn-icons-png.flaticon.com/512/1828/1828884.png"
             style="position:absolute;right:24px;bottom:20px;width:60px;height:60px;opacity:0.12;z-index:0;" />
        <div style="position:relative;z-index:1;">
        <h1 style='
            text-align: center;
            color: #1565c0;
            font-family: Segoe UI, Arial, sans-serif;
            font-size: 2.8rem;
            margin-bottom: 0.25em;
            letter-spacing: 2px;
            font-weight: 800;
            text-shadow: 2px 6px 18px #bbdefb, 0 2px 1px #fffde7;
        '>
            <span>🌟 MACO Calculation App</span> <br>
            <span style="font-size:1.1rem; color:#d84315; font-weight:600; font-style:italic;">
                By Gopal Mandloi
            </span>
        </h1>
        <h3 style='
            text-align: center;
            color: #388e3c;
            font-weight: 700;
            font-family: Segoe UI, Arial, sans-serif;
            margin-top:0;
            font-size: 1.35rem;
            letter-spacing: 1px;
            text-shadow: 0 1px 8px #c8e6c9;
        '>
            🚀 <span style="color:#1565c0;font-weight:700;">A one-stop solution for 
            <span style="background:#fffde7;padding:0 6px;border-radius:6px;">MACO</span>, 
            <span style="color:#ffa000;background:#fff;padding:0 6px;border-radius:6px;">Swab Limit</span>, and 
            <span style="color:#8e24aa;background:#ede7f6;padding:0 6px;border-radius:6px;">Rinse Limit</span>
            calculations in cleaning validation</span> 🚀
        </h3>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# The rest of your Streamlit app code continues below...
