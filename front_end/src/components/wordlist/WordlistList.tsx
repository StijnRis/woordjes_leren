import Wordlist from "./WordlistOverview";
interface Props {
  wordlists: Array<WordlistData>;
}

type WordlistData = {
  pk: number;
  name: string;
};

function WordlistsList({ wordlists }: Props) {
  return (
    <div className="row">
      {wordlists.map((wordlist) => {
        console.log(wordlist.pk);
        return (
          <div className="col-sm-6 mb-3 mb-sm-0" key={wordlist.pk}>
            <Wordlist
              id={wordlist.pk}
              progress={0}
              title={wordlist.name}
            ></Wordlist>
          </div>
        );
      })}
    </div>
  );
}

export default WordlistsList;
