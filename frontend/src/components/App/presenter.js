import React from "react";
//props체크를 위한 모듈
import PropTypes from "prop-types";
import { Route,Switch } from "react-router-dom";
import "./styles.module.scss";
import Footer from "components/Footer";
import Auth from "components/Auth";

//isLoggedIn이 이 컴포넌트 안에 있음 index.js에서 connect를 해주었기 때문임
const App = props => [
  //nav
  //route
  props.isLoggedIn ? <PrivateRoute key={2} /> : <PublicRoute key={2} />,
  //리액트 배열은 리턴을 할때 키가 필요함
  <Footer key={3} />
];

App.propTypes = {
  isLoggedIn : PropTypes.bool.isRequired
};

const PrivateRoute = props =>(
  <Switch>
    <Route exact path='/' render={()=>"feed"} />
    <Route path='/explore' render={()=>"explore"} />
  </Switch>
);

const PublicRoute = props =>(
  <Switch>
    <Route exact path='/' component={Auth} />
    <Route path='/forget' render={() => "reset password"} />
  </Switch>
);


export default App;
