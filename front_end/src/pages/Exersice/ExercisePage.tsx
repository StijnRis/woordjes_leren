import React, { useEffect, useState } from "react";
import Header from "../../components/Header";
import TranslateExercise from "../../components/exercise/TranslateExercise";
import classes from "./ExercisePage.module.css";
import HintSentence from "../../components/exercise/HintSentence";

const DUMMY_DATA =
{
  "pk": 2,
  "name": "Woordenlijst van Admin",
  "date_published": "2023-03-29T19:15:24.778640+02:00",
  "visibility": "pr",
  "owner": {
      "pk": 1,
      "username": "admin"
  },
  "materials": [
      {
          "pk": 4,
          "date_added": "2023-04-04T20:12:35+02:00",
          "translation": {
              "pk": 1,
              "wrong_tries": 0,
              "correct_tries": 0,
              "difficulty": 1.0,
              "word": {
                  "pk": 1,
                  "name": "lopen",
                  "language": {
                      "pk": 1,
                      "name": "Nederlands"
                  },
                  "usage": [
                      {
                          "pk": 1,
                          "sentence": "Wij lopen naar school."
                      }
                  ]
              },
              "translation": {
                  "pk": 3,
                  "name": "to walk",
                  "language": {
                      "pk": 2,
                      "name": "English"
                  },
                  "usage": []
              }
          }
      },
      {
        "pk": 4,
        "date_added": "2023-04-04T20:12:35+02:00",
        "translation": {
            "pk": 1,
            "wrong_tries": 0,
            "correct_tries": 0,
            "difficulty": 1.0,
            "word": {
                "pk": 1,
                "name": "slapen",
                "language": {
                    "pk": 1,
                    "name": "Nederlands"
                },
                "usage": [
                    {
                        "pk": 1,
                        "sentence": "Wij slapen op school."
                    }
                ]
            },
            "translation": {
                "pk": 3,
                "name": "sleep",
                "language": {
                    "pk": 2,
                    "name": "English"
                },
                "usage": [
                  {
                    "pk": 21309,
                    "sentence": "We sleep at school"
                  }
                ]
            }
        }
    }
  ]
};

const ExercisePage = () => {
  const [isLoaded, setIsLoaded] = useState(true);

  interface Material {
    pk: number;
    date_added: string;
    translation: {
        pk: number;
        wrong_tries: number;
        correct_tries: number;
        difficulty: number;
        word: {
          name: string
          language: {
            pk: number,
            name: string
          },
          usage: {
            pk: number,
            sentence: string
          }[]
        },
        translation: {
          name: string,
          language: {
            pk: number,
            name: string
          },
          usage: {
            pk: number,
            sentence: string
          }[]
        }
    }
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
  const [exerciseData, setExerciseData] = useState<WordlistData>(DUMMY_DATA);
  
  //Exercise handling
  const [currentExercise, setCurrentExercise] = useState<Material>(exerciseData.materials[1]);

  let exercise_index = -1;
  const nextExercise = (result: boolean) => {
    console.log(result);
    if (exercise_index <= exerciseData.materials.length) {
      exercise_index++;
      setCurrentExercise(exerciseData.materials[exercise_index]);
    }
  }

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
    setCurrentExercise(exerciseData.materials[0]);
    nextExercise(false);

    setIsLoaded(true);
  }, []);

  if (isLoaded && currentExercise !== undefined) {
    var word = currentExercise.translation.translation.name;
    var language = currentExercise.translation.translation.language.name;
    
    var usages = currentExercise.translation.translation.usage;
    var hintSentence = "";
    if (usages.length > 0) {
      hintSentence = usages[0].sentence;
    }

    return (
      <>
        <div className={classes.exercise_container}>
          <TranslateExercise
            language={language}
            word={word}
            hintSentence={hintSentence}
            exerciseHandler={nextExercise}
          />
        </div>
      </>
    );
  }
};

export default ExercisePage;
