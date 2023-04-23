import AllWordlists from "../../components/wordlist/AllWordlists";
import style from "./HomePage.module.css";
import main_style from "../../components/layout/Layout.module.css";
import { motion } from "framer-motion";

const HomePage = () => {
  const variants = {
    fade_in: { opacity: 1, y: 0 },
    invisible: { opacity: 0 },
    invisible_and_up: { opacity: 0, y: "-100%" },
  };

  return (
    <>
      <section className={style.banner}>
        <motion.div
          className={style.banner_content}
          animate="fade_in"
          initial="invisible_and_up"
          transition={{ duration: 0.5 }}
          variants={variants}
        >
          <h1>WRTS. Maar dan anders</h1>
          <p>Wij hebben namelijk super toffe animaties</p>
        </motion.div>
      </section>
      <section className={style.main_content}>
        <motion.div
          className={main_style.wrapper}
          animate="fade_in"
          initial="invisible"
          transition={{ duration: 0.5, delay: 0.3 }}
          variants={variants}
        >
          <AllWordlists />
        </motion.div>
      </section>
    </>
  );
};
export default HomePage;
