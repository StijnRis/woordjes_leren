const DUMMY_DATA = {
  pk: 2,
  name: "Woordenlijst van Admin",
  date_published: "2023-03-29T19:15:24.778640+02:00",
  visibility: "pr",
  owner: {
    pk: 1,
    username: "admin",
  },
  materials: [
    {
      pk: 4,
      date_added: "2023-04-04T20:12:35+02:00",
      translation: {
        pk: 1,
        wrong_tries: 0,
        correct_tries: 0,
        difficulty: 1.0,
        word: {
          pk: 1,
          name: "lopen",
          language: {
            pk: 1,
            name: "Nederlands",
          },
          usage: [
            {
              pk: 1,
              sentence: "Wij lopen naar school.",
            },
          ],
        },
        translation: {
          pk: 3,
          name: "to walk",
          language: {
            pk: 2,
            name: "English",
          },
          usage: [],
        },
      },
    },
    {
      pk: 4,
      date_added: "2023-04-04T20:12:35+02:00",
      translation: {
        pk: 1,
        wrong_tries: 0,
        correct_tries: 0,
        difficulty: 1.0,
        word: {
          pk: 1,
          name: "slapen",
          language: {
            pk: 1,
            name: "Nederlands",
          },
          usage: [
            {
              pk: 1,
              sentence: "Wij slapen op school.",
            },
          ],
        },
        translation: {
          pk: 3,
          name: "to sleep",
          language: {
            pk: 2,
            name: "English",
          },
          usage: [
            {
              pk: 21309,
              sentence: "We sleep at school",
            },
          ],
        },
      },
    },
  ],
};

export default DUMMY_DATA;
