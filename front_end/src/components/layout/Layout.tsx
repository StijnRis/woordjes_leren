import { ReactNode } from "react";
import Navigation from "./Navigation/NavigationOld";
import Footer from "./Footer/Footer";
import classes from "./Layout.module.css";

interface Props {
  children: ReactNode;
}

function Layout({ children }: Props) {
  return (
    <div className={classes.layout_grid}>
      <Navigation />
      <main className={classes.main}>{children}</main>
      <Footer />
    </div>
  );
}

export default Layout;
