import React from "react";
import main_style from "../Layout.module.css";
import style from "./Footer.module.css";

const Footer = () => {
  return (
    <footer className={style.footer}>
      <div className={main_style.wrapper + " " + style.footer_divider}>
        <div className={style.footer_item + " " + style.footer_logo}>
          <h2>Woordjes leren</h2>
          <img src="/src/assets/react.svg" />
        </div>
        <div className={style.footer_item}>
          <h2>Contact</h2>
          <a href="">Contact us</a>
          <a href="">Iets</a>
          <a href="">Iets</a>
        </div>
        <div className={style.footer_item}>
          <h2>Links</h2>
          <a href="">Privacy</a>
          <a href="">Cookies</a>
          <a href="">Iets</a>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
