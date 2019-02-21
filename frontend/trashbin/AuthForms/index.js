import React from "react";
import FacebookLogo from 'react-ionicons/lib/LogoFacebook';
import styles from "./styles.module.scss";
import PropTypes from "prop-types";
import Footer from "../Footer";

export const LoginForm = (props,context) => (
    <div className={styles.formComponent}>
        <form className={styles.form}>
            <input className={styles.textInput} type="text" placeholder={context.t("Username")}/>
            <input className={styles.textInput} type="password" placeholder={context.t("Password")}/>
            <input className={styles.button} type="submit" value={context.t("Log in")}/>
        </form>

        <span className={styles.divider}>{context.t("or")}</span>
        <span className={styles.facebookLink}>
            <FacebookLogo fontSize="20px" color="#385185"/>
            {context.t("Log in with Facebook")}</span>
        <span className={styles.forgotLink}>{context.t("Forgot password?")}</span>
    </div>
);

export const SignupForm = (props,context) => (
    <div className={styles.formComponent}>
        <h3 className={styles.signupHeader}>
            {context.t("Sign up to see photos and videos from your friends")}.
        </h3>
        <button className={styles.button}>
            <FacebookLogo fontSize="20px" color="white"/>
            {context.t("Log in with Facebook")}
        </button>
        <span className={styles.divider}> {context.t("or")} </span>

        <form className={styles.form}>
            <input className={styles.textInput} type="email" placeholder={context.t("Email")}/>
            <input className={styles.textInput} type="text" placeholder={context.t("Full Name")}/>
            <input className={styles.textInput} type="username" placeholder={context.t("Username")}/>
            <input className={styles.textInput} type="password" placeholder={context.t("Password")}/>
            <input className={styles.button} type="submit" value={context.t("Sign Up")}/>
        </form>

        <p className={styles.terms}>
            By signing up , you agree to our <span>Terms & Privacy Policy</span>
        </p>
    </div>
);

LoginForm.contextTypes = {
    t: PropTypes.func.isRequired
};
SignupForm.contextTypes = {
    t: PropTypes.func.isRequired
};