import React from "react";
import classes from "./SubmitButton.module.css";

interface Props {
  children: string;
}

const SubmitButton = ({ children }: Props) => {
  return <div className={classes.button_submit}>{children}</div>;
};

export default SubmitButton;
