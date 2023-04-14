import React from "react";
import style from "./Feedback.module.css";

interface Props {
  result: boolean;
  correction: string;
}

const Feedback = ({ result, correction }: Props) => {
  return (
    <div className={style.feedback} data-correct={result}>
      {/* ICONS */}
      {result ? (
        <img
          src="/public/icons/icon_correct.svg"
          className={style.feedback_icon}
        />
      ) : (
        <img
          src="/public/icons/icon_wrong.svg"
          className={style.feedback_icon}
        />
      )}

      {/* TEXT */}
      {result ? (
        <span className={style.feedback_title}>Goed!</span>
      ) : (
        <div>
          <p className={style.feedback_text}>ANTWOORD:</p>
          <span className={style.feedback_title}>{correction}</span>
        </div>
      )}
    </div>
  );
};

export default Feedback;
