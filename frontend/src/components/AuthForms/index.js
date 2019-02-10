import React from "react";
import FacebookLogo from 'react-ionicons/lib/LogoFacebook';
import styles from "./styles.module.scss";

export const LoginForm = props => (
    <div>
        <form>
            <input type="text" placeholder="User name"/>
            <input type="password" placeholder="Password"/>
            <input type="submit" value="Log in"/>
        </form>

        <span>or</span>
        <span>
            <FacebookLogo fontSize="20px" color="#385185"/>
            Log in with Facecbook</span>
        <span>Forgot password?</span>
    </div>
);

export const SignupForm = props => (
    <div className={styles.formComponent}>
        <h3 className={styles.signupHeader}>
            Sign up to see photos and videos from your friends.
        </h3>
        <button className={styles.button}>
            <FacebookLogo fontSize="20px" color="white"/>
            Log in with Facebook
        </button>
        <span className={styles.divider}> or </span>

        <form className={styles.form}>
            <input className={styles.textInput} type="email" placeholder="Email"/>
            <input className={styles.textInput} type="text" placeholder="Full Name"/>
            <input className={styles.textInput} type="username" placeholder="Username"/>
            <input className={styles.textInput} type="password" placeholder="Password"/>
            <input className={styles.button} type="submit" value="Sign up"/>
        </form>

        <p className={styles.terms}>
            By signing up , you agree to our <span>Terms & Privacy Policy</span>
        </p>
    </div>
);