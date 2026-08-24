import streamlit as st
import time

# --- 1. Basic Setup ---
st.set_page_config(layout="wide", page_title="Epic Hyperspace - Discharge Med Rec", initial_sidebar_state="collapsed")

# Injecting CSS for a purely Light-Themed Epic UI
st.markdown("""
<style>
/* Force Light Gray App Background */
.stApp, [data-testid="stAppViewContainer"] {
    background-color: #e2e6ea !important;
}

/* Global text overrides */
html, body, p, div, span, label, li {
    font-family: 'Tahoma', 'Segoe UI', Arial, sans-serif !important;
    color: #000000 !important;
}

header {visibility: hidden;}
[data-testid="stToolbar"] {display: none;}

/* Table Styling - High Contrast */
.epic-table {
    width: 100%; border-collapse: collapse; margin-top: 10px; margin-bottom: 15px; font-size: 13px;
    background-color: #ffffff;
}
.epic-table th {
    background-color: #e2e6ea !important; color: #000000 !important; 
    border: 1px solid #999999 !important; padding: 6px; text-align: left; font-weight: bold;
}
.epic-table td {
    border: 1px solid #999999 !important; padding: 8px 6px; color: #000000 !important;
}

/* Alert Box */
.alert-box {
    background-color: #fff4ce !important; border: 1px solid #d39e00 !important; border-left: 6px solid #d39e00 !important;
    padding: 10px !important; margin-bottom: 15px !important; color: #000000 !important; font-size: 13px !important;
}

/* Buttons */
.stButton>button {
    background-color: #f0f2f5 !important; border: 1px solid #555555 !important; color: #000000 !important; 
    border-radius: 2px !important; font-weight: bold !important; padding: 4px 10px !important;
}
.stButton>button[kind="primary"] {
    background-color: #204d74 !important; color: #ffffff !important; border-color: #122b40 !important;
}
</style>
""", unsafe_allow_html=True)

# Initialize session state for workflow trigger
if "reconciled" not in st.session_state:
    st.session_state.reconciled = False

# --- 2. Storyboard Top Banner (Light Steel Blue) ---
st.markdown("""
<div style="background-color: #b9c9d9; padding: 10px 15px; border-bottom: 4px solid #d9534f; margin-top: -50px; margin-bottom: 10px; border-radius: 3px; color: #000000;">
<span style="font-weight: bold; font-size: 14px; margin-right: 20px;">DOE, JOHN (M, 78 yo)</span>
<span style="font-size: 13px; margin-right: 20px;">MRN: 9482011</span>
<span style="font-size: 13px; margin-right: 20px;">DOB: 11/20/1947</span>
<span style="font-size: 13px; margin-right: 20px;">Bed: MS-4 312-2</span>
<span style="font-size: 13px; margin-right: 20px;">Code: Full Code</span>
<span style="font-size: 13px;">Allergies: <span style="color: #cc0000; font-weight: bold;">Penicillin</span></span>
</div>
""", unsafe_allow_html=True)

# --- 3. Hyperspace Navigation Tabs ---
st.markdown("""
<div style="display: flex; gap: 4px; padding: 0 10px; border-bottom: 2px solid #aaaaaa; margin-bottom: 15px;">
<div style="background-color: #e2e6ea; color: #333333; padding: 6px 15px; border: 1px solid #aaaaaa; border-bottom: none; border-radius: 4px 4px 0 0; font-size: 13px;">Chart Review</div>
<div style="background-color: #e2e6ea; color: #333333; padding: 6px 15px; border: 1px solid #aaaaaa; border-bottom: none; border-radius: 4px 4px 0 0; font-size: 13px;">Notes</div>
<div style="background-color: #ffffff; color: #000000; font-weight: bold; padding: 6px 15px; border: 1px solid #aaaaaa; border-bottom: 2px solid #ffffff; border-radius: 4px 4px 0 0; font-size: 13px; position: relative; top: 2px;">Discharge Navigator: Med Rec</div>
<div style="background-color: #e2e6ea; color: #333333; padding: 6px 15px; border: 1px solid #aaaaaa; border-bottom: none; border-radius: 4px 4px 0 0; font-size: 13px;">Orders</div>
</div>
""", unsafe_allow_html=True)

# --- 4. Workspace Layout ---
col1, spacer, col2 = st.columns([1.2, 0.05, 1.2])

