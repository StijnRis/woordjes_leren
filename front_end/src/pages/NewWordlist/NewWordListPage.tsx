import NewWordListForm from "../../components/wordlist/NewWordlistForm";
import { useNavigate } from "react-router-dom";

const NewWordlistPage = () => {
  const navigate = useNavigate();

  function handleAddMeetup(data: object) {
    navigate("/", { replace: true });
  }

  return (
    <section>
      <h1>Add new Wordlist</h1>
      <NewWordListForm onAddMeetup={handleAddMeetup} />
    </section>
  );
};
export default NewWordlistPage;
