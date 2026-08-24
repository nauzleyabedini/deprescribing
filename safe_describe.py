import streamlit as st
import time

# --- 1. Epic Hyperspace Advanced CSS Override ---
st.set_page_config(layout="wide", page_title="Epic Hyperspace - Discharge Med Rec", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #d8dee3 !important;
        font-family: 'Tahoma', 'Segoe UI', Arial, sans-serif !important;
    }
    
    /* Global layout text */
    html, body, p, div, span:not(.force-white), input, textarea {
        font-size: 12px !important;
        color: #111111 !important;
    }
    header {visibility: hidden;}
    [data-testid="stToolbar"] {display: none;}

    /* Storyboard Banner */
    .st-key-storyboard {
        background-color: #1c2d42 !important;
        color: #ffffff !important;
        padding: 6px 12px !important;
        border-bottom: 3px solid #e07a5f !important;
        margin-top: -55px;
        margin-bottom: 5px;
    }
    .st-key-storyboard span { color: #ffffff !important; font-weight: bold; }

    /* Hyperspace Tabs */
    .epic-tab-strip {
        display: flex; gap: 2px; background-color: #d8dee3; padding: 0px 5px; border-bottom: 1px solid #9ba5b1; margin-bottom: 8px;
    }
    .epic-tab {
        background-color: #e2e7ec; color: #333333; padding: 4px 12px; border: 1px solid #9ba5b1; border-bottom: none; border-radius: 3px 3px 0 0;
    }
    .epic-tab-active {
        background-color: #ffffff; color: #1c2d42; padding: 4px 14px; border: 1px solid #9ba5b1; border-bottom: 2px solid #ffffff; border-radius: 3px 3px 0 0; font-weight: bold;
    }

    /* Dockable Workspace Windows */
    [class^="st-key-epic_window_"] {
        background-color: #ffffff !important;
        border: 1px solid #7b8896 !important;
        border-radius: 0px !important;
        padding: 0px !important;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.15);
    }
    
    .epic-window-body { padding: 10px; background-color: #ffffff; }

    /* Med Rec Table Styling */
    .med-table { width: 100%; border-collapse: collapse; margin-bottom: 10px; font-size: 12px; }
    .med-table th { background-color: #e8ecf1; border: 1px solid #9ba5b1; padding: 4px; text-align: left; }
    .med-table td { border: 1px solid #9ba5b1; padding: 6px 4px; }
    
    .epic-alert-box {
        background-color: #fff9db; border: 1px solid #f08c00; border-left: 5px solid #f59f00; padding: 8px; margin-bottom: 10px;
    }
    
    .stButton>button {
        background-color: #e6ebef !important; border: 1px solid #7b8896 !important; color: #222222 !important; border-radius: 2px !important; font-weight: bold !important; padding: 3px 8px !important;
    }
    .stButton>button[kind="primary"] {
        background-color: #204d74 !important; color: white !important; border-color: #122b40 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. Storyboard Top Banner ---
with st.container(key="storyboard"):
    cols = st.columns([2.5, 1, 1, 1, 1.5])
    cols[0].markdown("<span>DOE, JOHN</span> (M, 78 yo) | MRN: 9482011", unsafe_allow_html=True)
    cols[1].markdown("<span>DOB:</span> 11/20/1947", unsafe_allow_html=True)
    cols[2].markdown("<span>Bed:</span> MS-4 312-2", unsafe_allow_html=True)
    cols[3].markdown("<span>Code:</span> Full Code", unsafe_allow_html=True)
    cols[4].markdown("<span>Allergies:</span> <span style='color:#ff9999;'>Penicillin</span>", unsafe_allow_html=True)

# --- 3. Hyperspace Navigation Tabs ---
st.markdown("""
<div class="epic-tab-strip">
    <div class="epic-tab">Chart Review</div>
    <div class="epic-tab">SnapShot</div>
    <div class="epic-tab">Notes</div>
    <div class="epic-tab-active">Discharge Navigator: Med Rec</div>
    <div class="epic-tab">Orders</div>
</div>
""", unsafe_allow_html=True)

# Initialize session state for workflow trigger
if "reconciled" not in st.session_state:
    st.session_state.reconciled = False

# --- 4. Workspace Layout ---
col1, col2 = st.columns(spec=[1.3, 1.2], gap="small")

# ----- WINDOW 1: Epic Discharge Med Rec Grid -----
with col1:
    with st.container(key="epic_window_1"):
        st.markdown(
            '<div style="background: linear-gradient(to bottom, #336699, #204d74); padding: 6px 8px; border-bottom: 1px solid #122b40;">'
            '<span class="force-white" style="color: #ffffff !important; font-weight: bold !important; text-transform: uppercase; font-size: 11px;">Discharge Medication Reconciliation Grid</span>'
            '</div>', 
            unsafe_allow_html=True
        )
        st.markdown('<div class="epic-window-body">', unsafe_allow_html=True)
        
        st.markdown("Review home and hospital medications prior to generating discharge prescriptions.")
        
        # Simulate Epic Med Rec Table
        st.markdown("""
        <table class="med-table">
            <tr>
                <th>Medication</th>
                <th>Admission Source</th>
                <th>Hospital Course Action</th>
                <th>Discharge Plan</th>
            </tr>
            <tr>
                <td><strong>Lisinopril 10mg</strong> PO Daily</td>
                <td>Home Med</td>
                <td>Continued</td>
                <td><span style="color:green; font-weight:bold;">[X] Continue</span></td>
            </tr>
            <tr>
                <td><strong>Metformin 500mg</strong> PO BID</td>
                <td>Home Med</td>
                <td>Continued</td>
                <td><span style="color:green; font-weight:bold;">[X] Continue</span></td>
            </tr>
            <tr style="background-color: #fdf2f2;">
                <td><strong>Quetiapine 25mg</strong> PO QHS</td>
                <td><em>New Inpatient Start (HD#3)</em></td>
                <td>Active for Delirium</td>
                <td><span style="color:red; font-weight:bold;">[X] Continue (Auto-selected)</span></td>
            </tr>
        </table>
        """, unsafe_allow_html=True)
        
        st.write("")
        if not st.session_state.reconciled:
            if st.button("Complete Med Rec & Sign Discharge Orders ⚡", type="primary", use_container_width=True):
                with st.spinner("FHIR API querying EHR delta & LLM evaluating clinical chart context..."):
                    time.sleep(1.5)
                st.session_state.reconciled = True
                st.rerun()
        else:
            st.success("Med Rec submitted. Intercept active.")
            if st.button("Reset Simulation"):
                st.session_state.reconciled = False
                st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)

# ----- WINDOW 2: Qualified Health Intercept & Pended Orders -----
with col2:
    with st.container(key="epic_window_2"):
        st.markdown(
            '<div style="background: linear-gradient(to bottom, #336699, #204d74); padding: 6px 8px; border-bottom: 1px solid #122b40;">'
            '<span class="force-white" style="color: #ffffff !important; font-weight: bold !important; text-transform: uppercase; font-size: 11px;">Qualified Health: Decision Support & Pended Actions</span>'
            '</div>', 
            unsafe_allow_html=True
        )
        st.markdown('<div class="epic-window-body">', unsafe_allow_html=True)
        
        if st.session_state.reconciled:
            st.markdown("""
            <div class="epic-alert-box">
                <strong>⚠️ QUALIFIED HEALTH SMART-INTERCEPT</strong><br>
                <strong>Safety Catch:</strong> You selected to continue <strong>Quetiapine 25mg</strong> at discharge. FHIR & chart review confirms this was started on HD#3 for <em>Hyperactive ICU Delirium</em>. No chronic psychiatric indication or taper plan found. Continuing this outpatient dramatically increases 30-day fall risk.
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("**Recommended Epic Order Adjustments:**")
            
            c1, c2 = st.columns(2)
            with c1:
                if st.button("Accept: Pend Discontinue", type="primary", use_container_width=True):
                    st.success("Order pended: Discontinue Quetiapine 25mg.")
            with c2:
                if st.button("Override: Keep Active", use_container_width=True):
                    st.warning("Override logged. Routing notification to Clinical Pharmacist.")
            
            st.markdown("<br><strong>SmartText: Discharge Summary Addendum</strong>", unsafe_allow_html=True)
            st.text_area(
                "Summary Addendum", 
                value="Quetiapine 25mg was initiated during the hospitalization for acute hyperactive delirium in the setting of sepsis. As the delirium has fully resolved and cognitive baseline is regained, this medication has been discontinued prior to discharge to mitigate fall risks.",
                height=110,
                label_visibility="collapsed"
            )
        else:
            st.info("Awaiting Med Rec submission... Click 'Complete Med Rec' on the left to trigger the AI safety intercept.")
            
        st.markdown('</div>', unsafe_allow_html=True)
