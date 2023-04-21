import { ReactNode } from "react";
import classes from "./Loading.module.css";

function Loading() {
  return (
    <div className={classes.loading_container}>
      <div className="spinner-border" role="status">
        <span className="visually-hidden">Loading...</span>
      </div>
      <h3>Loading...</h3>
    </div>
  );
}

export default Loading;
