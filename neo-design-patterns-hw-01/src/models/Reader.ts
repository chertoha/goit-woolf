import { Copy } from "./Copy";

export class Reader {
  private static nextid: number = 1;

  private _id: number;
  private _name: string;
  private _borrowedCopies: Copy[] = [];

  constructor(name: string) {
    this._id = Reader.nextid++;
    this._name = name;
  }

  get id(): number {
    return this._id;
  }

  get name(): string {
    return this._name;
  }

  get borrowedCopies(): Copy[] {
    return this._borrowedCopies;
  }

  borrowCopy(copy: Copy): void {
    this._borrowedCopies.push(copy);
  }

  returnBook(copy: Copy): void {
    this._borrowedCopies = this._borrowedCopies.filter((с) => с !== copy);
  }
}
