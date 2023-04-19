import React from "react";
import { useNavigate } from "react-router-dom";
import style from "./ErrorPage.module.css";

interface Props {
  code: number;
}

function ErrorPage({ code }: Props) {
  const navigator = useNavigate();

  const goBack = () => {
    navigator(-3);
  };

  let content;
  if (code === 403) {
    content = "Je hebt geen toestemming om deze pagina te bezoeken";
  } else if (code === 404) {
    content = "Deze pagina kan niet gevonden worden";
  }

  return (
    <div className={style.error_container}>
      <div className={style.error_card}>
        <h1>{code} Error</h1>
        <p>{content}</p>
        <button type="button" className="btn btn-primary" onClick={goBack}>
          Terug
        </button>
      </div>
    </div>
  );
}

export default ErrorPage;
