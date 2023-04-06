import React, { useEffect, useState } from "react";
import Header from "../../components/Header";
import TranslateExercise from "../../components/TranslateExercise";
// import "./exercise.css";

const Exercise = () => {
  const [exerciseData, setExerciseData] = useState([]);

  interface exercise {
    name: string;
    language: string;
    usage: Array<string>;
  }
  const [currentExercise, setCurrentExercise] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/quiz/api/words", { mode: "no-cors" })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setExerciseData(data);
        setCurrentExercise(data["results"][0]);
      })
      .catch((err) => console.log(err.message));
  }, []);

  return (
    <>
      <Header></Header>
      <div className="exercise-container">
        <TranslateExercise
          language="Frans"
          word="Bonjour"
          hintSentence="Salut, ça va? Moi je m’appelle Stéphane. Bonjour Stéphane, moi c’est Nicolas."
        />
      </div>
    </>
  );
};

export default Exercise;
