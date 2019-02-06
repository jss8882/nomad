import React from "react";
//컴포넌트들을 이어주기 위하여 링크(Link)를 사용할 것임
// <a =href를 사용하면 생성해 두었던 state가 초기화 되기 때문
import { Route, Link } from "react-router-dom";

const App = () => (
  <div>
    <Header />
  </div>
);

const Header = () => (
  <header>
    <h1>My Contacts</h1>

    <nav>
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/contacts">Contact</Link>
        </li>
      </ul>
    </nav>

    {/* 라우터를 설정 localhost:3000/접속하면 Welcome이라는 변수사용 */}
    {/* 라우터는 패턴기반으로 라우트를 축적하기 때문에 path가 '/'여도 다른곳에서도 모두 보여짐 (패턴매칭이 되기 때문) */}
    {/* <Route path="/" component={Welcome} /> */}

    {/* exact path를 사용하여 해결 */}
    <Route exact path="/" component={Welcome} />
    <Route path="/contacts" component={Contacts} />
  </header>
);

const Welcome = () => <h1>Welcome to the contacts App</h1>;

const Contacts = ({ match }) => (
  <div>
    <ul>
      <li><Link to="/contacts/sangsu">sangsu</Link></li>
      <li><Link to="/contacts/minsu">minsu</Link></li>
      <li><Link to="/contacts/benny">benny</Link></li>
    </ul>
    <Route
      exact
      path={`${match.path}`}
      render={() => <h3>Please select a contact</h3>}
    />
    <Route
      // contacts/sangsu로 접속하게 자동으로 sangsu는 params로 들어가게 됨
      // 여기에서 지정해두었던 contactName에 매칭되어
      path={`${match.path}/:contactName`}
      component={Contact}
    />
  </div>
);

const Contact = ({match}) => `Your friends name is ${match.params.contactName}`;
// import styles from 'App.module.scss';

// class App extends Component {
//   render() {
//     return (
//       <div className={styles.APP} />
//     );
//   }
// }

export default App;
