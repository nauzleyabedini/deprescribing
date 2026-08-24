import streamlit as st
import time

# --- 1. Epic Hyperspace Advanced CSS Override ---
st.set_page_config(layout="wide", page_title="Epic Hyperspace - Clinical Workspace", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    /* Force Epic desktop background and font */
    [data-testid="stAppViewContainer"] {
        background-color: #d8dee3 !important;
        font-family: 'Tahoma', 'Segoe UI', Arial, sans-serif !important;
    }
    
    /* Global high-density desktop scaling */
    html, body, p, div, span, button, input, textarea {
        font-size: 12px !important;
        color: #111111 !important;
    }

    header {visibility: hidden;}
    [data-testid="stToolbar"] {display: none;}

    /* ----------------------------------------------------------------
       EPIC STORYBOARD BANNER (Top Patient Context)
       ---------------------------------------------------------------- */
    .st-key-storyboard {
        background-color: #1c2d42 !important; /* Epic Dark Navy */
        color: #ffffff !important;
        padding: 6px 12px !important;
        border-bottom: 3px solid #e07a5f !important; /* Epic Orange Accent */
        margin-top: -55px;
        margin-bottom: 5px;
    }
    .st-key-storyboard span, .st-key-storyboard p {
        color: #ffffff !important;
        font-weight: bold;
    }

    /* ----------------------------------------------------------------
       HYPERSPACE TAB NAVIGATION STRIP
       ---------------------------------------------------------------- */
    .epic-tab-strip {
        display: flex;
        gap: 2px;
        background-color: #d8dee3;
        padding: 0px 5px;
        border-bottom: 1px solid #9ba5b1;
        margin-bottom: 8px;
    }
    .epic-tab {
        background-color: #e2e7ec;
        color: #333333;
        padding: 4px 12px;
        border: 1px solid #9ba5b1;
        border-bottom: none;
        border-radius: 3px 3px 0 0;
        font-weight: normal;
    }
    .epic-tab-active {
        background-color: #ffffff;
        color: #1c2d42;
        padding: 4px 14px;
        border: 1px solid #9ba5b1;
        border-bottom: 2px solid #ffffff;
        border-radius: 3px 3px 0 0;
        font-weight: bold;
    }

    /* ----------------------------------------------------------------
       DOCKABLE WORKSPACE WINDOWS (Panels)
       ---------------------------------------------------------------- */
    [class^="st-key-epic_window_"] {
        background-color: #f8f9fa !important;
        border: 1px solid #7b8896 !important;
        border-radius: 0px !important;
        padding: 0px !important;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.15);
    }
    
    /* Epic Window Title Bars (Blue Header) */
    .epic-window-header {
        background: linear-gradient(to bottom, #336699, #204d74);
        color: white !important;
        font-weight: bold;
        padding: 5px 8px;
        text-transform: uppercase;
        font-size: 11px !important;
        letter-spacing: 0.5px;
        border-bottom: 1px solid #122b40;
    }
    
    .epic-window-body {
        padding: 10px;
        background-color: #ffffff;
    }

    /* ----------------------------------------------------------------
       CLINICAL ALERTS & TABLES
       ---------------------------------------------------------------- */
    .epic-alert-box {
        background-color: #fff9db;
        border: 1px solid #f08c00;
        border-left: 5px solid #f59f00;
        padding: 8px;
        margin-bottom: 10px;
    }
    
    /* Epic Desktop Form Buttons */
    .stButton>button {
        background-color: #e6ebef !important;
        border: 1px solid #7b8896 !important;
        color: #222222 !important;
        border-radius: 2px !important;
        font-weight: bold !important;
        padding: 3px 8px !important;
        box-shadow: inset 0 1px 0 rgba(255,255,255,0.8);
    }
    .stButton>button:hover {
        background-color: #d2dce5 !important;
        border-color: #4a637d !important;
    }
    .stButton>button[kind="primary"] {
        background-color: #204d74 !important;
        color: white !important;
        border-color: #122b40 !important;
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
    <div class="epic-tab-active">Discharge Navigator</div>
    <div class="epic-tab">Medications</div>
    <div class="epic-tab">Orders</div>
</div>
""", unsafe_allow_html=True)

# --- 4. Three-Column Dockable Workspace Layout ---
col1, col2, col3 = st.columns(spec=[1, 1.1, 1.3], gap="small")

# ----- WINDOW 1: Patient Chart & Clinical Notes -----
with col1:
    with st.container(key="epic_window_1"):
        st.markdown('<div class="epic-window-header">Chart Review: Meds & Progress</div>', unsafe_allow_html=True)
        st.markdown('<div class="epic-window-body">', unsafe_allow_html=True)
        
        st.markdown("**Home / Admission Meds:**")
        st.code("• Lisinopril 10mg PO Daily\n• Metformin 500mg PO BID", language="text")
        
        st.markdown("**Active Inpatient Meds:**")
        st.code("• Lisinopril 10mg PO Daily\n• Metformin 500mg PO BID\n• Quetiapine 25mg PO QHS *(Started HD#3)*", language="text")
        
        st.markdown("**Progress Note / Consults (HD#3):**")
        st.text_area("Note Text", "HD#3: Patient extubated yesterday. Overnight, developed acute agitation, pulling at IV lines. CAM-ICU positive. Geriatrics consulted, recommended Quetiapine 25mg QHS PRN for hyperactive delirium. Pt calmer this morning.", height=130, disabled=True, label_visibility="collapsed")
        
        st.markdown('</div>', unsafe_allow_html=True)

# ----- WINDOW 2: Qualified Health AI Engine -----
with col2:
    with st.container(key="epic_window_2"):
        st.markdown('<div class="epic-window-header">Qualified Health: Background Engine</div>', unsafe_allow_html=True)
        st.markdown('<div class="epic-window-body">', unsafe_allow_html=True)
        
        st.write("Agent status: **Monitoring Discharge Tab**")
        run_agent = st.button("Trigger AI Protocol ⚡")
        
        agent_output = st.empty()
        
        if run_agent:
            with st.spinner("Executing FHIR cross-reference & NLP parse..."):
                time.sleep(1.5)
                simulated_response = {
                    "FHIR_Delta": "Quetiapine 25mg added inpatient",
                    "Indication_Verified": "Hyperactive ICU Delirium (HD#3)",
                    "Chronic_History": "None (No Schizophrenia/Bipolar coded)",
                    "Action_Recommended": "Safe to Deprescribe at Discharge",
                    "SmartLink_Text": "Quetiapine 25mg was initiated for acute hyperactive delirium during ICU stay. As delirium has resolved, medication is discontinued prior to discharge."
                }
                agent_output.json(simulated_response)
        else:
            st.info("The agent runs silently in the background. Click button to simulate event.")
            
        st.markdown('</div>', unsafe_allow_html=True)

# ----- WINDOW 3: Discharge Reconciliation Workflow -----
with col3:
    with st.container(key="epic_window_3"):
        st.markdown('<div class="epic-window-header">Discharge Medication Reconciliation</div>', unsafe_allow_html=True)
        st.markdown('<div class="epic-window-body">', unsafe_allow_html=True)
        
        if run_agent:
            st.markdown("""
            <div class="epic-alert-box">
                <strong>⚠️ QUALIFIED HEALTH DECISION SUPPORT</strong><br>
                <strong>Quetiapine 25mg</strong> was flagged as an acute-care continuation without chronic indication. Risk of post-discharge falls & cognitive sedation.
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("**Discharge Action Selection:**")
            
            action_btn1, action_btn2 = st.columns(2)
            with action_btn1:
                if st.button("Accept: Pend Discontinue", type="primary", use_container_width=True):
                    st.success("Order pended: Discontinue Quetiapine.")
            with action_btn2:
                if st.button("Reject: Keep Active", use_container_width=True):
                    st.warning("Flag cleared. Routed to Clinical Pharmacist.")
            
            st.markdown("<br>**Discharge Summary Addendum (SmartText):**", unsafe_allow_html=True)
            st.text_area("Summary Box", value=simulated_response['SmartLink_Text'], height=90, label_visibility="collapsed")
        else:
            st.markdown("<p style='color: #666; font-style: italic;'>Awaiting background evaluation results...</p>", unsafe_allow_html=True)
            
        st.markdown('</div>', unsafe_allow_html=True)
