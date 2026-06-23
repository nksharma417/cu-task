import streamlit as st
import pandas as pd
import joblib

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Career Recommendation",
    page_icon="🎓",
    layout="centered",
)

# ── Load model ────────────────────────────────────────────────────────────────
@st.cache_resource
def load_model():
    model    = joblib.load("career_prediction_model.pkl")
    encoders = joblib.load("encoders.pkl")
    return model, encoders

model, encoders = load_model()

# ── Sidebar: step indicator ───────────────────────────────────────────────────
STEPS = ["Academic background", "Skills & interests", "Personality & hobbies"]

if "step" not in st.session_state:
    st.session_state.step = 0

def go_next(): st.session_state.step = min(st.session_state.step + 1, len(STEPS))
def go_back(): st.session_state.step = max(st.session_state.step - 1, 0)
def restart(): st.session_state.step = 0

with st.sidebar:
    st.markdown("### Your progress")
    for i, name in enumerate(STEPS):
        if i < st.session_state.step:
            st.markdown(f"✅ {name}")
        elif i == st.session_state.step:
            st.markdown(f"**▶ {name}**")
        else:
            st.markdown(f"○ {name}")

# ── Header ────────────────────────────────────────────────────────────────────
st.title("🎓 Student Career Recommendation")
st.caption("Answer a few questions and get a personalised career suggestion.")
st.divider()

# ─────────────────────────────────────────────────────────────────────────────
# STEP 0 — Academic background
# ─────────────────────────────────────────────────────────────────────────────
if st.session_state.step == 0:
    st.subheader("Step 1 · Academic background")

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input("Age", 17, 25, 20)
    with col2:
        tenth = st.number_input("10th %", 0.0, 100.0, 75.0, step=0.5, format="%.1f")
    with col3:
        twelfth = st.number_input("12th %", 0.0, 100.0, 75.0, step=0.5, format="%.1f")

    col4, col5 = st.columns(2)
    with col4:
        stream = st.selectbox("12th stream", ["Science_PCM", "Science_PCB", "Commerce", "Arts"])
    with col5:
        cgpa = st.number_input("CGPA", 0.0, 10.0, 7.5, step=0.1, format="%.1f")

    degree = st.selectbox("Degree", ['BA', 'BSc Data Science', 'CA', 'BCA', 'BDes', 'BSc', 'BBA',
                                      'BTech', 'BHMS', 'BEd', 'LLB', 'BFA', 
                                     'MBBS', 'BCom', 'BAMS', 'BA Economics', 
                                     'BSc Nursing', 'BSc Biotechnology',
                                       'BSc Microbiology', 'BDS', 'CMA'])

    # Store values in session state so later steps can read them
    st.session_state.update(
        age=age, tenth=tenth, twelfth=twelfth,
        stream=stream, cgpa=cgpa, degree=degree,
    )

    st.markdown("")
    st.button("Continue →", on_click=go_next, type="primary")

# ─────────────────────────────────────────────────────────────────────────────
# STEP 1 — Skills & interests
# ─────────────────────────────────────────────────────────────────────────────
elif st.session_state.step == 1:
    st.subheader("Step 2 · Skills & interests")

    st.markdown("**Skills**")
    col1, col2 = st.columns(2)
    with col1:
        programming    = st.slider("Programming",    1, 5, 3)
        leadership     = st.slider("Leadership",     1, 5, 3)
        problem_solving = st.slider("Problem solving", 1, 5, 3)
    with col2:
        communication  = st.slider("Communication", 1, 5, 3)
        creativity     = st.slider("Creativity",    1, 5, 3)
        fitness        = st.slider("Physical fitness", 1, 5, 3)

    st.markdown("**Interests**")
    col3, col4 = st.columns(2)
    with col3:
        technology = st.slider("Technology", 1, 5, 3)
        finance    = st.slider("Finance",    1, 5, 3)
        business   = st.slider("Business",   1, 5, 3)
        law        = st.slider("Law",        1, 5, 3)
    with col4:
        medical  = st.slider("Medical",     1, 5, 3)
        govt     = st.slider("Government",  1, 5, 3)
        teaching = st.slider("Teaching",    1, 5, 3)

    st.session_state.update(
        programming=programming, communication=communication,
        leadership=leadership, creativity=creativity,
        problem_solving=problem_solving, fitness=fitness,
        technology=technology, medical=medical, finance=finance,
        govt=govt, business=business, teaching=teaching, law=law,
    )

    st.markdown("")
    back, _, fwd = st.columns([1, 4, 1])
    back.button("← Back",     on_click=go_back)
    fwd.button("Continue →", on_click=go_next, type="primary")

