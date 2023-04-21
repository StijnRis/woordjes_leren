import React, { useState, useRef, useEffect } from "react";
import HintButton from "../ui/buttons/HintButton";
import HintSentence from "../exercise/HintSentence";
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

  const keyboardHandler = (event: KeyboardEvent) => {
    if (event.key === "Enter" || event.code === "NumpadEnter") {
      validateAnswer();
    }
  };

  //Handle keyboard inputs
  useEffect(() => {
    if (inputRef.current !== null) {
      inputRef.current.addEventListener("keydown", keyboardHandler);

      // cleanup this component
      return () => {
        if (inputRef.current !== null) {
          inputRef.current.removeEventListener("keydown", keyboardHandler);
        }
      };
    }
  }, [inputRef]);

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
          autoComplete="off"
        />
      </div>

      <SubmitButton clickHandler={validateAnswer}>Controleren</SubmitButton>
    </div>
  );
};

export default TranslateExercise;
