import { Reader } from "../models/Reader";
import { Copy } from "../models/Copy";

export class BorrowService {
  borrow(reader: Reader, copy: Copy): boolean {
    if (!copy.isAvailable) return false;

    reader.borrowCopy(copy);
    copy.isAvailable = false;

    return true;
  }

  returnBook(reader: Reader, copy: Copy): void {
    reader.returnBook(copy);
    copy.isAvailable = true;
  }
}
