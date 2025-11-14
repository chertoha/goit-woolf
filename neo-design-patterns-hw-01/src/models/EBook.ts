import { AbstractBook } from "./AbstractBook";
import { Author } from "./Author";

export class EBook extends AbstractBook {
  private _url: string;

  constructor(name: string, year: number, author: Author, url: string) {
    super(name, year, author);
    this._url = url;

    this.author.addBook(this);
  }

  get url() {
    return this._url;
  }

  getDescription(): string {
    return `E-book "${this.name}" by ${this.author.name} (${this.year}) - Available at: ${this.url}`;
  }
}
