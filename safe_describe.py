import streamlit as st
import time

# --- 1. Basic Setup & State Management ---
st.set_page_config(layout="wide", page_title="Epic Hyperspace - Discharge Med Rec", initial_sidebar_state="expanded")

# Initialize session states for dynamic demo control
if "reconciled" not in st.session_state:
    st.session_state.reconciled = False
if "med_status" not in st.session_state:
    st.session_state.med_status = "default"
if "animation_played" not in st.session_state:
    st.session_state.animation_played = False

def reset_demo():
    st.session_state.reconciled = False
    st.session_state.med_status = "default"
    st.session_state.animation_played = False

# --- Demo Control Panel (Sidebar) ---
with st.sidebar:
    st.markdown("### 🎛️ Demo Control Panel")
    st.markdown("Select the patient scenario to demonstrate dynamic AI reasoning.")
    scenario = st.radio(
        "Patient Scenario:",
        [
            "1. Chronic Benzo (Safe to Continue)",
            "2. Acute Antipsychotic, Low Freq (Auto D/C)",
            "3. Acute Benzo, High Freq (Auto Taper)"
        ],
        on_change=reset_demo
    )

# --- 2. Injecting CSS for Light-Themed Epic UI ---
st.markdown("""
<style>
.stApp, [data-testid="stAppViewContainer"] { background-color: #e2e6ea !important; }
.stApp, p, label, li, td, th { font-family: 'Tahoma', 'Segoe UI', Arial, sans-serif !important; color: #000000 !important; }
.material-symbols-rounded, [data-testid*="Icon"] { font-family: 'Material Symbols Rounded' !important; }
header {visibility: hidden;}
[data-testid="stToolbar"] {display: none;}
.epic-table { width: 100%; border-collapse: collapse; margin-top: 10px; margin-bottom: 15px; font-size: 13px; background-color: #ffffff; }
.epic-table th { background-color: #e2e6ea !important; color: #000000 !important; border: 1px solid #999999 !important; padding: 6px; text-align: left; font-weight: bold; }
.epic-table td { border: 1px solid #999999 !important; padding: 8px 6px; color: #000000 !important; }
.pended-order { border: 1px solid #aaaaaa; background-color: #f8f9fa; padding: 10px; border-radius: 3px; margin-bottom: 5px; }
button { border-radius: 2px !important; font-weight: bold !important; padding: 4px 10px !important; font-family: 'Tahoma', 'Segoe UI', Arial, sans-serif !important; }
button[kind="secondary"] { background-color: #f0f2f5 !important; border: 1px solid #555555 !important; }
button[kind="secondary"] * { color: #000000 !important; }
button[kind="primary"] { background-color: #204d74 !important; border-color: #122b40 !important; }
button[kind="primary"] * { color: #ffffff !important; }
[data-testid="stExpander"] { border: 1px solid #aaaaaa !important; border-radius: 3px !important; margin-top: 5px; margin-bottom: 10px; background-color: #ffffff !important; }
[data-testid="stExpander"] summary { background-color: #f0f2f5 !important; }
[data-testid="stExpander"] summary p { color: #0056b3 !important; font-weight: bold !important; }
[class^="st-key-epic_window_"] { background-color: #ffffff !important; border: 1px solid #888888 !important; border-radius: 0px !important; padding: 15px !important; box-shadow: 2px 2px 5px rgba(0,0,0,0.15); }
.ai-trace-box { background-color: #1e1e1e; color: #4af626; font-family: 'Courier New', Courier, monospace; font-size: 11px; padding: 12px; border-radius: 4px; line-height: 1.6; margin-bottom: 15px; box-shadow: inset 0 0 10px rgba(0,0,0,0.5); }
</style>
""", unsafe_allow_html=True)

