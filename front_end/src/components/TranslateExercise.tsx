import React, { useState } from "react";
import Word from "./Word";
import HintButton from "./HintButton";
import HintSentence from "./HintSentence";
import SubmitButton from "./SubmitButton";
import classes from "./TranslateExercise.module.css";

interface Props {
  language: string;
  word: string;
  hintSentence: string;
}

const TranslateExercise = ({ language, word, hintSentence }: Props) => {
  const [hintVisible, setHintVisibility] = useState(false);

  return (
    <div className="exercise translate">
      <span id="instruction">Vertaal naar het {language}</span>

      <div className="flex">
        <Word word={word} />
        <HintButton
          onClick={() => {
            setHintVisibility(!hintVisible);
          }}
        />
      </div>

      {hintVisible && <HintSentence word={word}>{hintSentence}</HintSentence>}

      <div className="content">
        <input type="text" id="word-input" />
      </div>

      <SubmitButton>Controleren</SubmitButton>
    </div>
  );
};

export default TranslateExercise;
