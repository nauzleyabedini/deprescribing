import streamlit as st
import time

# --- 1. Epic Hyperspace Advanced CSS Override ---
st.set_page_config(layout="wide", page_title="Epic Hyperspace - Clinical Workspace", initial_sidebar_state="collapsed")

st.html("""
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
            
        st.markdown('</div>', unsafe_allow_html=True)       EPIC NAVIGATION TABS (Visual Fake)
       --------------------------------------------------- */
    .epic-tabs {
        display: flex; gap: 5px; padding: 5px 15px 0px 15px; background-color: #d8dee3; border-bottom: 1px solid #9ba5b1;
    }
    .epic-tab-active {
        background-color: #ffffff; color: #23395d; font-weight: bold; border: 1px solid #9ba5b1; border-bottom: none; padding: 5px 15px; border-radius: 4px 4px 0 0;
    }
    .epic-tab-inactive {
        background-color: #e8ecf1; color: #555; border: 1px solid #9ba5b1; padding: 5px 15px; border-radius: 4px 4px 0 0;
    }

    /* ---------------------------------------------------
       MAIN CONTENT PANELS
       Targets: st.container(key="epic_panel_...")
       --------------------------------------------------- */
    [class^="st-key-epic_panel_"] {
        background-color: #ffffff;
        border: 1px solid #9ba5b1;
        border-radius: 2px;
        padding: 10px !important;
        box-shadow: 1px 1px 3px rgba(0,0,0,0.1);
        height: 100%;
    }
    
    /* Section Headers inside the panels (Epic Blue) */
    .epic-section-header {
        background-color: #e8ecf1;
        color: #23395d;
        font-weight: bold;
        padding: 4px 8px;
        border: 1px solid #9ba5b1;
        margin-bottom: 10px;
        text-transform: uppercase;
        font-size: 11px !important;
    }

    /* ---------------------------------------------------
       AI ALERT BOX (Qualified Health Intercept)
       --------------------------------------------------- */
    .qh-alert {
        background-color: #fff4ce;
        border-left: 4px solid #e5a910;
        border-top: 1px solid #e5a910; border-right: 1px solid #e5a910; border-bottom: 1px solid #e5a910;
        padding: 8px 12px;
        color: #333;
        margin-bottom: 15px;
    }
    
    /* Epic Style Buttons */
    .stButton>button {
        background-color: #f3f5f8; border: 1px solid #9ba5b1; color: #333; border-radius: 3px; font-weight: bold; padding: 2px 10px;
    }
    .stButton>button:hover { background-color: #e2e6ea; border-color: #7b8896;}
    
    /* Primary Button (Blue Epic Action) */
    .stButton>button[kind="primary"] {
        background-color: #204d74; border: 1px solid #122b40; color: white;
    }
    .stButton>button[kind="primary"]:hover { background-color: #1a3e5c; }
    </style>
""", unsafe_allow_html=True)

# --- 2. Epic Storyboard (Top Banner) ---
with st.container(key="storyboard"):
    cols = st.columns([2, 1, 1, 1, 2])
    cols[0].markdown("**DOE, JOHN** | Male, 78 yo | DOB: 11/20/1947")
    cols[1].markdown("MRN: **9482011**")
    cols[2].markdown("CSN: **48299103**")
    cols[3].markdown("Loc: **MS-4 East**")
    cols[4].markdown("Allergies: <span style='color:#ff9999;'>Penicillins</span>", unsafe_allow_html=True)

# --- 3. Epic Tabs ---
st.markdown("""
<div class="epic-tabs">
    <div class="epic-tab-inactive">Chart Review</div>
    <div class="epic-tab-inactive">Results</div>
    <div class="epic-tab-inactive">Notes</div>
    <div class="epic-tab-active">Discharge (Nav)</div>
    <div class="epic-tab-inactive">Orders</div>
</div>
""", unsafe_allow_html=True)

st.write("") # Tiny spacer

