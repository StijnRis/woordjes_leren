import React from "react";

interface Props {
  word: string;
  children: string;
}

const HintSentence = ({ word, children }: Props) => {
  //Children is the hint sentence
  const wordIndex = children.toLowerCase().indexOf(word.toLowerCase());
  var hintSentence;
  if (wordIndex == -1) {
    hintSentence = children;
  } else {
    const wordInSentence = children.substring(
      wordIndex,
      wordIndex + word.length
    );
    const sentenceParts = children.split(wordInSentence);

    hintSentence = (
      <>
        {sentenceParts[0]}
        <strong>{wordInSentence}</strong>
        {sentenceParts[1]}
      </>
    );
  }
  return <div id="hint-sentence">"{hintSentence}"</div>;
};

export default HintSentence;
