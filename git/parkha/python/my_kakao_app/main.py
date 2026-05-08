import streamlit as st
from streamlit_option_menu import option_menu
import database
import auth
import pages_content

# 1. 페이지 설정
st.set_page_config(page_title="Kakao Career AI", layout="wide", page_icon="💛")

# 2. DB 초기화
database.init_db()

# 3. CSS 적용
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Noto Sans KR', sans-serif; background-color: #F9F9F9; }
    [data-testid="stSidebar"] { background-color: #3C3E44 !important; }
    .status-card { background-color: white; padding: 25px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border: 1px solid #EEEEEE; margin-bottom: 20px; }
    .stButton>button { width: 100%; background-color: #FEE500; color: #191919; border: none; padding: 12px; font-weight: 700; border-radius: 8px; }
    .stButton>button:hover { background-color: #F7E600; transform: translateY(-2px); }
    </style>
    """, unsafe_allow_html=True)

# 4. 세션 상태 초기화
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'user_name' not in st.session_state:
    st.session_state['user_name'] = "GUEST"

# 5. 사이드바 네비게이션
with st.sidebar:
    st.markdown(f"<h3 style='color:#FEE500; text-align:center;'>{st.session_state['user_name']}님</h3>", unsafe_allow_html=True)
    st.write("---")
    selected = option_menu(
        "Kakao AI Menu", ["Dashboard", "AI 직업 추천", "AI 모의면접", "나의 기록", "Account"],
        icons=['house-door', 'search-heart', 'chat-dots', 'journal-text', 'person-circle'],
        menu_icon="cast", default_index=0,
        styles={
            "container": {"background-color": "#3C3E44"},
            "nav-link": {"color": "white", "margin":"5px"},
            "nav-link-selected": {"background-color": "#FEE500", "color": "#191919", "font-weight": "700"},
        }
    )

# 6. 메뉴별 페이지 로딩 (나눈 파일의 함수 호출)
if selected == "Dashboard":
    pages_content.show_dashboard()
elif selected == "AI 직업 추천":
    pages_content.show_recommendation()
elif selected == "AI 모의면접":
    pages_content.show_interview()
elif selected == "나의 기록":
    pages_content.show_records()
elif selected == "Account":
    auth.show_account_page()