# ----- WINDOW 1: Epic Discharge Med Rec Grid -----
with col1:
    st.markdown("""
<div style="background-color: #c9d6e2; color: #000000; font-weight: bold; padding: 8px 12px; border: 1px solid #888888; border-bottom: none; font-size: 13px; text-transform: uppercase;">
Discharge Medication Reconciliation Grid
</div>
<div style="background-color: #ffffff; border: 1px solid #888888; padding: 15px; min-height: 400px;">
<p style="color: #000000; font-size: 13px; margin-top: 0;">Review home and hospital medications prior to generating discharge prescriptions.</p>

<table class="epic-table">
<tr>
<th>Medication</th>
<th>Admission Source</th>
<th>Discharge Plan</th>
</tr>
<tr>
<td><strong>Lisinopril 10mg</strong> PO Daily</td>
<td>Home Med</td>
<td style="color: #006600; font-weight: bold;">[X] Continue</td>
</tr>
<tr>
<td><strong>Metformin 500mg</strong> PO BID</td>
<td>Home Med</td>
<td style="color: #006600; font-weight: bold;">[X] Continue</td>
</tr>
<tr style="background-color: #ffeaea;">
<td><strong>Quetiapine 25mg</strong> PO QHS</td>
<td style="color: #aa0000;"><em>New Inpatient Start (HD#3)</em></td>
<td style="color: #aa0000; font-weight: bold;">[X] Continue (Auto-selected)</td>
</tr>
</table>
""", unsafe_allow_html=True)
    
    st.write("") 
    if not st.session_state.reconciled:
        if st.button("Complete Med Rec & Sign Orders ⚡", type="primary", use_container_width=True):
            with st.spinner("FHIR API querying EHR delta & LLM evaluating clinical chart context..."):
                time.sleep(1.5)
            st.session_state.reconciled = True
            st.rerun()
    else:
        st.success("Med Rec submitted. Intercept active.")
        if st.button("Reset Simulation"):
            st.session_state.reconciled = False
            st.rerun()
            
    st.markdown("""</div>""", unsafe_allow_html=True) 

# ----- WINDOW 2: Qualified Health Intercept & Pended Orders -----
with col2:
    st.markdown("""
<div style="background-color: #c9d6e2; color: #000000; font-weight: bold; padding: 8px 12px; border: 1px solid #888888; border-bottom: none; font-size: 13px; text-transform: uppercase;">
Qualified Health: Decision Support & Pended Actions
</div>
<div style="background-color: #ffffff; border: 1px solid #888888; padding: 15px; min-height: 400px;">
""", unsafe_allow_html=True)
    
    if st.session_state.reconciled:
        st.markdown("""
<div class="alert-box">
<strong style="color: #990000 !important; font-size: 14px;">⚠️ QUALIFIED HEALTH SMART-INTERCEPT</strong><br><br>
<strong style="color: #000000 !important;">Safety Catch:</strong> You selected to continue <strong>Quetiapine 25mg</strong> at discharge. FHIR & chart review confirms this was started on HD#3 for <em>Hyperactive ICU Delirium</em>. No chronic psychiatric indication or taper plan found. Continuing this outpatient dramatically increases 30-day fall risk.
</div>
<p style="color: #000000 !important; font-weight: bold; font-size: 13px;">Recommended Epic Order Adjustments:</p>
""", unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            if st.button("Accept: Pend Discontinue", type="primary", use_container_width=True):
                st.success("Order pended: Discontinue Quetiapine 25mg.")
        with c2:
            if st.button("Override: Keep Active", use_container_width=True):
                st.warning("Override logged. Routing notification to Clinical Pharmacist.")
        
        st.markdown("""
<div style="margin-top: 20px;">
<p style="color: #000000 !important; font-weight: bold; font-size: 13px; margin-bottom: 5px;">SmartText: Discharge Summary Addendum</p>
</div>
""", unsafe_allow_html=True)
        st.text_area(
            "Summary Addendum", 
            value="Quetiapine 25mg was initiated during the hospitalization for acute hyperactive delirium in the setting of sepsis. As the delirium has fully resolved and cognitive baseline is regained, this medication has been discontinued prior to discharge to mitigate fall risks.",
            height=110,
            label_visibility="collapsed"
        )
    else:
        st.info("Awaiting Med Rec submission... Click 'Complete Med Rec' on the left to trigger the AI safety intercept.")
        
    st.markdown("""</div>""", unsafe_allow_html=True)
