import React, { useState } from 'react';

/*
좋아하는 과일을 선택하면 h2태그 옆에 선택한 과일이 출력되도록 작성.
- 주의사항
  - 과일을 선택하세요. 를 선택하면 선택된 과일이 없습니다가 출력되도록 작성
*/

function App6(){

    let [fruit, setFruit] = useState("");

    const fruitChange = (e)=>{
        setFruit (e.target.value);
    }
    


    return(
        <div>
            <h1>좋아하는 과일은?</h1>
            <select onChange={fruitChange}>
                <option value="">과일을 선택하세요.</option>
                <option value="사과">사과</option>
                <option value="바나나">바나나</option>
                <option value="포도">포도</option>
            </select>
            <h2>좋아하는 과일 : {fruit === ""? "선택된 과일이 없습니다." : fruit}</h2>

        </div>
    );
}

export default App6;