import streamlit as st
import random
from datetime import datetime

st.set_page_config(
    page_title="Wedding at Cana",
    page_icon="🎉",
    layout="centered",
)

def generate_unique_number():
    return random.randint(0, 1999)

# Initialize session state
if 'name' not in st.session_state:
    st.session_state['name'] = ''
if 'rsvp_response' not in st.session_state:
    st.session_state['rsvp_response'] = None
if 'invitation_generated' not in st.session_state:
    st.session_state['invitation_generated'] = False

# logos
st.markdown("""
    <style>
        .logo-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px;
        }
        .logo {
            height: 80px;
        }
    </style>
    <div class="logo-container">
        <img src="https://i.imgur.com/LtGE5sq.png" class="logo" alt="Church Logo">
        <img src="https://i.imgur.com/p252pRe.png" class="logo" alt="Youth Service Logo">
    </div>
    """, unsafe_allow_html=True)


# Confetti animation for "Yes" response
st.markdown("""
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <script>
        function fireConfetti() {
            confetti({
                particleCount: 100,
                spread: 70,
                origin: { y: 0.6 }
            });
        }
    </script>
    """, unsafe_allow_html=True)

# Page styling
st.markdown("""
    <style>
        body {
            color: #333333;
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            direction: rtl;
        }
        .main {
            text-align: center;
        }
        .header {
            font-size: 1.7em;
            color: #0078D4;
            text-align: center;
        }
        .subheader {
            font-size: 1.2em;
            color: #5a5a5a;
        }
        .content {
            font-size: 1.2em;
            margin-top: 20px;
        }
        button[data-baseweb="button"] {
            background-color: #0078D4;
            color: white;
            font-size: 1.2em;
            border-radius: 10px;
        }
        .fun-button {
            background-color: #4CAF50;
            color: white;
            font-size: 1.5em;
            padding: 15px 30px;
            border-radius: 25px;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .fun-button:hover {
            background-color: #45a049;
        }
        .sad-button {
            background-color: #f44336;
            color: white;
            font-size: 1.5em;
            padding: 15px 30px;
            border-radius: 25px;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .sad-button:hover {
            background-color: #d32f2f;
        }
        /* For smaller screens like mobile */
        @media (max-width: 768px) {
            .main {
                text-align: center;
            }
            .stApp {
                background-image: url("data:image/jpg;base64,{mobile_bg}");
                background-size: cover;
                background-position: center;
            }
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main"><div class="header">أهلاً بك في عرس قانا الجليل</div></div>', unsafe_allow_html=True)
st.markdown('<div class="main"><div class="subheader">أدخل اسمك للحصول على دعوتك الخاصة</div></div>', unsafe_allow_html=True)

# Input
name = st.text_input("ادخل اسمك هنا:", value=st.session_state['name'])

if st.button("احصل على دعوتك"):
    if name.strip():
        st.session_state['name'] = name
        st.session_state['invitation_generated'] = True
        st.session_state['random_number'] = generate_unique_number()
        st.success(f"🎉 تم تسجيل اسمك بنجاح!")
        st.balloons()


if st.session_state['invitation_generated']:
    # The invitation
    st.markdown(f"""
        <div class="main content">
            <div style="background-color: #f0f8ff; padding: 10px; border-radius: 10px;">
                <h3 style="color: #0078D4;font-weight: bold;">عرس قانا الجليل</h3>
                    <p style="color: #5a5a5a;font-weight: bold;">دعوة خاصة: {st.session_state['name']}</p>
                    <p style="color: #5a5a5a;font-weight: bold;">رقم الدعوة: {st.session_state['random_number']}</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Countdown timer
    wedding_date = datetime(2025, 1, 24, 18, 0)
    time_remaining = wedding_date - datetime.now()
    st.markdown(f"""
        <div class="main content">
            <div style="background-color: #f0f8ff; padding: 10px; border-radius: 10px;">
                <h3 style="color: #0078D4;font-weight: bold;">المتبقي على معاد الفرح!</h3>
                <p style="color: #5a5a5a;font-weight: bold;">
                    {time_remaining.days}من الأيام  , {time_remaining.seconds // 3600} ساعة, و {(time_remaining.seconds % 3600) // 60} دقيقة متبقيين!
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # RSVP confirmation
    st.markdown("""
        <style>
            .header2 {
                text-align: right;
                font-size: 1.7em;
                color: #0078D4;
                font-weight: bold;
            }
        </style>
        <div class="main">
            <div class="header2">جاي الفرح؟</div>
        </div>
        """, unsafe_allow_html=True)


    rsvp_response = st.radio("أكيد هتحضر؟", ["اه أكيد", "لا"], index=0 if st.session_state['rsvp_response'] == "اه أكيد" else 1)

    if st.button("Submit"):
        st.session_state['rsvp_response'] = rsvp_response
        if rsvp_response == "اه أكيد":
            st.success(f"🎉 مستنيين نشوفك يا {st.session_state['name']}!")
            st.balloons()
            st.markdown("""
                <script>
                    fireConfetti();
                </script>
                """, unsafe_allow_html=True)
        else:
            st.warning(f"😢هتوحشنا. عيلتنا هتبقى ناقصة من غيرك يا {st.session_state['name']}!")

# Image for the page
st.image("https://i.imgur.com/3LO6o7I.jpg", caption="عرس قانا الجليل")

# Audio player
audio_url = "https://github.com/Selvia-nasser/CanaWeddingInvitation/raw/b0ff39331cc39c1bd29e69d47b0ea0d4f4207176/CanaWed.mp3"
st.audio(audio_url, format="audio/mp3", start_time=0, autoplay=True)
