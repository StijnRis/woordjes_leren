import WordlistList from "./WordlistList";

const DUMMY_DATA = [
  {
    id: 1,
    owner: {
      id: 2,
      username: "stijn",
    },
    name: "Woordenlijst van Stijn",
    progress: 0.2,
    date_published: "2023-03-29T17:57:54.870096+02:00",
    materials: [
      {
        date_added: "2023-04-04T20:11:10+02:00",
        translation: {
          id: 1,
          word: {
            name: "lopen",
            language: {
              name: "Nederlands",
            },
          },
          translation: {
            name: "to walk",
            language: {
              name: "English",
            },
            usage: [],
          },
          wrong_tries: 0,
          correct_tries: 0,
          difficulty: 1.0,
        },
      },
      {
        date_added: "2023-04-04T20:12:10+02:00",
        translation: {
          id: 2,
          word: {
            name: "lezen",
            language: {
              name: "Nederlands",
            },
          },
          translation: {
            name: "to read",
            language: {
              name: "English",
            },
            usage: [],
          },
          wrong_tries: 0,
          correct_tries: 0,
          difficulty: 1.0,
        },
      },
    ],
  },
  {
    id: 2,
    owner: {
      id: 3,
      username: "Jelmer",
    },
    name: "Woordenlijst van Jelmer",
    date_published: "2023-03-29T17:57:54.870096+02:00",
    progress: 0.5,
    materials: [
      {
        date_added: "2023-04-04T20:11:10+02:00",
        translation: {
          id: 1,
          word: {
            name: "lopen",
            language: {
              name: "Nederlands",
            },
          },
          translation: {
            name: "to walk",
            language: {
              name: "English",
            },
            usage: [],
          },
          wrong_tries: 0,
          correct_tries: 0,
          difficulty: 1.0,
        },
      },
      {
        date_added: "2023-04-04T20:12:10+02:00",
        translation: {
          id: 2,
          word: {
            name: "lezen",
            language: {
              name: "Nederlands",
            },
          },
          translation: {
            name: "to read",
            language: {
              name: "English",
            },
            usage: [],
          },
          wrong_tries: 0,
          correct_tries: 0,
          difficulty: 1.0,
        },
      },
    ],
  },
];

function AllWordlists() {
  return (
    <section>
      <h2>Alle woordenlijsten</h2>
      <WordlistList wordlists={DUMMY_DATA}></WordlistList>
    </section>
  );
}

export default AllWordlists;
