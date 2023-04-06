import Wordlist from "./Wordlist";

function Wordlists() {
  return (
    <div>
      <h2>Jouw woordenlijsten</h2>
      <div className="row">
        <Wordlist title="a"></Wordlist>
        <Wordlist title="b"></Wordlist>
        <Wordlist title="c"></Wordlist>
      </div>
    </div>
  );
}

export default Wordlists;
