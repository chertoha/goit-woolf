export class DocumentBuilder {
  private header: string = "";
  private body: string = "";
  private footer: string = "";

  constructor() {}

  addHeader(header: string) {
    this.header = header;
    return this;
  }

  addBody(body: string) {
    this.body = body;
    return this;
  }

  addFooter(footer: string) {
    this.footer = footer;
    return this;
  }

  build() {
    return this.header + "\n\n" + this.body + "\n\n" + this.footer;
  }
}
