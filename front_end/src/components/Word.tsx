import React from "react";

interface Props {
  word: string;
}

const Word = ({ word }: Props) => {
  return <span id="word">{word}</span>;
};

export default Word;
