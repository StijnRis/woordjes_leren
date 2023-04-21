import React from "react";
import style from "./Feedback.module.css";
import { motion } from "framer-motion";

interface Props {
  result: boolean;
  correction: string;
  isOpen: boolean;
}

const Feedback = ({ result, correction, isOpen }: Props) => {
  const variants = {
    open: { opacity: 1, y: 0, pointerEvents: "all" },
    closed: { opacity: 0, y: 10, pointerEvents: "none" },
  };

  return (
    <motion.div
      className={style.feedback}
      data-correct={result}
      initial={"closed"}
      animate={isOpen ? "open" : "closed"}
      variants={variants}
      transition={{ duration: 0.1 }}
    >
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
          <span className={style.feedback_title}>
            {isOpen ? correction : ""}
          </span>
        </div>
      )}
    </motion.div>
  );
};

export default Feedback;
