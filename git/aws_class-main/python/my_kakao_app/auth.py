import streamlit as st
from database import engine, hash_password
from sqlalchemy import text

def show_account_page():
    """Account 메뉴 클릭 시 보여줄 로그인/회원가입 화면"""
    if st.session_state['logged_in']:
        st.markdown("<div class='status-card'>", unsafe_allow_html=True)
        st.success(f"현재 **{st.session_state['user_name']}**님으로 로그인 중입니다.")
        if st.button("로그아웃"):
            st.session_state['logged_in'] = False
            st.session_state['user_name'] = "GUEST"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        col1, col2, col3 = st.columns([1, 1.5, 1])
        with col2:
            st.markdown("<div class='status-card'>", unsafe_allow_html=True)
            tab1, tab2 = st.tabs(["로그인", "회원가입"])
            
            with tab1:
                with st.form("login_form"):
                    u = st.text_input("아이디")
                    p = st.text_input("비밀번호", type="password")
                    if st.form_submit_button("로그인"):
                        with engine.connect() as conn:
                            res = conn.execute(text("SELECT password, name FROM users WHERE username = :u"), {"u": u}).fetchone()
                        if res and res[0] == hash_password(p):
                            st.session_state['logged_in'] = True
                            st.session_state['username'] = u
                            st.session_state['user_name'] = res[1]
                            st.rerun()
                        else:
                            st.error("정보가 일치하지 않습니다.")
                            
            with tab2:
                with st.form("signup_form"):
                    nu = st.text_input("아이디 만들기")
                    nn = st.text_input("이름")
                    np = st.text_input("비밀번호 설정", type="password")
                    if st.form_submit_button("가입 완료"):
                        try:
                            with engine.connect() as conn:
                                conn.execute(text("INSERT INTO users VALUES (:u, :p, :n)"), {"u": nu, "p": hash_password(np), "n": nn})
                                conn.commit()
                            st.success("가입 성공! 로그인 탭에서 로그인 해주세요.")
                        except:
                            st.error("이미 사용 중인 아이디입니다.")
            st.markdown("</div>", unsafe_allow_html=True)