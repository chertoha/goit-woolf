import { AbstractBook } from "./AbstractBook";
import { Book } from "./Book";

export class Copy {
  private _book: AbstractBook;
  private _isAvailable: boolean = true;

  constructor(book: AbstractBook) {
    this._book = book;
  }

  get book(): AbstractBook {
    return this._book;
  }

  get isAvailable(): boolean {
    return this._isAvailable;
  }

  set isAvailable(availability: boolean) {
    this._isAvailable = availability;
  }

  isCopyAvailable(): boolean {
    return this._isAvailable;
  }
}
