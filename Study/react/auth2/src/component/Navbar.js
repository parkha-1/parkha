import {Link} from "react-router-dom";

export function Navbar(){

	const NAV_ITEMS = [
		{label : "메인", path : "/"},
		{label : "로그인", path : "/login"},
		{label : "회원가입", path : "/signup"},
		{label : "마이 페이지", path : "/mypage"},
	]

	return (
		<nav>
			<ul>
				{
					NAV_ITEMS
					//나중에 로그인 여부에 따라 보여줄 메뉴를 다르게 하기 위한 filter를 미리 추가
					.filter(item =>{
						return true;
					})
					.map(item => <li><Link to={item.path}>{item.label}</Link></li>)
				}
			</ul>
		</nav>
	)
}