import React from 'react';
import './Header.css';

const Header = () => {
  return (
    <header className="header-container">
      {/* 1. 최상단 유틸리티 메뉴 (요구사항 반영) */}
      <div className="top-util-bar">
        <ul className="util-menu">
          <li>로그인</li>
          <li>회원가입</li>
          <li>쿠폰등록</li>
          <li>스크랩</li>
          <li>고객센터 ▾</li>
        </ul>
      </div>

      {/* 2. 중간 로고 및 검색 섹션 */}
      <div className="main-header-row">
        <div className="logo">집좀 가자</div>
        <div className="search-bar">
          <input type="text" placeholder="내 몸에 딱 맞는 그리팅 식단" />
          <button className="search-btn">🔍</button>
        </div>
        <div className="header-icons">
          <span className="icon">🚚</span>
          <span className="icon">🛒 <span className="cart-count">0</span></span>
        </div>
      </div>

      {/* 3. 메인 네비게이션 메뉴 */}
      <nav className="nav-bar">
        <div className="category-btn">☰ 카테고리</div>
        <ul className="nav-list">
          <li className="active">식단관리</li>
          <li>건강마켓</li>
          <li>식단추천</li>
          <li>건강식단</li>
          <li>질환맞춤</li>
          <li>챌린지식단</li>
          <li>식단연구소</li>
          <li>웰니스레터</li>
          <li className="highlight">무료영양진단</li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;