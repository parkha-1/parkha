import ChatBot from "./ChatBot";
import Main from "./Main";
import { BrowserRouter, Route, Routes } from "react-router-dom";

function App() {
  async function test(msg){

    const response = await fetch(`/api/v1/test?msg=${msg}`)
    
    if(!response.ok){
      console.log('연결 실패')
      return;
    }

    const res = await response.json()
    console.log(res.msg)

  }
  test('hi')

  async function testPost(msg){

    const response = await fetch(`/api/v1/test`,{
      method : 'post',
      headers :{
        'Content-type' : 'application/json'
      },
      body : JSON.stringify({'msg' : msg})
    })
    
    if(!response.ok){
      console.log('연결 실패')
      return;
    }

    const res = await response.text()
    console.log(res)

  }
  testPost('hi')
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" exact element={<Main/>} />
        <Route path="/chat" element={<ChatBot/>} />
      </Routes>
    </BrowserRouter>
  )
}

export default App;