# --- 3. Storyboard Top Banner ---
st.markdown("""
<div style="background-color: #b9c9d9; padding: 10px 15px; border-bottom: 4px solid #d9534f; margin-top: -50px; margin-bottom: 10px; border-radius: 3px; color: #000000; font-family: Tahoma, sans-serif;">
<span style="font-weight: bold; font-size: 14px; margin-right: 20px;">DOE, JOHN (M, 78 yo)</span>
<span style="font-size: 13px; margin-right: 20px;">MRN: 9482011</span>
<span style="font-size: 13px; margin-right: 20px;">DOB: 11/20/1947</span>
<span style="font-size: 13px; margin-right: 20px;">Bed: MS-4 312-2</span>
<span style="font-size: 13px; margin-right: 20px;">Code: Full Code</span>
<span style="font-size: 13px;">Allergies: <span style="color: #cc0000; font-weight: bold;">Penicillin</span></span>
</div>
""", unsafe_allow_html=True)

# --- 4. Hyperspace Navigation Tabs ---
st.markdown("""
<div style="display: flex; gap: 4px; padding: 0 10px; border-bottom: 2px solid #aaaaaa; margin-bottom: 15px; font-family: Tahoma, sans-serif;">
<div style="background-color: #e2e6ea; color: #333333; padding: 6px 15px; border: 1px solid #aaaaaa; border-bottom: none; border-radius: 4px 4px 0 0; font-size: 13px;">Chart Review</div>
<div style="background-color: #e2e6ea; color: #333333; padding: 6px 15px; border: 1px solid #aaaaaa; border-bottom: none; border-radius: 4px 4px 0 0; font-size: 13px;">Notes</div>
<div style="background-color: #ffffff; color: #000000; font-weight: bold; padding: 6px 15px; border: 1px solid #aaaaaa; border-bottom: 2px solid #ffffff; border-radius: 4px 4px 0 0; font-size: 13px; position: relative; top: 2px;">Discharge Navigator: Med Rec</div>
<div style="background-color: #e2e6ea; color: #333333; padding: 6px 15px; border: 1px solid #aaaaaa; border-bottom: none; border-radius: 4px 4px 0 0; font-size: 13px;">Orders</div>
</div>
""", unsafe_allow_html=True)

# --- 5. Workspace Layout ---
col1, spacer, col2 = st.columns([1.2, 0.05, 1.2])

# ----- WINDOW 1: Epic Discharge Med Rec Grid -----
with col1:
    with st.container(key="epic_window_1"):
        st.markdown("""
<div style="background-color: #c9d6e2; color: #000000; font-weight: bold; padding: 8px 12px; border-bottom: 1px solid #888888; font-size: 13px; text-transform: uppercase; margin: -15px -15px 15px -15px; font-family: Tahoma, sans-serif;">
Discharge Medication Reconciliation Grid
</div>
<p style="color: #000000; font-size: 13px; margin-top: 0;">Review home and hospital medications prior to generating discharge prescriptions.</p>
""", unsafe_allow_html=True)
        
        # Dynamic Med Rec Table Based on Scenario
        if "1" in scenario:
            target_med = "Lorazepam 1mg PO BID"
            source = "Home Med"
            row_color = "#ffffff"
            text_color = "#000000"
        elif "2" in scenario:
            target_med = "Quetiapine 25mg PO QHS"
            source = "<em>New Inpatient Start (HD#3)</em>"
            row_color = "#ffeaea"
            text_color = "#aa0000"
        else:
            target_med = "Lorazepam 1mg PO TID"
            source = "<em>New Inpatient Start (HD#2)</em>"
            row_color = "#ffeaea"
            text_color = "#aa0000"

        st.markdown(f"""
<table class="epic-table">
<tr><th>Medication</th><th>Admission Source</th><th>Discharge Plan</th></tr>
<tr><td><strong>Lisinopril 10mg</strong> PO Daily</td><td>Home Med</td><td style="color: #006600; font-weight: bold;">[X] Continue</td></tr>
<tr><td><strong>Metformin 500mg</strong> PO BID</td><td>Home Med</td><td style="color: #006600; font-weight: bold;">[X] Continue</td></tr>
<tr style="background-color: {row_color};">
<td><strong>{target_med}</strong></td>
<td style="color: {text_color};">{source}</td>
<td style="color: {text_color}; font-weight: bold;">[X] Continue (Auto-selected)</td>
</tr>
</table>
""", unsafe_allow_html=True)
        
        st.write("") 
        if not st.session_state.reconciled:
            if st.button("Complete Med Rec & Continue to Orders ⚡", type="primary", use_container_width=True):
                st.session_state.reconciled = True
                st.session_state.med_status = "default"
                st.rerun()
        else:
            st.success("Med Rec submitted.")
            if st.button("Reset Simulation"):
                reset_demo()
                st.rerun()

