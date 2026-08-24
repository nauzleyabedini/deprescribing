import streamlit as st
import time

# --- 1. Vibe Coding: Advanced Epic-Style CSS ---
st.set_page_config(layout="wide", page_title="Epic | Discharge Med Rec")

st.markdown("""
    <style>
    /* Global Settings: Dense, Arial font, gray background */
    html, body, [class*="css"] {
        font-family: 'Arial', sans-serif;
        background-color: #e5e8ea; 
        font-size: 14px;
    }
    
    /* The Epic-style Top Patient Banner */
    .epic-banner {
        background: linear-gradient(to bottom, #4a637d, #2b3a4a);
        color: white; 
        padding: 8px 15px; 
        border-radius: 3px; 
        font-size: 14px;
        font-weight: bold;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        margin-bottom: 15px;
    }
    
    /* Standard EHR Panel/Window */
    .epic-panel {
        background-color: #ffffff; 
        padding: 12px; 
        border: 1px solid #a0aab5; 
        box-shadow: inset 0 1px 0 rgba(255,255,255,0.5), 0 1px 2px rgba(0,0,0,0.05);
        border-radius: 2px;
        min-height: 400px;
    }
    
    /* Section Headers */
    .epic-header {
        background-color: #dbe4ee;
        color: #2b3a4a;
        padding: 4px 8px;
        font-weight: bold;
        border: 1px solid #a0aab5;
        border-bottom: none;
        font-size: 12px;
        text-transform: uppercase;
    }

    /* Alert Box for AI Insight */
    .epic-alert {
        background-color: #fff9d6; 
        border: 1px solid #e2c044; 
        padding: 8px; 
        color: #333;
        font-size: 13px;
        margin-bottom: 15px;
    }
    
    /* Hide standard Streamlit header and footer to make it look like a desktop app */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- 2. The Patient Banner ---
st.markdown('<div class="epic-banner">Doe, John (M, 78) | MRN: 9482011 | Admitted: 08/21/2026 | DX: Sepsis, Unspecified | Code Status: Full Code</div>', unsafe_allow_html=True)

# --- 3. Layout: 3 Columns ---
col1, col2, col3 = st.columns([1, 1.2, 1.2])

# --- 4. Column 1: EHR Context & Notes ---
with col1:
    st.markdown('<div class="epic-header">Chart Review & Data</div>', unsafe_allow_html=True)
    st.markdown('<div class="epic-panel">', unsafe_allow_html=True)
    
    st.markdown("**Prior to Admission Meds:**")
    st.code("1. Lisinopril 10mg Daily\n2. Metformin 500mg BID", language="text")
    
    st.markdown("**Current Inpatient Meds:**")
    st.code("1. Lisinopril 10mg Daily\n2. Metformin 500mg BID\n3. Quetiapine 25mg QHS", language="text")
    
    st.markdown("**Latest Progress Note (HD#3):**")
    unstructured_note = st.text_area("", "Pt extubated yesterday. Overnight, developed severe agitation, pulling at lines. CAM-ICU positive. Geriatrics consulted, recommended Quetiapine 25mg QHS PRN for hyperactive delirium. Pt calmer this morning.", height=120)
    
    st.markdown('</div>', unsafe_allow_html=True)

# --- 5. Column 2: AI Logic Engine (Qualified Health) ---
with col2:
    st.markdown('<div class="epic-header">Qualified Health: Background Processing</div>', unsafe_allow_html=True)
    st.markdown('<div class="epic-panel">', unsafe_allow_html=True)
    
    run_agent = st.button("Run Deprescribing Protocol")
    agent_output = st.empty()
    
    if run_agent:
        with st.spinner("Executing FHIR cross-reference and NLP note analysis..."):
            time.sleep(2) # Simulate API latency
            
            simulated_llm_response = {
                "indication_found": True,
                "acute_trigger": "Hyperactive ICU delirium",
                "chronic_continuation_recommended": False,
                "action_recommendation": "Eligible for Deprescribing",
                "draft_discharge_rationale": "Quetiapine 25mg was initiated for acute hyperactive delirium in the ICU. As delirium has resolved, this medication is safely discontinued prior to discharge."
            }
            agent_output.json(simulated_llm_response)
    st.markdown('</div>', unsafe_allow_html=True)

# --- 6. Column 3: The Discharge Reconcile UI ---
with col3:
    st.markdown('<div class="epic-header">Discharge Medication Reconciliation</div>', unsafe_allow_html=True)
    st.markdown('<div class="epic-panel">', unsafe_allow_html=True)
    
    if run_agent:
        st.markdown(f"""
        <div class="epic-alert">
            <strong>⚠️ Transition of Care Alert</strong><br>
            <strong>Quetiapine 25mg</strong> was flagged as a net-new CNS medication started for <em>{simulated_llm_response['acute_trigger']}</em>. No chronic indication found in chart history.
        </div>
        """, unsafe_allow_html=True)
        
        st.write("**Required Physician Action:**")
        
        # Interactive Buttons
        if st.button("✅ Accept AI Rec: Pend Discontinue Order", type="primary", use_container_width=True):
            st.success("Discontinue order pended. Will route to discharge summary.")
            
        if st.button("❌ Reject AI Rec: Keep Active & CC Pharmacy", use_container_width=True):
            st.info("Medication kept active. Routed to Unit Clinical Pharmacist for secondary review.")
                
        st.write("---")
        st.write("**Auto-Drafted Discharge Summary Snippet:**")
        st.text_area("", value=simulated_llm_response['draft_discharge_rationale'], height=100)
    else:
        st.write("Awaiting AI execution to populate discharge recommendations...")
        
    st.markdown('</div>', unsafe_allow_html=True)
