import React, { Component } from "react";
import PropTypes from "prop-types";
import SignupForm from "./presenter";

//const Container = props => <SignupForm {...props}/>;

class Container extends Component {
  state = {
    email: "",
    fullname: "",
    username: "",
    password: ""
  };
  static propTypes = {
    createAccount: PropTypes.func.isRequired

  }

  render() {
    const { email, name, username, password } = this.state;

    return (
      <SignupForm
        handleInputChange={this._handleInputChange}
        handleSubmit={this._handleSubmit}
        handleFacebookLogin={this._handleFacebookLogin}
        emailValue={email}
        nameValue={name}
        usernameValue={username}
        passwordValue={password}
      />
    );
  }
  _handleInputChange = event => {
    const {
      target: { value, name }
    } = event;
    this.setState({
        [name]:value
    });

    console.log(this.state);
  };

  _handleSubmit = event => {
      const {username,password,email,name} = this.state;
      const {createAccount} = this.props;
      event.preventDefault();
      console.log(this.state);
      createAccount(username,password,email,name);
  }

  _handleFacebookLogin = response =>{
    console.log(response)
  }
}


export default Container;
