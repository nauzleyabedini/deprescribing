import streamlit as st
import time

# --- 1. Epic Hyperspace Configuration & CSS ---
st.set_page_config(layout="wide", page_title="Epic | Hyperspace", initial_sidebar_state="collapsed")

st.html("""
    <style>
    /* Global Application Background - Epic Gray */
    [data-testid="stAppViewContainer"] {
        background-color: #d8dee3;
        font-family: 'Tahoma', 'Segoe UI', Arial, sans-serif !important;
    }
    
    /* Shrink all font sizes to match Epic's high-density desktop look */
    html, body, p, div, span, button, input, textarea, [class*="st-"] {
        font-size: 13px !important;
    }

    /* Hide standard Streamlit header */
    header {visibility: hidden;}

    /* ---------------------------------------------------
       STORYBOARD BANNER (Top Patient Info)
       Targets: st.container(key="storyboard")
       --------------------------------------------------- */
    .st-key-storyboard {
        background-color: #23395d; /* Classic Epic Navy */
        color: white;
        padding: 5px 15px !important;
        border-bottom: 3px solid #f4a261; /* Epic's orange accent line */
        margin-top: -50px;
    }
    .st-key-storyboard p { color: white !important; font-weight: bold; margin: 0;}
    
    /* ---------------------------------------------------
       EPIC NAVIGATION TABS (Visual Fake)
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
