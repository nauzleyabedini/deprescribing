import streamlit as st
import json
import time

# --- 1. Vibe Coding: Custom Epic-Style CSS ---
st.set_page_config(layout="wide", page_title="QH Deprescribing Agent")
st.markdown("""
    <style>
    .main {background-color: #f3f5f8;}
    .ehr-header {background-color: #2b3a4a; color: white; padding: 10px; border-radius: 5px; font-weight: bold;}
    .panel-box {background-color: white; padding: 15px; border-radius: 5px; border: 1px solid #d1d5db; box-shadow: 0 1px 3px rgba(0,0,0,0.1);}
    .alert-box {background-color: #fff8e6; border-left: 4px solid #ffc107; padding: 10px; margin-top: 10px;}
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="ehr-header">Discharge Medication Reconciliation | Patient: Doe, John (Age: 78) | Admitted: Sepsis</div><br>', unsafe_allow_html=True)

# --- 2. Layout: 3 Columns ---
col1, col2, col3 = st.columns([1, 1, 1.2])

# --- 3. Simulated FHIR & Note Inputs (Column 1) ---
with col1:
    st.markdown('<div class="panel-box">', unsafe_allow_html=True)
    st.subheader("1. Data Ingestion")
    
    # Simulated FHIR Calls
    st.markdown("**FHIR: Condition (Chronic Baseline)**")
    st.code('{"resourceType": "Condition", "clinicalStatus": "active", "code": "Essential hypertension"}', language='json')
    
    st.markdown("**FHIR: Medication Delta**")
    st.code('{"New_Inpatient_Meds": ["Quetiapine 25mg"]}', language='json')
    
    # Unstructured Note
    st.markdown("**Unstructured Progress Note**")
    unstructured_note = st.text_area("Hospital Course (HD#3)", "Pt extubated yesterday. Overnight, developed severe agitation, pulling at lines. CAM-ICU positive. Geriatrics consulted, recommended Quetiapine 25mg QHS PRN for hyperactive delirium. Pt calmer this morning.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- 4. Logic Engine (Column 2) ---
with col2:
    st.markdown('<div class="panel-box">', unsafe_allow_html=True)
    st.subheader("2. AI Logic Engine")
    run_agent = st.button("Run Qualified Health Agent 🚀")
    
    agent_output = st.empty()
    if run_agent:
        with st.spinner("Analyzing FHIR delta and unstructured text..."):
            time.sleep(1.5) # Simulate API Latency
            
            # This is where your actual OpenAI/Anthropic API call would go.
            # Using strict JSON schema enforcement to guarantee this structure.
            simulated_llm_response = {
                "indication_found": True,
                "acute_trigger": "Hyperactive ICU delirium",
                "chronic_continuation_recommended": False,
                "action_recommendation": "Eligible for Deprescribing",
                "draft_discharge_rationale": "Quetiapine 25mg was initiated during admission for acute hyperactive delirium. As delirium has resolved and no chronic indication exists, this medication is safely discontinued prior to discharge."
            }
            agent_output.json(simulated_llm_response)
    st.markdown('</div>', unsafe_allow_html=True)

# --- 5. Actionable EHR Intercept (Column 3) ---
with col3:
    st.markdown('<div class="panel-box">', unsafe_allow_html=True)
    st.subheader("3. Discharge Workflow")
    
    if run_agent:
        st.markdown(f"""
        <div class="alert-box">
            <strong>💡 AI Deprescribing Insight</strong><br>
            <strong>Quetiapine 25mg</strong> was flagged as a net-new CNS medication. <br>
            Context: <em>{simulated_llm_response['acute_trigger']}</em>.
        </div>
        """, unsafe_allow_html=True)
        
        st.write("---")
        
        # Interactive Buttons
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("✅ Pend Discontinue Order", type="primary"):
                st.success("Discontinue order pended for signature.")
        with col_b:
            if st.button("⚠️ Reject & CC Pharmacy"):
                st.info("Routed to Unit Clinical Pharmacist.")
                
        st.write("---")
        
        # Auto-Drafted Documentation
        st.text_area("Draft Discharge Summary Snippet:", value=simulated_llm_response['draft_discharge_rationale'], height=100)
    else:
        st.info("Awaiting agent execution...")
        
    st.markdown('</div>', unsafe_allow_html=True)
