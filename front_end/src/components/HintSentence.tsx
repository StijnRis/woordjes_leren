import React from 'react'

interface Props {
    word: string
    children: string
}

const HintSentence = ({word, children}: Props) => {
    //Children is the hint sentence
    const wordIndex = children.toLowerCase().indexOf(word.toLowerCase());
    if (wordIndex == -1) {
        throw new Error("Word " + word + " is not found in the hint sentence: " + children);
    }

    const wordInSentence = children.substring(wordIndex, wordIndex + word.length);
    const sentenceParts = children.split(wordInSentence);

    console.log(wordIndex, word, wordInSentence);

    return (
        <div id="hint-sentence">
            "{sentenceParts[0]}
            <strong>{wordInSentence}</strong>
            {sentenceParts[1]}"
        </div>
    )
}

export default HintSentence