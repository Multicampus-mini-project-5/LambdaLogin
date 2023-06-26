import axios from "axios";
import { useEffect } from "react";

function Login () {

// api 추가
  useEffect(() => {
    axios.post('https://yeuc2uld81.execute-api.ap-northeast-3.amazonaws.com/production/login', {ID:"admin", PWD: "password"})
    .then(res => {
        console.log(res);
    })
    .catch(err => console.log(err));
}, []);
// -------------------------------------------------------------------------------------------
  return (
    <div className="page-container">
      <div className="login-form">
        <input type="text" placeholder="아이디를 입력하세요" />
        <div><input type="password" placeholder="비밀번호를 입력하세요" /> </div>      
      </div>
      <div>
        <button>회원가입</button>
        <button>Log In</button> 
      </div>
    </div>
   

  );
}

export default Login;