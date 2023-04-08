import { useRef } from "react";
import Card from "../ui/Card";
import classes from "./newWordlistForm.module.css";

interface Props {
  onAddMeetup: (data: object) => void;
}

function NewWordListForm({ onAddMeetup }: Props) {
  const refTitle = useRef<HTMLInputElement>(null);

  function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();

    if (refTitle.current !== null) {
      const enteredTitle = refTitle.current.value;

      const data = {
        title: enteredTitle,
      };

      onAddMeetup(data);
    }
  }

  return (
    <Card>
      <form className={classes.form} onSubmit={handleSubmit}>
        <div>
          <label htmlFor="title">Title</label>
          <input type="text" required id="title" ref={refTitle} />
        </div>
        <div className={classes.action}>
          <button>Add wordlist</button>
        </div>
      </form>
    </Card>
  );
}

export default NewWordListForm;
