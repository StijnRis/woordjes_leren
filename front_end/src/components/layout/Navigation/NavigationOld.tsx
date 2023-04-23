import { Link } from "react-router-dom";
import classes from "./Navigation.module.css";
import main_classes from "../Layout.module.css";

function Navigation() {
  return (
    <nav className="navbar navbar-expand-lg bg-body-tertiary">
      <div className={"container-fluid " + main_classes.wrapper}>
        <Link className={"navbar-brand " + classes.header} to="/">
          <img
            src="/src/assets/react.svg"
            alt="Logo"
            width="30"
            height="24"
            className="d-inline-block align-text-top"
          />
          Woordjes Leren
        </Link>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            <li className="nav-item">
              <Link to="/" className="nav-link active" aria-current="page">
                Home
              </Link>
            </li>
            <li className="nav-item">
              <Link to="/aa" className="nav-link">
                Geen idee
              </Link>
            </li>
            <li className="nav-item dropdown">
              <Link
                className="nav-link dropdown-toggle"
                to="/wordlists"
                role="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                Woordenlijsten
              </Link>
              <ul className="dropdown-menu">
                <li>
                  <Link to="/wordlists/my" className="dropdown-item">
                    Mijn Woordenlijsten
                  </Link>
                </li>
                <li>
                  <Link to="/wordlists/all" className="dropdown-item">
                    Alle woordenlijsten
                  </Link>
                </li>
                <li>
                  <hr className="dropdown-divider" />
                </li>
                <li>
                  <Link to="/a" className="dropdown-item">
                    Something else here
                  </Link>
                </li>
              </ul>
            </li>
            <li className="nav-item">
              <Link to="/the-future-and-beyond" className="nav-link disabled">
                The future
              </Link>
            </li>
          </ul>
          <form className="d-flex" role="search">
            <input
              className="form-control me-2"
              type="search"
              placeholder="Search"
              aria-label="Search"
            />
            <button className="btn btn-outline-success" type="submit">
              Zoeken
            </button>
          </form>
        </div>
      </div>
    </nav>
  );
}

export default Navigation;
