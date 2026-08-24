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

/* Pended Order Box */
.pended-order {
    border: 1px solid #aaaaaa; background-color: #f8f9fa; padding: 10px; border-radius: 3px; margin-bottom: 5px;
}

/* Base Button Styling */
button {
    border-radius: 2px !important; 
    font-weight: bold !important; 
    padding: 4px 10px !important;
}

/* Secondary Button (Gray/Black) */
button[kind="secondary"] {
    background-color: #f0f2f5 !important; 
    border: 1px solid #555555 !important; 
}
button[kind="secondary"] * {
    color: #000000 !important;
}

/* Primary Button (Deep Blue/White) */
button[kind="primary"] {
    background-color: #204d74 !important; 
    border-color: #122b40 !important;
}
/* FORCE all elements inside primary button to be white */
button[kind="primary"] * {
    color: #ffffff !important;
}

/* Safe Streamlit Expander Styling */
[data-testid="stExpander"] {
    border: 1px solid #aaaaaa !important;
    border-radius: 3px !important;
    margin-top: 5px;
    margin-bottom: 10px;
    background-color: #ffffff !important;
}
[data-testid="stExpander"] summary {
    background-color: #e2e6ea !important;
    padding: 8px 12px !important;
}
[data-testid="stExpander"] summary p {
    color: #0056b3 !important;
    font-weight: bold !important;
    font-size: 12px !important;
}
[data-testid="stExpanderDetails"] {
    padding: 10px !important;
}

/* Dockable Workspace Windows */
[class^="st-key-epic_window_"] {
    background-color: #ffffff !important;
    border: 1px solid #888888 !important;
    border-radius: 0px !important;
    padding: 15px !important;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.15);
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
    with st.container(key="epic_window_1"):
        st.markdown("""
<div style="background-color: #c9d6e2; color: #000000; font-weight: bold; padding: 8px 12px; border-bottom: 1px solid #888888; font-size: 13px; text-transform: uppercase; margin: -15px -15px 15px -15px;">
Discharge Medication Reconciliation Grid
</div>
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
            if st.button("Complete Med Rec & Continue to Orders ⚡", type="primary", use_container_width=True):
                with st.spinner("Processing reconciliation..."):
                    time.sleep(1.5)
                st.session_state.reconciled = True
                st.rerun()
        else:
            st.success("Med Rec submitted.")
            if st.button("Reset Simulation"):
                st.session_state.reconciled = False
                st.rerun()

# ----- WINDOW 2: Discharge Orders (Silent Intercept) -----
with col2:
    with st.container(key="epic_window_2"):
        st.markdown("""
<div style="background-color: #c9d6e2; color: #000000; font-weight: bold; padding: 8px 12px; border-bottom: 1px solid #888888; font-size: 13px; text-transform: uppercase; margin: -15px -15px 15px -15px;">
Discharge Orders: Awaiting Signature
</div>
""", unsafe_allow_html=True)
        
        if st.session_state.reconciled:
            st.markdown("""
<p style="color: #006600; font-weight: bold; font-size: 13px; margin-bottom: 5px;">1 Order Pended for Review</p>
<div class="pended-order">
    <p style="margin: 0; font-size: 13px; font-weight: bold;">
        <span style="color: #aa0000; text-decoration: line-through;">Quetiapine (SEROQUEL) 25mg Tablet</span>
    </p>
    <p style="margin: 0; font-size: 12px; color: #333333;"><strong>Action:</strong> <span style="color: #aa0000; font-weight: bold;">Discontinue</span></p>
    <p style="margin: 0; font-size: 11px; color: #666666;">Route: Oral | Frequency: Nightly</p>
</div>
""", unsafe_allow_html=True)
            
            # The fixed "Pop up bubble" for rationale
            with st.expander("💡 View Auto-Discontinue Rationale"):
                st.markdown("""
                <p style="font-size: 12px; color: #333333; margin: 0; padding: 5px;">
                <strong>Qualified Health AI:</strong> Chart review confirms this medication was initiated on HD#3 for <em>Hyperactive ICU Delirium</em>. No chronic psychiatric indication or taper plan was found in prior FHIR history. This medication was auto-pended for discontinuation to mitigate 30-day post-discharge fall risk.
                </p>
                """, unsafe_allow_html=True)
                if st.button("Undo & Keep Active (Route to Pharmacy)", key="undo_btn"):
                    st.warning("Order restored. Routing to unit pharmacist.")

            st.markdown("""
<hr style="margin: 15px 0; border: 0; border-top: 1px solid #dddddd;">
<p style="color: #000000 !important; font-weight: bold; font-size: 13px; margin-bottom: 5px;">SmartText: Discharge Summary Addendum</p>
""", unsafe_allow_html=True)
            
            st.text_area(
                "Summary Addendum", 
                value="Quetiapine 25mg was initiated during the hospitalization for acute hyperactive delirium in the setting of sepsis. As the delirium has fully resolved and cognitive baseline is regained, this medication has been discontinued prior to discharge to mitigate fall risks.",
                height=90,
                label_visibility="collapsed"
            )
            
            st.write("")
            if st.button("Sign Orders & Close Encounter", type="primary", use_container_width=True):
                st.success("Orders signed successfully. Discharge Summary updated.")
                
        else:
            st.info("Awaiting Med Rec submission... Complete the grid on the left to generate discharge orders.")
