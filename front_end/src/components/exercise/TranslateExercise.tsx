import React, { useState } from "react";
import Word from "./Word";
import HintButton from "../ui/buttons/HintButton";
import HintSentence from "./HintSentence";
import SubmitButton from "../ui/buttons/SubmitButton";
import style from "./TranslateExercise.module.css";
import exercise_style from "../../pages/Exersice/ExercisePage.module.css";

interface Props {
  language: string;
  word: string;
  hintSentence: string;
  exerciseHandler: Function
}

const TranslateExercise = ({ language, word, hintSentence, exerciseHandler }: Props) => {
  const [hintVisible, setHintVisibility] = useState(false);

  //Check value
  const validateAnswer = (answer: string) => {
    const result = true;
    exerciseHandler(result);
    return result;
  }

  return (
    <div className={exercise_style.exercise + " " + style.translate}>
      <span id={exercise_style.instruction}>Vertaal naar het {language}</span>

      <div className={exercise_style.flex}>
        <span id={exercise_style.word}>{word}</span>
        <HintButton
          onClick={() => {
            setHintVisibility(!hintVisible);
          }}
        />
      </div>

      {hintVisible && <HintSentence word={word}>{hintSentence}</HintSentence>}

      <div className={exercise_style.content}>
        <input type="text" id={style.word_input} />
      </div>

      <SubmitButton clickHandler={validateAnswer}>Controleren</SubmitButton>
    </div>
  );
};

export default TranslateExercise;
