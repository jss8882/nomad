import React from "react";
// import FacebookLogo from "react-ionicons/lib/LogoFacebook";
import PropTypes from "prop-types";
import formStyles from "shared/formStyles.module.scss";
import FacebookLogin from "react-facebook-login";

export const LoginForm = (props, context) => (
  <div className={formStyles.formComponent}>
    <form className={formStyles.form} onSubmit={props.handleSubmit}>
      <input
        className={formStyles.textInput}
        type="text"
        placeholder={context.t("Username")}
        value={props.usernameValue}
        // value까지만 적으면 폼에 입력할때 사용되는 함수가 명시되지 않았으므로 적히지 않음
        // 즉 뭔가를 입력할때를 위한 함수가 필요함.
        onChange={props.handleInputChange}
        name="username"
      />
      <input
        className={formStyles.textInput}
        type="password"
        placeholder={context.t("Password")}
        value={props.passwordValue}
        onChange={props.handleInputChange}
        name="password"
      />
      <input
        className={formStyles.button}
        type="submit"
        value={context.t("Log in")}
      />
    </form>

    <span className={formStyles.divider}>{context.t("or")}</span>
    <span className={formStyles.facebookLink}>
    {/* facebook login  */}
      <FacebookLogin
        appId="2341676329398705"
        autoLoad={false}
        fields="name,email,picture"
        callback={props.handleFacebookLogin}
        cssClass={formStyles.facebookLink}
        icon="fa-facebook-official"
        textButton={context.t("Log in with Facebook")}
      />
    </span>
    <span className={formStyles.forgotLink}>
      {context.t("Forgot password?")}
    </span>
  </div>
);

LoginForm.propTypes = {
  usernameValue: PropTypes.string.isRequired,
  passwordValue: PropTypes.string.isRequired,
  handleInputChange: PropTypes.func.isRequired,
  handleSubmit: PropTypes.func.isRequired,
  handleFacebookLogin: PropTypes.func.isRequired
};

LoginForm.contextTypes = {
  t: PropTypes.func.isRequired
};

export default LoginForm;
