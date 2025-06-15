import streamlit as st

st.set_page_config(page_title="MACO Calculation App By Gopal Mandloi", layout="wide")

st.markdown(
    """
    <h1 style="
        text-align: center;
        font-weight: bold;
        letter-spacing:2px;
        margin-bottom: 10px;
        font-size: 3em;
        background: linear-gradient(90deg, #47c6ff 10%, #60aaff 30%, #a084ee 60%, #ff6495 80%, #ff3838 100%);
        background-clip: text;
        -webkit-background-clip: text;
        color: transparent;
        -webkit-text-fill-color: transparent;
        ">
        MACO Calculation App By Gopal Mandloi
    </h1>
    <div style='text-align: center; margin-bottom: 16px;'>
        <img src='https://images.unsplash.com/photo-1515378791036-0648a3ef77b2?auto=format&fit=facearea&w=800&h=200&q=80' width='180' style='margin:10px; border-radius:12px;'/>
        <img src='https://images.unsplash.com/photo-1505751172876-fa1923c5c528?auto=format&fit=facearea&w=800&h=200&q=80' width='180' style='margin:10px; border-radius:12px;'/>
        <img src='https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=facearea&w=800&h=200&q=80' width='180' style='margin:10px; border-radius:12px;'/>
    </div>
    <h4 style='text-align: center; color: #444;'>A one-stop solution for MACO, Swab Limit, and Rinse Limit calculations in cleaning validation</h4>
    """,
    unsafe_allow_html=True
)

# ----- The rest of your app code goes here -----
# For demonstration, here's a message:
st.info("👆 Above section includes a colorful gradient app title and your three images. Add your app logic/code below this block.")
