import React from 'react'
import Header from './components/Header'
import TranslateExcersice from './TranslateExcersice'

const ExerciseApp = () => {
  return (
    <>
      <Header></Header>
      <div className="exercise-container">
        <TranslateExcersice language='Nederlands' word='Bonjour' hintSentence='Salut, ça va? Moi je m’appelle Stéphane. Bonjour Stéphane, moi c’est Nicolas.'/>
      </div>
    </>
  )
}

export default ExerciseApp
