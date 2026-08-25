import streamlit as st
import time

# --- 1. Basic Setup & State Management ---
st.set_page_config(layout="wide", page_title="Epic Hyperspace - Discharge Med Rec", initial_sidebar_state="expanded")

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
    st.markdown("Select the patient scenario to demonstrate dynamic AI reasoning based on safety guidelines.")
    scenario = st.radio(
        "Patient Scenario:",
        [
            "1. Chronic Benzo (Safe to Continue)",
            "2. Haldol PRN + Hospice (Palliative Exception)",
            "3. Quetiapine 12.5mg Scheduled (Low Risk D/C)",
            "4. Quetiapine PRN (Infrequent MAR usage)",
            "5. Lorazepam + Seizure Hx (High Risk Taper & PCP Handoff)",
            "6. Alprazolam (Rapid Dependence Warning)"
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
            target_med, source, row_color, text_color = "Lorazepam 1mg PO BID", "Home Med", "#ffffff", "#000000"
        elif "2" in scenario:
            target_med, source, row_color, text_color = "Haloperidol 0.5mg PO Q4H PRN", "<em>New Inpatient Start (HD#5)</em>", "#ffeaea", "#aa0000"
        elif "3" in scenario:
            target_med, source, row_color, text_color = "Quetiapine 12.5mg PO QHS", "<em>New Inpatient Start (11 days ago)</em>", "#ffeaea", "#aa0000"
        elif "4" in scenario:
            target_med, source, row_color, text_color = "Quetiapine 12.5mg PO Q6H PRN", "<em>New Inpatient Start (5 days ago)</em>", "#ffeaea", "#aa0000"
        elif "5" in scenario:
            target_med, source, row_color, text_color = "Lorazepam 1mg PO TID", "<em>New Inpatient Start (5 days ago)</em>", "#ffeaea", "#aa0000"
        else: # Scenario 6
            target_med, source, row_color, text_color = "Alprazolam 0.5mg PO QHS", "<em>New Inpatient Start (2 weeks ago)</em>", "#ffeaea", "#aa0000"

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
            # --- DYNAMIC AI VISUALIZER ANIMATION ---
            if not st.session_state.animation_played:
                trace_box = st.empty()
                logs = ["📡 Initializing Qualified Health Agent...", "🔄 Querying FHIR API: Evaluating Medication Delta..."]
                
                if "1" in scenario:
                    logs.extend(["✅ Match found in pre-admission medication history.", "🧠 Logic Gate: Chronic medication. No intervention required."])
                elif "2" in scenario:
                    logs.extend(["📊 MAR check: Administered 3-4x daily.", "📄 NLP scanning Palliative Care consult note...", "✅ Exception found: Patient transitioning to Hospice.", "🧠 Logic Gate: Palliative exception applied. Safe to continue."])
                elif "3" in scenario:
                    logs.extend(["📄 NLP note scan: Indication is ICU Delirium.", "📊 MAR check: 12.5mg Scheduled QHS for 11 days.", "🧠 Logic Gate: Short course, low-dose, low discontinuation syndrome risk. Auto-pending abrupt stop."])
                elif "4" in scenario:
                    logs.extend(["📊 MAR check: PRN administration (0-2 doses/day) for 5 days.", "🧠 Logic Gate: Below 30-day threshold, infrequent usage. Safe to stop abruptly."])
                elif "5" in scenario:
                    logs.extend(["📄 NLP note scan: Indication is Agitation (now resolved).", "⚠️ Problem List scan: Identifying high-risk features...", "🚨 ALERT: History of Seizures identified.", "🧠 Logic Gate: High risk for unmonitored withdrawal. Generating conservative taper and pharmacy consult."])
                elif "6" in scenario:
                    logs.extend(["⚠️ Pharmacologic check: Agent is Alprazolam.", "🧠 Logic Gate: High risk of rapid dependence (2-4 weeks). Abrupt stop contraindicated. Routing to pharmacy for long-acting substitution taper."])

                logs.append("⚡ Generating tailored workflow intervention...")
                
                current_log = ""
                for log in logs:
                    current_log += f"> {log}<br>"
                    trace_box.markdown(f'<div class="ai-trace-box">{current_log}</div>', unsafe_allow_html=True)
                    time.sleep(0.5)
                time.sleep(0.5)
                trace_box.empty()
                st.session_state.animation_played = True 

            # ==========================================
            # SCENARIO 1: CHRONIC BENZO 
            # ==========================================
            if "1" in scenario:
                st.success("✔️ All orders validated. No safety intercepts required.")
                with st.expander("💡 View AI Clinical Rationale"):
                    st.markdown("<p style='font-size:12px; margin:0; padding:5px;'>The AI verified via FHIR that Lorazepam 1mg is an established chronic home medication pre-hospitalization. No deprescribing action or taper plan is required.</p>", unsafe_allow_html=True)
                st.write("")
                if st.button("Sign Orders & Close Encounter", type="primary", use_container_width=True):
                    st.success("Orders signed successfully.")

            # ==========================================
            # SCENARIO 2: HALDOL + HOSPICE
            # ==========================================
            elif "2" in scenario:
                st.success("✔️ All orders validated. Guideline exception applied.")
                with st.expander("💡 View AI Clinical Rationale (Palliative Exception)"):
                    st.markdown("<p style='font-size:12px; margin:0; padding:5px;'><strong>Inputs Collected:</strong> New inpatient start of Haloperidol 0.5mg PRN. Administered 3-4x daily.<br><strong>Logic Path Executed:</strong> NLP scanning of the Palliative Care consult note confirms the patient is transitioning to Hospice for comfort care. Haloperidol for terminal agitation is a guideline-supported continuation. Deprescribing algorithm safely bypassed.</p>", unsafe_allow_html=True)
                st.write("")
                if st.button("Sign Orders & Close Encounter", type="primary", use_container_width=True):
                    st.success("Orders signed successfully.")

            # ==========================================
            # SCENARIO 3: QUETIAPINE SCHEDULED (11 DAYS)
            # ==========================================
            elif "3" in scenario:
                if st.session_state.med_status in ["default", "discontinued"]:
                    st.markdown("""
<div class="pended-order">
    <p style="margin: 0; font-size: 13px; font-weight: bold;"><span style="color: #aa0000; text-decoration: line-through;">Quetiapine (SEROQUEL) 12.5mg Tablet</span></p>
    <p style="margin: 0; font-size: 12px;"><strong>Action:</strong> <span style="color: #aa0000; font-weight: bold;">Discontinue</span></p>
</div>
""", unsafe_allow_html=True)
                    with st.expander("💡 View AI Clinical Rationale"):
                        st.markdown("<p style='font-size: 12px; margin: 0; padding: 5px;'><strong>Guideline Path 3 (Step 1):</strong> Short-term/low-dose use for delirium (11 days). Rebound burden is low at 12.5mg. Because 12.5mg cannot be easily tapered without tablet splitting, an abrupt stop with explicit AVS symptom education is appropriate.</p>", unsafe_allow_html=True)
                        if st.button("Undo & Keep Active", key="undo_btn3"):
                            st.session_state.med_status = "kept"
                            st.rerun()
                    addendum_text = "Quetiapine 12.5mg QHS was initiated 11 days ago for delirium. Delirium is resolved. Medication safely discontinued prior to discharge."
                    avs_text = "We are stopping Seroquel (quetiapine). You might have some trouble sleeping or feel dizzy for a few days. Call your doctor if it does not get better."
                else: 
                    st.warning("Override logged.")
                    st.markdown('<div class="pended-order" style="border-color: #d39e00; background-color: #fff4ce;"><p style="margin: 0; font-size: 13px; font-weight: bold;">Quetiapine (SEROQUEL) 12.5mg Tablet</p><p style="margin: 0; font-size: 12px;"><strong>Action:</strong> <span style="color: #006600; font-weight: bold;">Continue</span></p></div>', unsafe_allow_html=True)
                    if st.button("Re-Apply Auto-Discontinue"):
                        st.session_state.med_status = "discontinued"
                        st.rerun()
                    addendum_text = "Quetiapine 12.5mg was initiated for delirium. Continued at discharge for ***. Please assess for ongoing indication at outpatient follow-up."
                    avs_text = "Keep taking Seroquel as directed. Talk to your doctor at your next visit about this medicine."

                st.markdown('<hr style="margin: 15px 0; border: 0; border-top: 1px solid #dddddd;"><p style="font-weight: bold; font-size: 13px; margin-bottom: 5px;">Discharge Summary Addendum</p>', unsafe_allow_html=True)
                st.text_area("Summary Addendum", value=addendum_text, height=65, label_visibility="collapsed", key="text3_summ")
                st.markdown('<p style="font-weight: bold; font-size: 13px; margin-top: 10px; margin-bottom: 5px;">Patient AVS Instructions</p>', unsafe_allow_html=True)
                st.text_area("AVS Text", value=avs_text, height=65, label_visibility="collapsed", key="text3_avs")

            # ==========================================
            # SCENARIO 4: QUETIAPINE PRN (5 DAYS)
            # ==========================================
            elif "4" in scenario:
                if st.session_state.med_status in ["default", "discontinued"]:
                    st.markdown("""
<div class="pended-order">
    <p style="margin: 0; font-size: 13px; font-weight: bold;"><span style="color: #aa0000; text-decoration: line-through;">Quetiapine (SEROQUEL) 12.5mg Tablet</span></p>
    <p style="margin: 0; font-size: 12px;"><strong>Action:</strong> <span style="color: #aa0000; font-weight: bold;">Discontinue</span></p>
</div>
""", unsafe_allow_html=True)
                    with st.expander("💡 View AI Clinical Rationale"):
                        st.markdown("<p style='font-size: 12px; margin: 0; padding: 5px;'><strong>Guideline Path 3 (Step 1):</strong> Short-term PRN use. MAR reflects infrequent administration (0-2x/day) for only 5 days. Safe to discontinue abruptly without tapering.</p>", unsafe_allow_html=True)
                        if st.button("Undo & Keep Active", key="undo_btn4"):
                            st.session_state.med_status = "kept"
                            st.rerun()
                    addendum_text = "Quetiapine 12.5mg PRN was initiated 5 days ago. Patient used infrequently. Safely discontinued at discharge."
                    avs_text = "We are stopping the as-needed Seroquel (quetiapine) you took in the hospital. You do not need this at home."
                else: 
                    st.warning("Override logged.")
                    st.markdown('<div class="pended-order" style="border-color: #d39e00; background-color: #fff4ce;"><p style="margin: 0; font-size: 13px; font-weight: bold;">Quetiapine (SEROQUEL) 12.5mg Tablet</p><p style="margin: 0; font-size: 12px;"><strong>Action:</strong> <span style="color: #006600; font-weight: bold;">Continue</span></p></div>', unsafe_allow_html=True)
                    if st.button("Re-Apply Auto-Discontinue"):
                        st.session_state.med_status = "discontinued"
                        st.rerun()
                    addendum_text = "Quetiapine PRN continued at discharge for ***."
                    avs_text = "Keep taking Seroquel as needed."

                st.markdown('<hr style="margin: 15px 0; border: 0; border-top: 1px solid #dddddd;"><p style="font-weight: bold; font-size: 13px; margin-bottom: 5px;">Discharge Summary Addendum</p>', unsafe_allow_html=True)
                st.text_area("Summary Addendum", value=addendum_text, height=65, label_visibility="collapsed", key="text4_summ")
                st.markdown('<p style="font-weight: bold; font-size: 13px; margin-top: 10px; margin-bottom: 5px;">Patient AVS Instructions</p>', unsafe_allow_html=True)
                st.text_area("AVS Text", value=avs_text, height=65, label_visibility="collapsed", key="text4_avs")

            # ==========================================
            # SCENARIO 5: LORAZEPAM + SEIZURES (HIGH RISK)
            # ==========================================
            elif "5" in scenario:
                if st.session_state.med_status in ["default", "tapered"]:
                    st.markdown("""
<div class="pended-order" style="border-left: 5px solid #0056b3;">
    <p style="margin: 0; font-size: 13px; font-weight: bold; color: #0056b3;">Lorazepam (ATIVAN) Taper Protocol</p>
    <p style="margin: 0; font-size: 12px;"><strong>Action:</strong> <span style="color: #0056b3; font-weight: bold;">Initiate Taper + Pharmacy Consult</span></p>
</div>
<div class="pended-order" style="border-left: 5px solid #28a745; background-color: #e8f5e9;">
    <p style="margin: 0; font-size: 12px; color: #000;"><strong>[Action]</strong> Draft In-Basket Message to PCP for close follow-up.</p>
</div>
""", unsafe_allow_html=True)
                    with st.expander("💡 View AI Clinical Rationale (High-Risk Benzo)"):
                        st.markdown("""
                        <p style='font-size: 12px; margin: 0; padding: 5px;'>
                        <strong>Guideline Path 1 (Step 2 - High Risk):</strong> Patient has a history of seizures. 
                        This patient is NOT appropriate for an unmonitored abrupt stop. Because withdrawal seizures could occur after discharge, a highly conservative taper has been drafted, pharmacy has been consulted for pre-discharge review, and an explicit hand-off message is queued for the PCP.
                        </p>
                        """, unsafe_allow_html=True)
                        if st.button("Undo & Stop Abruptly (DANGEROUS)", key="undo_btn5"):
                            st.session_state.med_status = "abrupt"
                            st.rerun()
                    addendum_text = "Lorazepam 1mg TID was initiated for agitation 5 days ago. Due to patient's history of seizures, abrupt discontinuation is unsafe. A conservative outpatient taper has been ordered and pharmacy consulted. PCP notified via in-basket. Please monitor closely for withdrawal seizures or autonomic instability."
                    avs_text = "It is NOT safe to stop taking Ativan (lorazepam) suddenly because of your health history. You must follow the exact instructions to take less of it over time.\n\nGo to the Emergency Room RIGHT AWAY if you have a seizure, start shaking badly, or feel confused."
                else: 
                    st.error("⚠️ HIGH RISK: Abrupt discontinuation in a patient with seizure history is dangerous.")
                    st.markdown('<div class="pended-order" style="border-color: #aa0000; background-color: #ffeaea;"><p style="margin: 0; font-size: 13px; font-weight: bold;"><span style="color: #aa0000; text-decoration: line-through;">Lorazepam 1mg Tablet</span></p><p style="margin: 0; font-size: 12px;"><strong>Action:</strong> <span style="color: #aa0000; font-weight: bold;">Discontinue (Abrupt)</span></p></div>', unsafe_allow_html=True)
                    if st.button("Re-Apply Taper & PCP Handoff"):
                        st.session_state.med_status = "tapered"
                        st.rerun()
                    addendum_text = "Lorazepam 1mg TID discontinued abruptly. Patient at high risk for withdrawal seizures due to prior history. Please monitor closely outpatient."
                    avs_text = "We are stopping Ativan today. Go to the ER right away if you have a seizure."

                st.markdown('<hr style="margin: 15px 0; border: 0; border-top: 1px solid #dddddd;"><p style="font-weight: bold; font-size: 13px; margin-bottom: 5px;">Discharge Summary Addendum</p>', unsafe_allow_html=True)
                st.text_area("Summary Addendum", value=addendum_text, height=90, label_visibility="collapsed", key="text5_summ")
                st.markdown('<p style="font-weight: bold; font-size: 13px; margin-top: 10px; margin-bottom: 5px;">Patient AVS Instructions</p>', unsafe_allow_html=True)
                st.text_area("AVS Text", value=avs_text, height=90, label_visibility="collapsed", key="text5_avs")

            # ==========================================
            # SCENARIO 6: ALPRAZOLAM (RAPID DEPENDENCE)
            # ==========================================
            elif "6" in scenario:
                if st.session_state.med_status in ["default", "pended_consult"]:
                    st.markdown("""
<div class="pended-order" style="border-left: 5px solid #d39e00;">
    <p style="margin: 0; font-size: 13px; font-weight: bold; color: #d39e00;">Pharmacy Consult: Alprazolam Taper Review</p>
    <p style="margin: 0; font-size: 12px;"><strong>Action:</strong> <span style="color: #d39e00; font-weight: bold;">Review BEFORE Discharge</span></p>
</div>
""", unsafe_allow_html=True)
                    with st.expander("💡 View AI Clinical Rationale (Alprazolam)"):
                        st.markdown("""
                        <p style='font-size: 12px; margin: 0; padding: 5px;'>
                        <strong>Guideline Path 1 (Step 1):</strong> Agent is Alprazolam. Do NOT stop abruptly even after a 2-week course due to risk of rapid dependence. AI recommends routing to pharmacy to consider switching to a longer-acting benzo for a smoother outpatient self-taper.
                        </p>
                        """, unsafe_allow_html=True)
                        if st.button("Undo & Force Abrupt Stop", key="undo_btn6"):
                            st.session_state.med_status = "abrupt_stop"
                            st.rerun()
                    addendum_text = "Alprazolam 0.5mg QHS initiated 2 weeks ago in ICU. Due to risk of rapid dependence with this specific agent, pharmacy has been consulted prior to discharge to assist with a structured taper plan (considering long-acting transition)."
                    avs_text = "A pharmacist will speak with you before you leave the hospital about a plan to slowly stop your anxiety medicine. Do not stop taking it suddenly on your own."
                else:
                    st.error("⚠️ Warning: Abrupt stop of Alprazolam carries rapid withdrawal risk.")
                    st.markdown('<div class="pended-order" style="border-color: #aa0000; background-color: #ffeaea;"><p style="margin: 0; font-size: 13px; font-weight: bold;"><span style="color: #aa0000; text-decoration: line-through;">Alprazolam 0.5mg</span></p><p style="margin: 0; font-size: 12px;"><strong>Action:</strong> <span style="color: #aa0000; font-weight: bold;">Discontinue (Abrupt Stop)</span></p></div>', unsafe_allow_html=True)
                    if st.button("Re-Apply Pharmacy Consult"):
                        st.session_state.med_status = "pended_consult"
                        st.rerun()
                    addendum_text = "Alprazolam abruptly discontinued. Monitor for rapid withdrawal symptoms."
                    avs_text = "We are stopping Alprazolam today. Call your doctor if you feel very anxious or sick."

                st.markdown('<hr style="margin: 15px 0; border: 0; border-top: 1px solid #dddddd;"><p style="font-weight: bold; font-size: 13px; margin-bottom: 5px;">Discharge Summary Addendum</p>', unsafe_allow_html=True)
                st.text_area("Summary Addendum", value=addendum_text, height=75, label_visibility="collapsed", key="text6_summ")
                st.markdown('<p style="font-weight: bold; font-size: 13px; margin-top: 10px; margin-bottom: 5px;">Patient AVS Instructions</p>', unsafe_allow_html=True)
                st.text_area("AVS Text", value=avs_text, height=65, label_visibility="collapsed", key="text6_avs")

            # Shared Sign Orders Button for all branches
            if "1" not in scenario and "2" not in scenario:
                if st.button("Sign Orders & Close Encounter", type="primary", use_container_width=True, key="master_sign"):
                    st.success("Orders signed successfully.")
                    
        else:
            st.info("Awaiting Med Rec submission... Complete the grid on the left to generate discharge orders.")
