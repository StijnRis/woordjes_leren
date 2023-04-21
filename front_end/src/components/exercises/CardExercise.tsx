import React, { useState, useRef, useEffect } from "react";
import { motion } from "framer-motion";
import HintButton from "../ui/buttons/HintButton";
import HintSentence from "../exercise/HintSentence";
import SubmitButton from "../ui/buttons/SubmitButton";
import style from "./CardExercise.module.css";
import exercise_style from "../../pages/Exersice/ExercisePage.module.css";

interface Props {
  from_language: string;
  to_language: string;
  from_word: string;
  to_word: string;
  from_sentence: string;
  to_sentence: string;
  nextExerciseHandler: Function;
}

const CardExercise = ({
  from_language,
  to_language,
  from_word,
  to_word,
  from_sentence,
  to_sentence,
  nextExerciseHandler,
}: Props) => {
  const [hintVisible, setHintVisibility] = useState(false);
  const [isFlipped, setIsFlipped] = useState(false);

  const variants = {
    normal: { transform: "rotateY(0deg)" },
    flipped: { transform: "rotateY(180deg)" },
    exit: { transform: "rotateY(180deg)" },
  };

  return (
    <motion.div
      className={style.card}
      onClick={() => {
        setIsFlipped(!isFlipped);
      }}
      initial={"normal"}
      animate={isFlipped ? "flipped" : "normal"}
      exit="exit"
      variants={variants}
    >
      {/* FRONT */}
      <div className={style.card_front}>
        <span id={exercise_style.instruction}>Klik om vertaling te zien</span>

        <div className={exercise_style.flex}>
          <span id={exercise_style.word}>{from_word}</span>
          {from_sentence !== "" && (
            <HintButton
              onClick={() => {
                setHintVisibility(!hintVisible);
              }}
            />
          )}
        </div>

        {hintVisible && (
          <HintSentence word={from_word}>{from_sentence}</HintSentence>
        )}
      </div>

      {/* BACK */}
      <div className={style.card_back}>
        <span id={exercise_style.instruction}>Klik om origineel te zien</span>

        <div className={exercise_style.flex}>
          <span id={exercise_style.word}>{to_word}</span>
        </div>

        <div className={exercise_style.content}>
          {from_sentence !== "" && (
            <HintSentence word={from_word}>{from_sentence}</HintSentence>
          )}
          {to_sentence !== "" && (
            <HintSentence word={to_sentence}>{to_sentence}</HintSentence>
          )}
        </div>

        <SubmitButton
          clickHandler={() => {
            nextExerciseHandler();
          }}
        >
          Volgende
        </SubmitButton>
      </div>
    </motion.div>
  );
};

export default CardExercise;
