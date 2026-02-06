import { useState } from "react";


function Insert (){


  
  let [date, setDate] = useState("");
  let [text, setText] = useState("");
  
  const addTodo= (e)=>{
    e.preventDefault();

    const sendInsertTodo = async () =>{
      try{
        const response = await fetch("/api/v1/todos", {
          method : "POST",
          headers : {
            "Content-Type" : "application/json"
          },
          body : JSON.stringify({
            date : date,
            text : text
          })
        });

        if(response.status === 200){
          const result = await response.json();
          if(result){
            alert("할일을 등록했습니다.");
            setText("");
          }else{
            alert("할일을 등록하지 못했습니다.");
          }
        }

      }catch(e){
        console.error(e);
      }
    }
      sendInsertTodo();
  } 

    
  


  return (
    <div>
      <h1>할일 등록</h1>
      <form className="insert-form" onSubmit={addTodo}>
        <div>
        <label htmlFor="date">날짜</label>
        <input type="date" name="date" id="date" onChange={(e)=>{setDate(e.target.value)}}
        value={date}/>
        </div>
        <div>
        <label htmlFor="text">할일</label>
        <input type="text" name="text" id="text" onChange={(e)=>{setText(e.target.value)}}
        value={text}/>
        </div>
        <button>등록</button>
      </form>
    </div>
  );
}



export default Insert;