import React from "react";
import classes from "./HintButton.module.css";

interface Props {
  onClick: () => void;
}

const HintButton = ({ onClick }: Props) => {
  return (
    <div className={classes.button_hint} onClick={onClick}>
      ?
    </div>
  );
};

export default HintButton;
