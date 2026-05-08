import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import text
from database import engine
from datetime import datetime
from openai import OpenAI

# OpenAI 클라이언트 (API 키는 보안을 위해 환경변수나 main에서 관리하는 것이 좋습니다)
# 여기서는 직접 입력하거나 main.py에서 정의된 값을 사용하세요.
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

# --- 공통 스타일 (가독성 향상용) ---
def card_style(content, title=None):
    if title:
        st.markdown(f"#### {title}")
    st.markdown(f"<div class='status-card'>{content}</div>", unsafe_allow_html=True)

# --- [Page 1] Dashboard ---
def show_dashboard():
    st.markdown("### 🏠 실시간 채용 현황")
    
    # 상단 요약 지표 (Metrics)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric(label="📊 전체 지원자", value="1,284명", delta="신규 12명")
    with c2:
        st.metric(label="✅ 평균 합격 점수", value="88점", delta="▲ 1.5")
    with c3:
        st.metric(label="🔥 핫한 직군", value="AI/LLM", delta="인기")

    st.write("---")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("#### 📈 직군별 채용 수요")
        df = pd.DataFrame({'Job': ['AI Dev', 'Data Engine', 'Backend', 'Product Design'], 'Count': [95, 72, 88, 56]})
        fig = px.bar(df, x='Job', y='Count', color='Job', 
                     color_discrete_sequence=['#FEE500', '#3C3E44', '#FFCD00', '#191919'])
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("#### 📢 Kakao News")
        st.info("카카오 AI 캠퍼스 신규 수강생 모집 중 (D-3)")
        st.success("2026 상반기 신입 개발자 블라인드 채용 공고 오픈")
        st.warning("데이터 사이언티스트 경력직 상시 채용")

# --- [Page 2] AI 직업 추천 ---
def show_recommendation():
    st.markdown("### 🔍 AI 맞춤 직업 진단")
    st.markdown("<p style='color: gray;'>당신의 기술 스택을 분석하여 가장 잘 어울리는 카카오 내 직무를 추천합니다.</p>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown("<div class='status-card'>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            skill_input = st.text_area("보유 스킬 및 경험", placeholder="예: Python, SQL 사용 가능. 데이터 시각화 프로젝트 경험 1회...", height=100)
        with c2:
            career_goal = st.selectbox("커리어 목표", ["빠른 기술 성장", "높은 비즈니스 영향력", "안정적인 서비스 운영", "혁신적인 UI/UX"])
            
        if st.button("AI 정밀 진단 시작 ✨"):
            if skill_input:
                with st.spinner("AI가 당신의 커리어를 매칭 중입니다..."):
                    prompt = f"사용자 스킬: {skill_input}, 목표: {career_goal}. 카카오의 직무 중 하나를 추천하고 이유를 3줄로 적어줘."
                    response = client.chat.completions.create(model="gpt-4o", messages=[{"role": "user", "content": prompt}])
                    st.markdown("---")
                    st.markdown(f"#### 💡 추천 결과: {response.choices[0].message.content}")
                    st.balloons()
            else:
                st.error("분석을 위해 스킬을 입력해주세요.")
        st.markdown("</div>", unsafe_allow_html=True)

# --- [Page 3] AI 모의면접 ---
def show_interview():
    st.markdown("### 💬 AI 실시간 모의면접 관")
    
    # 면접 설정 세션
    col1, col2 = st.columns([1, 2])
    with col1:
        job = st.selectbox("지원 직무", ["AI 엔지니어", "데이터 분석가", "서비스 기획자"])
        difficulty = st.select_slider("난이도", options=["주니어", "미드레벨", "시니어"])
    
    st.markdown("<div class='status-card'>", unsafe_allow_html=True)
    
    # 채팅 메시지 초기화
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "system", "content": f"당신은 카카오의 {job} 직무 면접관입니다. {difficulty} 수준의 질문을 던지세요. 한 번에 하나씩만 질문하세요."},
            {"role": "assistant", "content": f"반갑습니다. {st.session_state['user_name']}님. {job} 직무 면접을 시작해도 될까요? 먼저 첫 번째 질문을 드리겠습니다. 본인이 수행했던 가장 자랑스러운 프로젝트에 대해 설명해주세요."}
        ]
    
    # 채팅 기록 표시
    for msg in st.session_state.messages[1:]:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # 사용자 입력
    if prompt := st.chat_input("면접관에게 답변하기..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.write(prompt)
        
        with st.chat_message("assistant"):
            with st.spinner("생각 중..."):
                response = client.chat.completions.create(model="gpt-4o", messages=st.session_state.messages)
                full_response = response.choices[0].message.content
                st.write(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # 종료 및 저장
    if st.button("면접 종료 및 AI 피드백 저장 💾"):
        if st.session_state['logged_in']:
            with st.spinner("AI가 면접 전체를 평가 중입니다..."):
                eval_prompt = "지금까지의 대화를 분석해서 점수(0~100)와 짧은 피드백 한 줄을 '점수|피드백' 형식으로만 출력해줘."
                eval_res = client.chat.completions.create(model="gpt-4o", messages=st.session_state.messages + [{"role": "user", "content": eval_prompt}])
                
                try:
                    score_val, feedback_val = eval_res.choices[0].message.content.split('|')
                    score_val = int(''.join(filter(str.isdigit, score_val)))
                except:
                    score_val, feedback_val = 80, "전반적으로 논리적인 답변이 인상적이었습니다."

                with engine.connect() as conn:
                    conn.execute(text("INSERT INTO interview_logs (username, job_title, score, feedback, date) VALUES (:u, :j, :s, :f, :d)"),
                                 {"u": st.session_state['username'], "j": job, "s": score_val, "f": feedback_val, "d": datetime.now().strftime('%Y-%m-%d')})
                    conn.commit()
                st.success(f"저장 완료! 점수: {score_val}점")
                st.toast("기록이 '나의 기록' 탭에 저장되었습니다!", icon="✅")
                # 메시지 리셋
                del st.session_state.messages
        else:
            st.warning("로그인한 사용자만 결과를 저장할 수 있습니다.")

# --- [Page 4] 나의 기록 ---
def show_records():
    st.markdown("### 📑 나의 AI 성장 리포트")
    
    if not st.session_state['logged_in']:
        st.markdown("""
            <div style='text-align: center; padding: 50px;'>
                <h2 style='color: #DDDDDD;'>🔒 로그인 후 확인 가능합니다</h2>
                <p>Account 메뉴에서 로그인하고 당신의 성장 궤적을 확인하세요.</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        with engine.connect() as conn:
            df = pd.read_sql(text("SELECT job_title, score, feedback, date FROM interview_logs WHERE username = :u ORDER BY date DESC"), 
                             conn, params={"u": st.session_state['username']})
        
        if not df.empty:
            st.markdown("<div class='status-card'>", unsafe_allow_html=True)
            
            # 요약 데이터
            avg_score = df['score'].mean()
            st.write(f"#### 🏆 평균 면접 점수: {avg_score:.1f}점")
            
            # 시각화
            fig = px.line(df, x='date', y='score', markers=True, title="나의 면접 점수 추이",
                          color_discrete_sequence=['#FEE500'])
            fig.update_layout(xaxis_title="날짜", yaxis_title="점수")
            st.plotly_chart(fig, use_container_width=True)
            
            st.write("---")
            st.write("#### 📜 상세 기록 히스토리")
            st.dataframe(df, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.info("아직 저장된 면접 기록이 없습니다. AI 모의면접을 시작해보세요!")