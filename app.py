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
    <h2 style='text-align: center; color: #1976d2; margin-bottom: 0.5em;'>View Final Results</h2>
    <div style='text-align: center; margin-bottom: 18px;'>
        <img src='https://cdn.pixabay.com/photo/2014/12/21/23/45/tablets-579355_1280.png' width='140' style='margin:14px; border-radius:8px;' title='Tablet'/>
        <img src='https://cdn.pixabay.com/photo/2017/02/15/12/12/capsule-2060975_1280.png' width='140' style='margin:14px; border-radius:8px;' title='Capsule'/>
    </div>
    <h4 style='text-align: center; color: #444;'>A one-stop solution for MACO, Swab Limit, and Rinse Limit calculations in cleaning validation</h4>
    """,
    unsafe_allow_html=True
)

# ---- Your further app logic goes below ----
st.info("👆 Title, results heading, and tablet/capsule pictures are now shown above. Add your app logic below this block.")
