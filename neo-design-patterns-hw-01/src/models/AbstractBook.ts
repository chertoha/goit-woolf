import { Author } from "./Author";

export abstract class AbstractBook {
  private _name: string;
  private _year: number;
  private _author: Author;

  constructor(name: string, year: number, author: Author) {
    this._name = name;
    this._year = year;
    this._author = author;
  }

  get name(): string {
    return this._name;
  }

  get year(): number {
    return this._year;
  }

  get author(): Author {
    return this._author;
  }

  abstract getDescription(): string;
}
