import { useState } from "react";
import ModalDelete from "../ModalDelete";
import Card from "../ui/card/Card";

interface Props {
  id: number;
  title: string;
  progress: number;
}

function Wordlist({ id, title, progress }: Props) {
  const [modalIsOpen, setModalIsOpen] = useState(false);

  function handleDelete() {
    setModalIsOpen(true);
  }

  function handleCancelDelete() {
    setModalIsOpen(false);
  }

  function handleConfirmDelete() {
    setModalIsOpen(false);
  }

  var progressPercentage = progress * 100;
  return (
    <>
      <Card>
        <div className="card">
          <div className="card-header">Recent geoefend</div>
          <div className="card-body">
            <h5 className="card-title">{title}</h5>
            <div
              className="progress"
              role="progressbar"
              aria-label="Basic example"
              aria-valuenow={0}
              aria-valuemin={0}
              aria-valuemax={1}
            >
              <div
                className="progress-bar"
                style={{ width: progressPercentage + "%" }}
              ></div>
            </div>
            <p className="card-text">{progressPercentage}% goed.</p>
            <a href={"/exercise/" + id} className="btn btn-primary">
              Oefenen
            </a>
            <button type="button" className="btn btn-secondary">
              Bewerken
            </button>
            <button
              type="button"
              className="btn btn-danger"
              onClick={handleDelete}
            >
              Verwijderen
            </button>
          </div>
        </div>
      </Card>
      {modalIsOpen && (
        <ModalDelete
          onCancel={handleCancelDelete}
          onConfirm={handleConfirmDelete}
        />
      )}
    </>
  );
}

export default Wordlist;
