interface Props {
  onCancel: () => void;
  onConfirm: () => void;
}

function ModalDelete({ onCancel, onConfirm }: Props) {
  var tabIndex = -1;
  return (
    <div
      className="modal fade show"
      tabIndex={tabIndex}
      id="ModalDelete"
      style={{ display: "block" }}
    >
      <div className="modal-dialog">
        <div className="modal-content">
          <div className="modal-header">
            <h1 className="modal-title">Verwijder woordenlijst</h1>
            <button
              type="button"
              className="btn-close"
              onClick={onCancel}
            ></button>
          </div>
          <div className="modal-body">
            <p>Weet je zeker dat je de lijst wilt verwijderen?</p>
          </div>
          <div className="modal-footer">
            <button
              type="button"
              className="btn btn-secondary"
              onClick={onCancel}
            >
              Close
            </button>
            <button
              type="button"
              className="btn btn-danger"
              onClick={onConfirm}
            >
              Verwijder lijst
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default ModalDelete;