# --- 4. Main Workspace Layout ---
col1, col2, col3 = st.columns([1, 1.2, 1.5])

# ----- COLUMN 1: Clinical Data & Charting -----
with col1:
    with st.container(key="epic_panel_1"):
        st.markdown('<div class="epic-section-header">Admission vs Inpatient Meds</div>', unsafe_allow_html=True)
        st.markdown("**Prior to Admission:**")
        st.code("Lisinopril 10mg PO Daily\nMetformin 500mg PO BID", language="text")
        
        st.markdown("**Active Inpatient:**")
        st.code("Lisinopril 10mg PO Daily\nMetformin 500mg PO BID\nQuetiapine 25mg PO QHS (Started HD#3)", language="text")
        
        st.write("---")
        st.markdown('<div class="epic-section-header">Latest Progress Note</div>', unsafe_allow_html=True)
        st.text_area("H&P / Consults", "HD#3: Pt extubated yesterday. Overnight, developed severe agitation, pulling at IV lines. CAM-ICU positive. Geriatrics consulted, recommended Quetiapine 25mg QHS PRN for hyperactive delirium. Pt calmer this morning. Continuing standard sepsis protocol.", height=150, disabled=True)

# ----- COLUMN 2: Qualified Health AI Engine -----
with col2:
    with st.container(key="epic_panel_2"):
        st.markdown('<div class="epic-section-header">Qualified Health: Background Processing</div>', unsafe_allow_html=True)
        
        run_agent = st.button("Run Deprescribing Protocol ▶")
        agent_output = st.empty()
        
        if run_agent:
            with st.spinner("Executing FHIR cross-reference and NLP note analysis..."):
                time.sleep(2) # Simulate API latency
                
                # Hardcoded JSON logic engine payload
                simulated_llm_response = {
                    "FHIR_Delta_Found": "Quetiapine 25mg",
                    "indication_found": True,
                    "acute_trigger": "Hyperactive ICU delirium (HD#3)",
                    "chronic_continuation_recommended": False,
                    "action_recommendation": "Eligible for Deprescribing",
                    "draft_discharge_rationale": "Quetiapine 25mg was initiated for acute hyperactive delirium in the ICU. As delirium has resolved, this medication is safely discontinued prior to discharge."
                }
                agent_output.json(simulated_llm_response)
        else:
            st.info("Waiting for agent trigger. Typically runs silently on discharge tab activation.")

# ----- COLUMN 3: Discharge Med Rec Action Panel -----
with col3:
    with st.container(key="epic_panel_3"):
        st.markdown('<div class="epic-section-header">Discharge Medication Reconciliation</div>', unsafe_allow_html=True)
        
        if run_agent:
            st.markdown(f"""
            <div class="qh-alert">
                <strong><span style="color:#b22222;">!</span> Transition of Care Alert: Inappropriate CNS Med</strong><br>
                <strong>Quetiapine 25mg</strong> was flagged as a net-new medication started for <em>{simulated_llm_response['acute_trigger']}</em>. No chronic psychiatric indication found in FHIR history.
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("**Action Required: Resolve Quetiapine 25mg**")
            
            # Epic-style discrete action buttons
            action_col1, action_col2 = st.columns(2)
            with action_col1:
                if st.button("Discontinue (AI Rec)", type="primary", use_container_width=True):
                    st.success("Order pended: Discontinue Quetiapine 25mg.")
            with action_col2:
                if st.button("Keep Active (CC Pharmacy)", use_container_width=True):
                    st.warning("Medication continued. Routing to Unit Pharmacist.")
                    
            st.write("---")
            st.markdown('<div class="epic-section-header">SmartLink: Discharge Summary Draft</div>', unsafe_allow_html=True)
            st.text_area("Hospital Course Addendum", value=simulated_llm_response['draft_discharge_rationale'], height=100)
        else:
            st.markdown("<p style='color: #777;'>Reconciliation grid will populate upon review.</p>", unsafe_allow_html=True)
