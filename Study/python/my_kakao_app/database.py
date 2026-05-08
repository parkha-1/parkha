import hashlib
from sqlalchemy import create_engine, text

# DB 연결 설정
engine = create_engine('sqlite:///career_ai.db')

def init_db():
    """데이터베이스 테이블 초기화"""
    with engine.connect() as conn:
        # 사용자 테이블
        conn.execute(text("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT, name TEXT)"))
        # 면접 기록 테이블
        conn.execute(text("CREATE TABLE IF NOT EXISTS interview_logs (id INTEGER PRIMARY KEY, username TEXT, job_title TEXT, score INTEGER, feedback TEXT, date TEXT)"))
        conn.commit()

def hash_password(password):
    """비밀번호 암호화 (SHA-256)"""
    return hashlib.sha256(str.encode(password)).hexdigest()