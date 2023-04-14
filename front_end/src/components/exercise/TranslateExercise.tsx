import React, { useState, useRef } from "react";
import Word from "./Word";
import HintButton from "../ui/buttons/HintButton";
import HintSentence from "./HintSentence";
import SubmitButton from "../ui/buttons/SubmitButton";
import style from "./TranslateExercise.module.css";
import exercise_style from "../../pages/Exersice/ExercisePage.module.css";

interface Props {
  language: string;
  word: string;
  translation: string;
  hintSentence: string;
  feedbackHandler: Function;
}

const TranslateExercise = ({
  language,
  word,
  translation,
  hintSentence,
  feedbackHandler,
}: Props) => {
  const [hintVisible, setHintVisibility] = useState(false);
  const inputRef = useRef<HTMLInputElement>(null);

  //Check value
  const validateAnswer = () => {
    if (inputRef.current !== null) {
      var answer = inputRef.current.value;
      var correct = answer.toLowerCase() == translation.toLowerCase();

      feedbackHandler(correct);

      //Empty field
      inputRef.current.value = "";
    }
  };

  //Handle keyboard inputs
  const handleKeyPress = (event: any) => {
    if (event.key === "Enter") {
      validateAnswer();
    }
  };

  return (
    <div className={style.translate}>
      <span id={exercise_style.instruction}>Vertaal naar het {language}</span>

      <div className={exercise_style.flex}>
        <span id={exercise_style.word}>{word}</span>
        {hintSentence !== "" && (
          <HintButton
            onClick={() => {
              setHintVisibility(!hintVisible);
            }}
          />
        )}
      </div>

      {hintVisible && <HintSentence word={word}>{hintSentence}</HintSentence>}

      <div className={exercise_style.content}>
        <input
          type="text"
          id={style.word_input}
          ref={inputRef}
          onKeyPress={handleKeyPress}
        />
      </div>

      <SubmitButton clickHandler={validateAnswer}>Controleren</SubmitButton>
    </div>
  );
};

export default TranslateExercise;
