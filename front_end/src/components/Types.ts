interface Usage {
  pk: number;
  sentence: string;
}

interface Language {
  pk: number;
  name: string;
}

interface Word {
  pk: number;
  name: string;
  language: Language;
  usage: Usage[];
}

interface Translation {
  pk: number;
  wrong_tries: number;
  correct_tries: number;
  from_word: Word;
  to_word: Word;
}

interface Material {
  pk: number;
  date_added: string;
  translation: Translation;
}

interface Owner {
  pk: number;
  username: string;
}

interface Wordlist {
  pk: number;
  name: string;
  date_published: string;
  visibility: string;
  owner: Owner;
  materials: Material[];
}