# ----- WINDOW 2: Discharge Orders & AI Trace -----
with col2:
    with st.container(key="epic_window_2"):
        st.markdown("""
<div style="background-color: #c9d6e2; color: #000000; font-weight: bold; padding: 8px 12px; border-bottom: 1px solid #888888; font-size: 13px; text-transform: uppercase; margin: -15px -15px 15px -15px; font-family: Tahoma, sans-serif;">
Discharge Orders: Awaiting Signature
</div>
""", unsafe_allow_html=True)
        
        if st.session_state.reconciled:
            # --- AI VISUALIZER ANIMATION (Only runs once!) ---
            if not st.session_state.animation_played:
                trace_box = st.empty()
                logs = [
                    "📡 Initializing Qualified Health Agent...",
                    "🔄 Querying FHIR API: Comparing Pre-Admit MedicationStatement vs Active Inpatient MedicationRequest...",
                    "✅ Medication Delta Processed.",
                    "📊 Querying MAR (MedicationAdministration) for 24-hour administration frequency...",
                    "📄 Fetching DocumentReference: NLP scanning CAM-ICU, Progress, and Consult notes...",
                    "🧠 Executing Clinical Logic Gate (Chronic vs. Acute / Low Freq vs. High Freq)...",
                    "⚡ Generating tailored workflow intervention and patient instructions..."
                ]
                current_log = ""
                for log in logs:
                    current_log += f"> {log}<br>"
                    trace_box.markdown(f'<div class="ai-trace-box">{current_log}</div>', unsafe_allow_html=True)
                    time.sleep(0.5)
                time.sleep(0.5)
                trace_box.empty()
                st.session_state.animation_played = True 

            # ==========================================
            # SCENARIO 1: CHRONIC BENZO (SAFE)
            # ==========================================
            if "1" in scenario:
                st.success("✔️ All orders validated. No safety intercepts required.")
                st.markdown("<p style='font-size:13px;'>The AI verified via FHIR that Lorazepam 1mg is an established chronic home medication pre-hospitalization. No deprescribing action or taper plan is required.</p>", unsafe_allow_html=True)
                
                st.write("")
                if st.button("Sign Orders & Close Encounter", type="primary", use_container_width=True):
                    st.success("Orders signed successfully.")

            # ==========================================
            # SCENARIO 2: ACUTE ANTIPSYCHOTIC (AUTO D/C)
            # ==========================================
            elif "2" in scenario:
                if st.session_state.med_status in ["default", "discontinued"]:
                    st.markdown("""
<p style="color: #006600; font-weight: bold; font-size: 13px; margin-bottom: 5px;">1 Order Pended for Review</p>
<div class="pended-order">
    <p style="margin: 0; font-size: 13px; font-weight: bold;"><span style="color: #aa0000; text-decoration: line-through;">Quetiapine (SEROQUEL) 25mg Tablet</span></p>
    <p style="margin: 0; font-size: 12px; color: #333333;"><strong>Action:</strong> <span style="color: #aa0000; font-weight: bold;">Discontinue</span></p>
    <p style="margin: 0; font-size: 11px; color: #666666;">Route: Oral | Frequency: Nightly</p>
</div>
""", unsafe_allow_html=True)
                    
                    with st.expander("💡 View AI Clinical Rationale"):
                        st.markdown("<p style='font-size: 12px; margin: 0; padding: 5px;'><strong>Logic Path Executed:</strong> FHIR delta confirms inpatient start. NLP note analysis confirms initiation for <em>Acute ICU Delirium</em> which is now resolved. MAR check shows low dose/infrequent administration. <strong>Recommendation:</strong> Safe to discontinue abruptly to mitigate post-discharge fall risk.</p>", unsafe_allow_html=True)
                        if st.button("Undo & Keep Active", key="undo_btn2"):
                            st.session_state.med_status = "kept"
                            st.rerun()
                    
                    addendum_text = "Quetiapine 25mg was initiated during the hospitalization for acute hyperactive delirium. As the delirium has fully resolved and cognitive baseline is regained, this medication has been discontinued prior to discharge to mitigate fall risks. Patient was instructed on self-monitoring for mild rebound insomnia."
                    avs_text = "We are stopping the medicine Seroquel (quetiapine) that you took in the hospital. You do not need it anymore. You might have some trouble sleeping, feel sick to your stomach, or feel dizzy for a few days. This is normal and should go away. Call your doctor if you feel very sick or if it does not get better."

                else: # Override state
                    st.warning("Override logged. Routing to unit pharmacist.")
                    st.markdown("""
<div class="pended-order" style="border-color: #d39e00; background-color: #fff4ce;">
    <p style="margin: 0; font-size: 13px; font-weight: bold;">Quetiapine (SEROQUEL) 25mg Tablet</p>
    <p style="margin: 0; font-size: 12px; color: #333333;"><strong>Action:</strong> <span style="color: #006600; font-weight: bold;">Continue</span></p>
</div>
""", unsafe_allow_html=True)
                    if st.button("Re-Apply Auto-Discontinue"):
                        st.session_state.med_status = "discontinued"
                        st.rerun()
                    
                    addendum_text = "Quetiapine 25mg was initiated during the hospitalization for acute hyperactive delirium. This medication is being continued at discharge for ***. Please assess for ongoing indication and taper plan at outpatient follow-up."
                    avs_text = "You will keep taking Seroquel (quetiapine) at home. Please talk to your doctor at your next visit to see if you still need this medicine."

                st.markdown('<hr style="margin: 15px 0; border: 0; border-top: 1px solid #dddddd;"><p style="font-weight: bold; font-size: 13px; margin-bottom: 5px;">SmartText: Discharge Summary Addendum</p>', unsafe_allow_html=True)
                st.text_area("Summary Addendum", value=addendum_text, height=90, label_visibility="collapsed", key="text2_summ")
                
                st.markdown('<p style="font-weight: bold; font-size: 13px; margin-top: 10px; margin-bottom: 5px;">SmartText: Patient After Visit Summary (AVS)</p>', unsafe_allow_html=True)
                st.text_area("AVS Text", value=avs_text, height=85, label_visibility="collapsed", key="text2_avs")

                if st.button("Sign Orders & Close Encounter", type="primary", use_container_width=True, key="sign2"):
                    st.success("Orders signed successfully.")

            # ==========================================
            # SCENARIO 3: ACUTE BENZO (AUTO TAPER)
            # ==========================================
            elif "3" in scenario:
                if st.session_state.med_status in ["default", "tapered"]:
                    st.markdown("""
<p style="color: #006600; font-weight: bold; font-size: 13px; margin-bottom: 5px;">1 Order Pended for Review</p>
<div class="pended-order" style="border-left: 5px solid #0056b3;">
    <p style="margin: 0; font-size: 13px; font-weight: bold; color: #0056b3;">Lorazepam (ATIVAN) Taper Protocol</p>
    <p style="margin: 0; font-size: 12px; color: #333333;"><strong>Action:</strong> <span style="color: #0056b3; font-weight: bold;">Initiate Outpatient Taper</span></p>
    <p style="margin: 0; font-size: 11px; color: #666666;">Instructions: Decrease total daily dose by 25% every 7 days until discontinued.</p>
</div>
<p style="font-size: 11px; color: #666; font-style: italic; margin-top: -3px;">*Clinical Pharmacist flagged for review.*</p>
""", unsafe_allow_html=True)
                    
                    with st.expander("💡 View AI Clinical Rationale"):
                        st.markdown("<p style='font-size: 12px; margin: 0; padding: 5px;'><strong>Logic Path Executed:</strong> FHIR confirms inpatient start. MAR analysis reveals high-frequency administration (>2 doses daily for 48+ hours). <strong>Recommendation:</strong> Abrupt discontinuation poses severe withdrawal risk (seizures, rebound anxiety). Auto-pending standard 25% weekly step-down taper and alerting pharmacy for pre-discharge safety review.</p>", unsafe_allow_html=True)
                        if st.button("Undo & Stop Abruptly (Not Recommended)", key="undo_btn3"):
                            st.session_state.med_status = "abrupt"
                            st.rerun()
                    
                    addendum_text = "Lorazepam 1mg TID was initiated during the hospitalization. Patient received >2 doses daily over the last 48 hours. To mitigate risk of unmonitored benzodiazepine withdrawal, abrupt discontinuation is contraindicated. A structured taper has been prescribed (decrease daily dose by 25% every week). Patient instructed to seek emergency care for severe autonomic symptoms. Pharmacy notified for discharge coordination."
                    avs_text = "You were given a medicine called Ativan (lorazepam) in the hospital to help you. It is NOT safe to stop taking this all at once. You must slowly take less of it over time.\n\nFollow the new directions on your pill bottle exactly.\n\nCall your doctor if you feel very nervous, shaky, or your heart beats fast.\nGo to the Emergency Room RIGHT AWAY if you have a seizure, see things that are not there, or feel very confused."

                else: # Override state (Abrupt Stop)
                    st.error("⚠️ Warning: Abrupt discontinuation of frequent benzodiazepines carries seizure risk. Override logged.")
                    st.markdown("""
<div class="pended-order" style="border-color: #aa0000; background-color: #ffeaea;">
    <p style="margin: 0; font-size: 13px; font-weight: bold;"><span style="color: #aa0000; text-decoration: line-through;">Lorazepam (ATIVAN) 1mg Tablet</span></p>
    <p style="margin: 0; font-size: 12px; color: #333333;"><strong>Action:</strong> <span style="color: #aa0000; font-weight: bold;">Discontinue (Abrupt)</span></p>
</div>
""", unsafe_allow_html=True)
                    if st.button("Re-Apply Taper Protocol"):
                        st.session_state.med_status = "tapered"
                        st.rerun()
                    
                    addendum_text = "Lorazepam 1mg TID was initiated during the hospitalization and is being abruptly discontinued at discharge due to ***. Patient is at elevated risk for unmonitored benzodiazepine withdrawal. Please monitor closely outpatient."
                    avs_text = "We are stopping the medicine Ativan (lorazepam) today. Stopping this medicine suddenly can make you feel sick. Go to the Emergency Room RIGHT AWAY if you have a seizure, see things that are not there, or feel very confused."

                st.markdown('<hr style="margin: 15px 0; border: 0; border-top: 1px solid #dddddd;"><p style="font-weight: bold; font-size: 13px; margin-bottom: 5px;">SmartText: Discharge Summary Addendum</p>', unsafe_allow_html=True)
                st.text_area("Summary Addendum", value=addendum_text, height=90, label_visibility="collapsed", key="text3_summ")
                
                st.markdown('<p style="font-weight: bold; font-size: 13px; margin-top: 10px; margin-bottom: 5px;">SmartText: Patient After Visit Summary (AVS)</p>', unsafe_allow_html=True)
                st.text_area("AVS Text", value=avs_text, height=115, label_visibility="collapsed", key="text3_avs")

                if st.button("Sign Orders & Close Encounter", type="primary", use_container_width=True, key="sign3"):
                    st.success("Orders signed successfully.")
                    
        else:
            st.info("Awaiting Med Rec submission... Complete the grid on the left to generate discharge orders.")
