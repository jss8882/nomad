import React, { Component } from "react";
import PropTypes from "prop-types";
import LoginForm from "./presenter";

class Container extends Component {
  // 로그인을 수행하기 위해서 로그인 폼의 유저명과 비밀번호를 추적해야한다.
  state = {
    username: "",
    password: ""
  };

  static propTypes = {
    facebookLogin: PropTypes.func.isRequired,
    usernameLogin: PropTypes.func.isRequired
  }

  render() {
    const { username, password } = this.state;
    return (
      <LoginForm
        handleInputChange={this._handleInputChange}
        handleSubmit = {this._handleSubmit}
        handleFacebookLogin = {this._handleFacebookLogin}
        usernameValue={username}
        passwordValue={password}
      />
    );
  }

  _handleInputChange = event => {
    //패턴매칭을 통하여 저장
      const { target : {value,name}} = event;
    //   console.log(value);
    //   console.log(name);
    this.setState({
        // 패턴매칭을 통하여 state에 저장
        //name could be either username or password
        [name] : value
    });
    console.log(this.state);
  };

  _handleSubmit = event => {
    //   브라우저가 디폴트 작업을 하지 않게 하기위해서 preventDefault를 사용
      const {usernameLogin} = this.props;
      const {username , password} = this.state;
      event.preventDefault();
      usernameLogin(username,password);
  }

  _handleFacebookLogin = response => {
    const {facebookLogin} = this.props;
    console.log(response.accessToken)
    facebookLogin(response.accessToken);
  }

}

// const Container = props => <LoginForm {...props}/>;

export default Container;
