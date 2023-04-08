import { Routes, Route } from "react-router-dom";
import HomePage from "./pages/Home/HomePage";
import NewWordlistPage from "./pages/NewWordlist/NewWordListPage";
import ExercisePage from "./pages/Exersice/ExercisePage";
import Layout from "./components/layout/Layout";

const App = () => {
  return (
    <Layout>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/new-wordlist" element={<NewWordlistPage />} />
        <Route path="/exercise" element={<ExercisePage />} />
      </Routes>
    </Layout>
  );
};

export default App;
