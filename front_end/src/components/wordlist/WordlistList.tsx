import Wordlist from "./Wordlist";
interface Props {
  wordlists: Array<WordlistData>;
}

type WordlistData = {
  id: number;
  name: string;
  progress: number;
};

function WordlistsList({ wordlists }: Props) {
  return (
    <div className="row">
      {wordlists.map((wordlist) => {
        return (
          <Wordlist
            key={wordlist.id}
            progress={wordlist.progress}
            title={wordlist.name}
          ></Wordlist>
        );
      })}
    </div>
  );
}

export default WordlistsList;
