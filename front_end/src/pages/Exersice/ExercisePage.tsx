import React, { useEffect, useState } from "react";
import Header from "../../components/Header";
import TranslateExercise from "../../components/exercise/TranslateExercise";
import Feedback from "../../components/exercise/Feedback";
import classes from "./ExercisePage.module.css";
import HintSentence from "../../components/exercise/HintSentence";
import DUMMY_DATA from "./DUMMY_DATA";

interface Material {
  pk: number;
  date_added: string;
  translation: {
    pk: number;
    wrong_tries: number;
    correct_tries: number;
    difficulty: number;
    word: {
      name: string;
      language: {
        pk: number;
        name: string;
      };
      usage: {
        pk: number;
        sentence: string;
      }[];
    };
    translation: {
      name: string;
      language: {
        pk: number;
        name: string;
      };
      usage: {
        pk: number;
        sentence: string;
      }[];
    };
  };
}

interface WordlistData {
  pk: number;
  name: string;
  date_published: string;
  visibility: string;
  owner: {
    pk: number;
    username: string;
  };
  materials: Material[];
}

const ExercisePage = () => {
  const [exerciseData, setExerciseData] = useState<WordlistData>(DUMMY_DATA);
  const [exerciseIndex, setExerciseIndex] = useState<number>(0);
  const [correctCount, setCorrectCount] = useState<number>(0);

  const [isLoaded, setIsLoaded] = useState<boolean>(true);
  const [feedbackVisible, setFeedbackVisibility] = useState<boolean>(false);
  const [correct, setCorrect] = useState<boolean>(false);
  const [exerciseFinished, setExerciseFinished] = useState<boolean>(false);

  // Get data
  useEffect(() => {
    // fetch("http://127.0.0.1:8000/quiz/api/words", { mode: "no-cors" })
    //   .then((response) => response.json())
    //   .then((data) => {
    //     console.log(data);
    //     setExerciseData(data);
    //     setCurrentExercise(data["results"][0]);
    //   })
    //   .catch((err) => console.log(err.message));
    setExerciseData(DUMMY_DATA);

    setIsLoaded(true);
  }, []);

  const feedbackHandler = (validationResultCorrect: boolean) => {
    if (validationResultCorrect) {
      setCorrectCount(correctCount + 1);
    }
    setCorrect(validationResultCorrect);
    setFeedbackVisibility(true);
  };

  const nextExercise = () => {
    console.log(exerciseIndex + 1, exerciseData.materials.length);
    setExerciseIndex(exerciseIndex + 1);

    if (exerciseIndex + 1 === exerciseData.materials.length) {
      setExerciseFinished(true);
    }
  };

  //Handle keyboard inputs
  const handleKeyPress = (event: any) => {
    if (event.key === "Enter" && feedbackVisible) {
      setFeedbackVisibility(false);
      nextExercise();
    }
  };

  let content;

  console.log("Exercise finished: " + exerciseFinished);
  if (!exerciseFinished) {
    var currentExercise = exerciseData.materials[exerciseIndex];
    if (currentExercise === undefined) {
      content = <span>This exercise can not be loaded</span>;
    }

    if (isLoaded) {
      var word = currentExercise.translation.translation.name;
      var translation = currentExercise.translation.word.name;
      var language = currentExercise.translation.word.language.name;

      var usages = currentExercise.translation.translation.usage;
      var hintSentence = "";
      if (usages.length > 0) {
        hintSentence = usages[0].sentence;
      }

      content = (
        <>
          <TranslateExercise
            language={language}
            word={word}
            translation={translation}
            hintSentence={hintSentence}
            feedbackHandler={feedbackHandler}
          />
          {feedbackVisible && (
            <Feedback result={correct} correction={translation} />
          )}
        </>
      );
    }
  } else {
    content = (
      <>
        <h1>Finished</h1>
        <p>Correct: {correctCount}</p>
        <p>Wrong: {exerciseData.materials.length - correctCount}</p>
      </>
    );
  }

  return (
    <div className={classes.exercise_container} onKeyPress={handleKeyPress}>
      <div className={classes.exercise}>{content}</div>
    </div>
  );
};

export default ExercisePage;
