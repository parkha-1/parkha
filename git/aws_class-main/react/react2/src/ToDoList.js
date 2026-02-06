import { useState } from "react";

function ToDoList(){

  //할일을 저장할 state 변수를 선언. 문자열. todo
  let [todo, setTodo] = useState("");
  //할일 목록을 저장할 state 변수를 선언. 객체 배열. todos
  //id : 번호 , todo : 할일
  let [todos, setTodos] = useState([
  { id: 1, todo: "" },
  { id: 2, todo: "" }
  ]);
  //번호를 저장할 변수를 선언
  let [num, setNum] = useState(3);
  //할일을 입력하면 state 변수에 저장하는 함수 선언 및 이벤트 등록
  const todoChange = e => setTodo(e.target.value);
  //등록을 클릭하면 입력된 할일을 할일 목록에 추가하는 함수를 선언 및 이벤트 등록
  const addTodo = e => {e.preventDefault(); //form태그의 submit 이벤트가 발생되어 서버에 전송되지 않게 하기 위해
  //추가할 객체
  let todoObj = {
    id : num++,
    todo : todo
  }
    setTodos([...todos, todoObj]);
    setNum(num+1);
    setTodo("");
  }
  return(
    <div>
      <form onSubmit={addTodo}>
        <input type="text" placeholder="할일을 입력하세요." onChange={todoChange} value={todo}/>
        <button>등록</button>
      </form>
      <hi>할 일 목록</hi>
      <ul>
        {
          todos.map(item=>{
            return(
              <li key={"todo"+item.id}>{item.todo}</li>
            )
          })
        }
      </ul>
    </div>
  )
}

export default ToDoList;