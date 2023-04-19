import React, { MouseEventHandler } from "react";
import classes from "./SubmitButton.module.css";

interface Props {
  children: string;
  clickHandler: MouseEventHandler;
}

const SubmitButton = ({ children, clickHandler }: Props) => {
  return (
    <div className={classes.button_submit} onClick={clickHandler}>
      {children}
    </div>
  );
};

export default SubmitButton;
