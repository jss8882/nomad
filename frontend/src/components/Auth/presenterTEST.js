import React from "react";
import styles from "./styles.module.scss";

const Auth = (props, context) => (
    //TODO 
    <main className={styles.auth}>
      <div className={styles.column}>
        <img
          src={require("images/phone.png")}
          alt="stagram"
        />
      </div>
      <div className={styles.column}>
        <div className={styles.whiteBox}></div>

        <div className={styles.appBox}>
          <span> get app store app</span>
          <div className={styles.appStore}>
            <img 
              src={require("images/ios.png")}
              alt="get gram on isoappStore"
            />
            <img 
              src={require("images/android.png")}
              alt="get gram on android store"
            />
          </div>

        </div>
      </div>
    </main>
      

  );

  export default Auth;