import { useEffect, useRef, useState } from "react";
import Card from "../ui/card/Card";
import classes from "./newWordlistForm.module.css";
import { useNavigate } from "react-router-dom";
import Loading from "../ui/loading/Loading";

interface Props {
  id: number;
  handleData: (data: Wordlist) => void;
  children: JSX.Element | JSX.Element[];
}

function Wordlist({ id, handleData, children }: Props) {
  const navigate = useNavigate();

  const [isLoaded, setIsLoaded] = useState<boolean>(true);

  // Getting data
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
        handleData(data);
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

  if (!isLoaded) {
    return <Loading />;
  } else {
    return children;
  }
}

export default Wordlist;
