import React from "react";
// stateless component에 context를 부르기 위하여
import PropTypes from "prop-types";
import styles from "./styles.module.scss"


// stateless component
// 번역을 위해서 컴포넌트에 context를 주어야함
//context를 넘기기 위해 두번째 인자에 context가 있음 porps외에도 컨텍스트를 줘야함
const Footer = (props,context) => (
    <footer className={styles.footer}>
        <div className={styles.column}>
            <nav className={styles.nav}>
                <ul className={styles.list}>
                    <li className={styles.listItem}>{context.t("About Us")}</li>
                    <li className={styles.listItem}>{context.t("Support")}</li>
                    <li className={styles.listItem}>{context.t("Blog")}</li>
                    <li className={styles.listItem}>{context.t("Press")}</li>
                    <li className={styles.listItem}>API</li>
                    <li className={styles.listItem}>{context.t("Jobs")}</li>
                    <li className={styles.listItem}>{context.t("Privacy")}</li>
                    <li className={styles.listItem}>{context.t("Terms")}</li>
                    <li className={styles.listItem}>{context.t("Directory")}</li>
                    <li className={styles.listItem}>{context.t("Language")}</li>
                </ul>
            </nav>
        </div>
        <div className={styles.column}>
            <span className={styles.copyright}>2019 copyright</span>
        </div>
    </footer>

)

Footer.contextTypes = {
    t: PropTypes.func.isRequired
};

export default Footer;