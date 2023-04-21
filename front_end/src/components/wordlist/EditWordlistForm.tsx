import { useRef } from "react";
import Card from "../ui/card/Card";

interface Props {
  onSaveWordlist: (data: object) => void;
  wordlist: Wordlist;
}

function EditWordListForm({ onSaveWordlist, wordlist }: Props) {
  const refName = useRef<HTMLInputElement>(null);

  function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();

    if (refName.current !== null) {
      const enteredName = refName.current.value;

      wordlist.name = enteredName;

      onSaveWordlist(wordlist);
    }
  }

  return (
    <Card>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="name">Name</label>
          <input type="text" required id="name" ref={refName} />
        </div>
        <div>
          <button>Add wordlist</button>
        </div>
      </form>
    </Card>
  );
}

export default EditWordListForm;
