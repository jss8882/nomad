import React from "react";
// import FacebookLogo from "react-ionicons/lib/LogoFacebook";
import PropTypes from "prop-types";
import formStyles from "shared/formStyles.module.scss";
import FacebookLogin from "react-facebook-login";

export const SignupForm = (props, context) => (
  <div className={formStyles.formComponent}>
    <h3 className={formStyles.signupHeader}>
      {context.t("Sign up to see photos and videos from your friends")}.
    </h3>
    <FacebookLogin
      appId="2341676329398705"
      autoLoad={false}
      fields="email,name,picture"
      callback={props.handleFacebookLogin}
      cssClass={formStyles.button}
      icon="fa-facebook-official"
      textButton={context.t("Log in with Facebook")}
    />
    <span className={formStyles.divider}> {context.t("or")} </span>

    <form className={formStyles.form} onSubmit={props.handleSubmit}>
      <input
        className={formStyles.textInput}
        type="email"
        placeholder={context.t("Email")}
        onChange={props.handleInputChange}
        value={props.emailValue}
        name="email"
      />
      <input
        className={formStyles.textInput}
        type="text"
        placeholder={context.t("Full Name")}
        onChange={props.handleInputChange}
        value={props.fullnameValue}
        name="fullname"

      />
      <input
        className={formStyles.textInput}
        type="username"
        placeholder={context.t("Username")}
        onChange={props.handleInputChange}
        value={props.usernameValue}
        name="username"
      />
      <input
        className={formStyles.textInput}
        type="password"
        placeholder={context.t("Password")}
        onChange={props.handleInputChange}
        value={props.passwordValue}
        name="password"
      />
      <input
        className={formStyles.button}
        type="submit"
        value={context.t("Sign Up")}
      />
    </form>

    <p className={formStyles.terms}>
      By signing up , you agree to our <span>Terms & Privacy Policy</span>
    </p>
  </div>
);

SignupForm.contextTypes = {
  t: PropTypes.func.isRequired
};

SignupForm.propType = {
  handleInputChange: PropTypes.func.isRequired,
  handleSubmit: PropTypes.func.isRequired,
  handleFacebookLogin: PropTypes.func.isRequired,
  emailValue: PropTypes.string.isRequired,
  fullnameValue: PropTypes.string.isRequired,
  usernameValue: PropTypes.string.isRequired,
  passwordValue: PropTypes.string.isRequired
  
};

export default SignupForm;
