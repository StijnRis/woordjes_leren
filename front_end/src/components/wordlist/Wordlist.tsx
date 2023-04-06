import { useState } from "react";
import ModalDelete from "../ModalDelete";

interface Props {
  title: string;
  progress: number;
}

function Wordlist({ title, progress }: Props) {
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
      <div className="col-sm-6 mb-3 mb-sm-0">
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
            <button type="button" className="btn btn-primary">
              Oefenen
            </button>
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
      </div>
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
