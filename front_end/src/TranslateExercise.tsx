import React, { useState } from "react";
import Word from "./components/Word";
import HintButton from "./components/HintButton";
import HintSentence from "./components/HintSentence";
import SubmitButton from "./components/SubmitButton";

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
