import { Routes, Route } from "react-router-dom";
import Home from "./pages/Home/Home";
import NewWordlist from "./pages/NewWordlist/NewWordList";
import Exercise from "./pages/Exersice/Exercise";
import Navigation from "./components/layout/navigation";

const App = () => {
  return (
    <div>
      <Navigation></Navigation>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/new-wordlist" element={<NewWordlist />} />
        <Route path="/exercise" element={<Exercise />} />
      </Routes>
    </div>
  );
};

export default App;
