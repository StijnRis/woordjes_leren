import { Routes, Route } from "react-router-dom";
import HomePage from "./pages/Home/HomePage";
import NewWordlistPage from "./pages/NewWordlist/NewWordListPage";
import ExercisePage from "./pages/Exersice/ExercisePage";
import ErrorPage from "./pages/Error/ErrorPage";
import Layout from "./components/layout/Layout";

const App = () => {
  return (
    <Layout>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/new-wordlist" element={<NewWordlistPage />} />
        <Route path="/exercise/:id" element={<ExercisePage />} />
        <Route path="/403" element={<ErrorPage code={403} />} />
        <Route path="/404" element={<ErrorPage code={404} />} />
      </Routes>
    </Layout>
  );
};

export default App;
