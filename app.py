import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="MACO Calculation App By Gopal Mandloi", layout="wide")

# ------- TOP BANNER -------
st.markdown(
    """
    <div style="max-width:900px;margin:0 auto 28px auto;padding:0 2vw;">
        <h1 style="
            text-align:center;
            color:#1565c0;
            font-size:2.7rem;
            font-family:Segoe UI,Arial,sans-serif;
            font-weight:900;
            letter-spacing:1.5px;
            margin-bottom:0.2em;
            text-shadow: 1px 2px 12px #bbdefb;
        ">
            🌟 MACO Calculation App
        </h1>
        <div style="text-align:center;margin-bottom:0.3em;">
            <span style="font-size:1.2em; color:#d84315; font-weight:600; font-style:italic;">
                By Gopal Mandloi
            </span>
        </div>
        <div style="
            text-align:center;
            color:#388e3c;
            font-weight:600;
            font-size:1.21rem;
            font-family:Segoe UI,Arial,sans-serif;
            margin-bottom:1.15em;
            text-shadow: 0 1px 8px #c8e6c9;
        ">
            🚀 A one-stop solution for <b style="color:#1565c0;">MACO</b>, <b style="color:#ffa000;">Swab Limit</b>, and <b style="color:#8e24aa;">Rinse Limit</b> calculations in cleaning validation,<br>
            with automatic identification of <span style="color:#d84315;font-weight:700;">Previous Worst Case</span> and <span style="color:#d84315;font-weight:700;">Next Worst Case</span> products.
        </div>
        <div style="
            background: linear-gradient(90deg,#fff3e0 60%,#e3f2fd 100%);
            border-left: 5px solid #1976d2;
            border-radius: 9px;
            padding: 13px 18px 13px 26px;
            color: #444;
            font-size: 1.09em;
            font-family: Segoe UI, Arial, sans-serif;
            box-shadow: 0 2px 14px #cfd8dc36;
            margin-bottom: 0.5em;
            max-width:750px;
            margin-left:auto;
            margin-right:auto;
        ">
            <b>Message from Gopal Mandloi:</b> This app is shared to help the pharma professional community and ultimately save patient lives by ensuring correct MACO assessments.<br>
            <span style="color:#d84315;font-weight:600;">This tool is completely free of cost</span> — if anyone asks you for money or favors to use this app, please <b>inform me directly</b>.<br>
            Please use this app responsibly and do not misuse it.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------- APP LOGIC (upload, download, calculations, results) ----------
mode = st.radio(
    "How do you want to provide data?",
    ("Use example files", "Upload my own files")
)

example_files = {
    "Product Details": "product_details.xlsx",
    "Analytical Method Validation": "analytical_method_validation.xlsx",
    "Solubility & Cleaning": "solubility_cleaning.xlsx",
    "Equipment Details": "equipment_details.xlsx",
    "Rating Criteria (4 sheets)": "rating_criteria.xlsx"
}

if mode == "Upload my own files":
    uploaded_details = st.file_uploader("Product Details", type=["xlsx"])
    uploaded_amv = st.file_uploader("Analytical Method Validation", type=["xlsx"])
    uploaded_solclean = st.file_uploader("Solubility & Cleaning", type=["xlsx"])
    uploaded_equips = st.file_uploader("Equipment Details", type=["xlsx"])
    uploaded_criteria = st.file_uploader("Rating Criteria (4 sheets)", type=["xlsx"])
else:
    uploaded_details = example_files["Product Details"]
    uploaded_amv = example_files["Analytical Method Validation"]
    uploaded_solclean = example_files["Solubility & Cleaning"]
    uploaded_equips = example_files["Equipment Details"]
    uploaded_criteria = example_files["Rating Criteria (4 sheets)"]

st.markdown("### Download Sample (Filled) Templates")
if mode == "Use example files":
    def file_download_button(filepath, button_label):
        try:
            if os.path.exists(filepath):
                with open(filepath, "rb") as f:
                    data = f.read()
                st.download_button(
                    label=button_label,
                    data=data,
                    file_name=os.path.basename(filepath),
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
            else:
                st.warning(f"File not found: {filepath}")
        except Exception as e:
            st.warning(f"Cannot access file: {filepath}. Error: {e}")

    file_download_button(example_files["Product Details"], "Download Product Details (filled, .xlsx)")
    file_download_button(example_files["Analytical Method Validation"], "Download Analytical Method Validation (filled, .xlsx)")
    file_download_button(example_files["Solubility & Cleaning"], "Download Solubility & Cleaning (filled, .xlsx)")
    file_download_button(example_files["Equipment Details"], "Download Equipment Details (filled, .xlsx)")
    file_download_button(example_files["Rating Criteria (4 sheets)"], "Download Rating Criteria (filled, .xlsx)")
else:
    st.info("Use your own files above. Sample templates are only available in 'Use example files' mode.")

st.markdown("""
**How to use this App (Procedure):**

1. **Download Sample Templates** (button above)
2. **Edit your data** in the sample templates (do not change column names or sheet names)
3. **Upload your own Excel files above**
4. **Click any result button below** to see your calculation results!

:warning: **If you use your own files, make sure column names and sheet names match the templates.**
""")

def read_excel_or_none(f, **kwargs):
    try:
        return pd.read_excel(f, **kwargs)
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None

files_ready = all([uploaded_details, uploaded_amv, uploaded_solclean, uploaded_equips, uploaded_criteria])

if files_ready:
    df = read_excel_or_none(uploaded_details)
    df_equip = read_excel_or_none(uploaded_equips)
    templates = None
    try:
        templates = pd.read_excel(uploaded_criteria, sheet_name=None)
    except Exception as e:
        st.error(f"Error loading Rating Criteria: {e}")

    if any(x is None for x in [df, df_equip, templates]):
        st.stop()

    solubility_template = templates['Solubility']
    dose_template = templates['Dose']
    toxicity_template = templates['Toxicity']
    cleaning_template = templates['Cleaning']

    def assign_solubility_group(sol, template):
        if pd.isna(sol): return None
        sol = str(sol).strip().lower()
        for _, row in template.iterrows():
            desc = str(row['Description']).strip().lower()
            if sol == desc:
                return row['Group']
        return None
    def assign_range_group(value, template):
        try: value = float(value)
        except: return None
        for _, row in template.iterrows():
            if row['Min'] <= value <= row['Max']:
                return row['Group']
        return None
    def assign_cleaning_group(val, template):
        if pd.isna(val): return None
        val = str(val).strip().lower()
        for _, row in template.iterrows():
            desc = str(row['Description']).strip().lower()
            if val == desc:
                return row['Group']
        return None

    df['Solubility_Group'] = df['Solubility'].apply(lambda x: assign_solubility_group(x, solubility_template))
    df['Dose_Group'] = df['Min Dose (mg)'].apply(lambda x: assign_range_group(x, dose_template))
    df['Toxicity_Group'] = df['ADE/PDE (µg/day)'].apply(lambda x: assign_range_group(x, toxicity_template))
    df['Cleaning_Group'] = df['Hardest To Clean'].apply(lambda x: assign_cleaning_group(x, cleaning_template))
    df['Worst_Case_Rating'] = (
        df['Solubility_Group'].astype(float) *
        df['Dose_Group'].astype(float) *
        df['Toxicity_Group'].astype(float) *
        df['Cleaning_Group'].astype(float)
    )
    df['BatchSize_Dose_Ratio'] = df['Min Batch Size (kg)'] / df['Max Dose (mg)']

    prev_worst_case = df.loc[df['Worst_Case_Rating'].idxmax()]
    next_worst_case = df.loc[df['BatchSize_Dose_Ratio'].idxmin()]
    min_batch_next_kg = next_worst_case['Min Batch Size (kg)']
    max_dose_next_mg = next_worst_case['Max Dose (mg)']
    min_dose_prev_mg = prev_worst_case['Min Dose (mg)']
    ade_prev_ug = prev_worst_case['ADE/PDE (µg/day)']
    ade_prev_mg = ade_prev_ug / 1000

    maco_10ppm = 0.00001 * min_batch_next_kg * 1e6 / max_dose_next_mg
    maco_tdd = min_dose_prev_mg * min_batch_next_kg * 1e6 / (max_dose_next_mg * 1000)
    maco_ade = ade_prev_mg * min_batch_next_kg * 1e6 / max_dose_next_mg
    lowest_maco = min(maco_10ppm, maco_tdd, maco_ade)

    total_surface_area = df_equip['Product contact Surface Area (m2)'].sum()
    total_surface_area_with_margin = total_surface_area * 1.2
    swab_surface = df['Swab Surface in M. Sq.'].iloc[0]
    swab_limit = lowest_maco * swab_surface / total_surface_area_with_margin

    rinse_limits = []
    for idx, row in df_equip.iterrows():
        eq_surface = row['Product contact Surface Area (m2)']
        rinse_limit = lowest_maco * eq_surface / total_surface_area_with_margin
        rinse_vol_L = rinse_limit / 10
        rinse_limits.append({
            'Eq. Name': row['Eq. Name'],
            'Eq. ID': row['Eq. ID'],
            'Surface Area (m2)': eq_surface,
            'Rinse Limit (mg)': round(rinse_limit, 6),
            'Rinse Volume (L)': round(rinse_vol_L, 2)
        })
    df_rinse_limits = pd.DataFrame(rinse_limits)

    st.markdown("---")
    st.subheader("View Final Results")

    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("📦 Previous Worst Case Product", use_container_width=True):
            st.success(f"**Previous Worst Case Product**: {prev_worst_case['Product Name']}")
            st.write(f"Min Dose: {prev_worst_case['Min Dose (mg)']} mg")
            st.write(f"Max Dose: {prev_worst_case['Max Dose (mg)']} mg")
            st.write(f"ADE/PDE: {prev_worst_case['ADE/PDE (µg/day)']} µg/day")
    with col2:
        if st.button("🚚 Next Worst Case Product", use_container_width=True):
            st.success(f"**Next Worst Case Product**: {next_worst_case['Product Name']}")
            st.write(f"Min Batch Size: {next_worst_case['Min Batch Size (kg)']} kg")
            st.write(f"Max Dose: {next_worst_case['Max Dose (mg)']} mg")
    with col3:
        if st.button("🛑 MACO Calculations", use_container_width=True):
            st.success("**MACO Results**")
            st.write(f"10 ppm MACO: {maco_10ppm:.4f} mg")
            st.write(f"TDD MACO: {maco_tdd:.4f} mg")
            st.write(f"ADE/PDE MACO: {maco_ade:.4f} mg")
            st.write(f"**Lowest MACO (used): {lowest_maco:.4f} mg**")

    col4, col5 = st.columns([1, 1])
    with col4:
        if st.button("🧪 Swab Limit", use_container_width=True):
            st.success("**Swab Limit**")
            st.write(f"Swab Surface Used: {swab_surface} m²")
            st.write(f"Total Equip Surface (with 20% margin): {total_surface_area_with_margin:.2f} m²")
            st.write(f"**Swab Limit: {swab_limit:.6f} mg**")
    with col5:
        if st.button("💧 Rinse Limit & Volume (Equipment-wise)", use_container_width=True):
            st.success("**Rinse Limit & Volume per Equipment**")
            st.write("**(Rinse Volume is in L only)**")
            st.dataframe(df_rinse_limits, use_container_width=True)

st.markdown("""
**Common Issues:**
- If you get a column/sheet name error, please check your Excel file and use the sample template for reference.
- All files must be in `.xlsx` format.
""")

# ------- ATTRACTIVE DISCLAIMER AT THE BOTTOM -------
st.markdown(
    """
    <div style="
        background: linear-gradient(90deg, #FFEEEC 50%, #E0F7FA 100%);
        border: 3px solid #FF9800;
        border-radius: 16px;
        padding: 22px 32px;
        margin: 48px 0 0 0;
        box-shadow: 0 6px 24px #ffecb3;
        max-width: 900px;
        margin-left: auto;
        margin-right: auto;
    ">
        <h2 style="color:#d84315; margin-top:0;">🚧 Cleaning Validation APP by <em>Gopal Mandloi</em> 🚧</h2>
        <p style="font-size:17px;">
            <b>This App is <span style="color:#d84315;">Under Development</span> — Please Read!</b>
        </p>
        <p>
            Thank you for visiting the <b>MACO Calculation App</b>! This tool is <b>actively being developed</b> and may have bugs,
            especially in file uploading (templates, multi-file) and result accuracy.<br>
            <span style="color:#b71c1c; font-weight:bold;">Please do not use this app for official or critical calculations at this stage.</span>
        </p>
        <ul style="margin-top:16px;">
            <li><b>Upcoming Features:</b>
                <ul>
                    <li>📄 Automatic protocol and PDF report generation</li>
                    <li>🖱️ One-click calculation/export of all results</li>
                    <li>⚡ Enhanced automatic result calculation</li>
                </ul>
            </li>
        </ul>
        <p>Once all bugs are fixed, I’ll create a <b>detailed video guide</b> on how to use this app.</p>
        <div style="margin:14px 0; color:#1565c0;"><b>🔎 Your Feedback Needed:</b> Please share your expectations, feature requests, or improvement ideas. This helps ensure I address all needs during development.</div>
        <div style="margin-bottom:14px; color:#388e3c;"><b>🤝 Contributors Welcome:</b> This app is 100% free and built individually with limited resources. If you know Python, Java, HTML, or related tech and want to help, please reach out!</div>
        <div style="font-size:16px; color:#6d4c41;">
            With your feedback and support, I’m confident we’ll make this app even better, very soon.<br>
            <span style="float:right; font-style:italic;">— Gopal Mandloi</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
