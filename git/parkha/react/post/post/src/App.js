import React from 'react';
import './App.css';
import Header from './Header'; // 분리한 헤더 임포트

const App = () => {
  const dietData = [
    { id: 1, sub: "든든한 단백질 케어", title: "단백질식단", img: "https://via.placeholder.com" },
    { id: 2, sub: "꾸준한 식단 관리를 위한", title: "칼로리식단", img: "https://via.placeholder.com" },
    { id: 3, sub: "내 몸을 위한 가장 편안한 속도", title: "저속식단", img: "https://via.placeholder.com" },
    { id: 4, sub: "당은 줄이고, 식사는 즐겁게", title: "저당식단", img: "https://via.placeholder.com" }
  ];

  return (
    <div className="container">
      {/* 분리된 헤더 컴포넌트 */}
      <Header />

      {/* 메인 콘텐츠 영역 */}
      <main style={{maxWidth: '1100px', margin: '0 auto', padding: '20px 0'}}>
        {/* 배너 섹션 */}
        <section className="main-banner">
          <div className="banner-text">
            <p>건강한 일상을 지키는 가장 쉬운 관리</p>
            <h1 style={{fontSize: '32px', margin: '10px 0'}}>건강식단 ❯</h1>
            <p style={{color: '#e74c3c', fontWeight: 'bold'}}>건강식단과 함께 구매 시 연속혈당측정기 10% 할인</p>
          </div>
          <img src="https://via.placeholder.com" alt="banner" className="banner-img" />
        </section>

        {/* 카드 그리드 섹션 */}
        <div className="card-grid">
          {dietData.map((item) => (
            <div key={item.id} className="diet-card">
              <div className="card-info">
                <h4 style={{color: '#888', fontWeight: 'normal'}}>{item.sub}</h4>
                <h2 style={{margin: '5px 0'}}>{item.title} ❯</h2>
              </div>
              <img src={item.img} alt={item.title} className="card-icon" />
            </div>
          ))}
        </div>

        {/* 마이그리팅 하단 바 */}
        <div className="my-greeting-bar">
          <p style={{margin: 0}}>직접 설계하는 나만의 식단</p>
          <h2 style={{margin: '5px 0'}}>집좀가자 ❯</h2>
        </div>
      </main>
    </div>
  );
};

export default App;