# ─────────────────────────────────────────────────────────────────────────────
# STEP 2 — Personality & hobbies
# ─────────────────────────────────────────────────────────────────────────────
elif st.session_state.step == 2:
    st.subheader("Step 3 · Personality & hobbies")

    col1, col2 = st.columns(2)
    with col1:
        personality = st.selectbox(
            "Personality type",
            ['Analytical', 'Helping', 'Leadership', 'Creative', 'Research'],
        )
    with col2:
        hobby = st.selectbox(
            "Primary hobby",
            ['Writing', 'Sports', 'Reading', 'Public Speaking', 'Music', 'Coding', 'Social Work', 'Drawing'],
        )

    st.info(
        "Your personality and hobby help distinguish between careers with "
        "similar academic profiles — e.g. Creative + Drawing leans toward "
        "design, while Analytical + Coding leans toward engineering.",
        icon="ℹ️",
    )

    # Summary
    with st.expander("📋 Review your answers"):
        s = st.session_state
        st.markdown(f"""
| Field | Value |
|---|---|
| Age | {s.age} |
| 10th % | {s.tenth} |
| 12th % | {s.twelfth} |
| Stream | {s.stream} |
| Degree | {s.degree} |
| CGPA | {s.cgpa} |
| Personality | {personality} |
| Hobby | {hobby} |
""")

    st.session_state.update(personality=personality, hobby=hobby)

    st.markdown("")
    back, _, predict_btn = st.columns([1, 3, 2])
    back.button("← Back", on_click=go_back)

    if predict_btn.button("✨ Predict career", type="primary"):
        go_next()
        st.rerun()

# ─────────────────────────────────────────────────────────────────────────────
# STEP 3 — Result
# ─────────────────────────────────────────────────────────────────────────────
elif st.session_state.step == 3:
    s = st.session_state

    input_data = pd.DataFrame([{
        "Student_ID":        0,
        "Age":               s.age,
        "10th_Percentage":   s.tenth,
        "12th_Percentage":   s.twelfth,
        "12th_Stream":       s.stream,
        "Degree":            s.degree,
        "CGPA":              s.cgpa,
        "Programming":       s.programming,
        "Communication":     s.communication,
        "Leadership":        s.leadership,
        "Creativity":        s.creativity,
        "Problem_Solving":   s.problem_solving,
        "Technology_Interest":  s.technology,
        "Medical_Interest":     s.medical,
        "Finance_Interest":     s.finance,
        "Government_Interest":  s.govt,
        "Business_Interest":    s.business,
        "Teaching_Interest":    s.teaching,
        "Law_Interest":         s.law,
        "Physical_Fitness":     s.fitness,
        "Personality":          s.personality,
        "Hobby":                s.hobby,
    }])

    for col in ["12th_Stream", "Degree", "Personality", "Hobby"]:
        input_data[col] = encoders[col].transform(input_data[col])

    prediction = model.predict(input_data)
    career = encoders["Career"].inverse_transform(prediction)[0]

    # ── Result card ──────────────────────────────────────────────────────────
    st.markdown(
        f"""
        <div style="
            background: linear-gradient(135deg, #f0f4ff 0%, #e8f0fe 100%);
            border-radius: 16px;
            padding: 2rem;
            text-align: center;
            margin: 1rem 0;
        ">
            <div style="font-size: 3rem;">🏆</div>
            <p style="color: #666; font-size: 0.9rem; margin: 0.5rem 0 0.25rem;">Recommended career</p>
            <h2 style="color: #1a56db; font-size: 2rem; margin: 0;">{career}</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Tags
    tags = [s.degree, s.stream, s.personality, s.hobby]
    st.markdown(" ".join(f"`{t}`" for t in tags))

    st.markdown("")
    col_a, col_b = st.columns(2)
    col_a.button("🔄 Start over", on_click=restart)

    with st.expander("📊 View input data sent to model"):
        st.dataframe(input_data, use_container_width=True)
