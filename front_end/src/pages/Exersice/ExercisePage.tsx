import React, { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import useStateRef from "react-usestateref";
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
  //Get id
  const params = useParams();
  const id = params.id;

  const navigate = useNavigate();

  const [exerciseData, setExerciseData] = useState<WordlistData>();
  const [wordlistLength, setWordListLength] = useState<number>(0);
  const [exerciseIndex, setExerciseIndex, exerciseIndexRef] =
    useStateRef<number>(0);
  const [correctCount, setCorrectCount, correctCountRef] =
    useStateRef<number>(0);

  const [feedbackVisible, setFeedbackVisibility, feedbackVisibleRef] =
    useStateRef<boolean>(false);

  const [isLoaded, setIsLoaded] = useState<boolean>(true);
  const [correct, setCorrect] = useState<boolean>(false);
  const [exerciseFinished, setExerciseFinished, exerciseFinishedRef] =
    useStateRef<boolean>(false);

  // Get data
  useEffect(() => {
    fetch(`http://localhost:8000/quiz/api/wordlists/${id}/`)
      .then((response) => {
        if ([403, 404].includes(response.status)) {
          throw response;
        }
        return response;
      })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setExerciseData(data);
        setWordListLength(data.materials.length);
        setIsLoaded(true);
      })
      .catch((err) => {
        if (err instanceof Response) {
          if (err.status === 403) {
            navigate("/403");
          } else if (err.status === 404) {
            navigate("/404");
          }
        } else {
          console.log(err);
        }
      });
  }, []);

  const handleFeedback = (validationResultCorrect: boolean) => {
    if (feedbackVisibleRef.current) {
      nextExercise();

      setFeedbackVisibility(false);
    } else {
      //Handle result
      if (validationResultCorrect) {
        setCorrectCount(correctCountRef.current + 1);
      }
      setCorrect(validationResultCorrect);

      setFeedbackVisibility(true);
    }
  };

  const nextExercise = () => {
    setExerciseIndex(exerciseIndexRef.current + 1);

    if (isLoaded && exerciseIndexRef.current === wordlistLength) {
      setExerciseFinished(true);
    }
  };

  let content;

  if (isLoaded && exerciseData !== undefined) {
    if (!exerciseFinishedRef.current) {
      var currentExercise = exerciseData.materials[exerciseIndex];
      if (currentExercise === undefined) {
        content = <span>This exercise can not be loaded</span>;
      }

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
            feedbackHandler={handleFeedback}
          />
          {feedbackVisible && (
            <Feedback result={correct} correction={translation} />
          )}
        </>
      );
    } else {
      content = (
        <>
          <h1>Finished</h1>
          <p>Correct: {correctCount}</p>
          <p>Wrong: {wordlistLength - correctCount}</p>
        </>
      );
    }
  } else {
    content = (
      <div className={classes.loading_container}>
        <div className="spinner-border" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
        <h3>Loading...</h3>
      </div>
    );
  }

  return (
    <div className={classes.exercise_container}>
      <div className={classes.exercise}>{content}</div>
    </div>
  );
};

export default ExercisePage;
