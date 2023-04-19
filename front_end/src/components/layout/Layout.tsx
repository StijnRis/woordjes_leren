import { ReactNode } from "react";
import Navigation from "./Navigation";
import classes from "./Layout.module.css";

interface Props {
  children: ReactNode;
}

function Layout({ children }: Props) {
  return (
    <div className={classes.wrapper}>
      <Navigation />
      <main className={classes.main}>{children}</main>
    </div>
  );
}

export default Layout;
