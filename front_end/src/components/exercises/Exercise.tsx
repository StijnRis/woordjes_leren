import React from "react";
import { motion, AnimatePresence } from "framer-motion";
import classes from "../../pages/Exersice/ExercisePage.module.css";

interface Props {
  children: JSX.Element | JSX.Element[];
}

const Exercise = ({ children }: Props) => {
  return (
    <motion.div
      className={classes.exercise}
      initial={{ x: "100%", opacity: 0 }}
      animate={{ x: 0, opacity: 1 }}
      exit={{ x: "-100%", opacity: 0 }}
      transition={{ duration: 0.2 }}
    >
      {children}
    </motion.div>
  );
};

export default Exercise;
