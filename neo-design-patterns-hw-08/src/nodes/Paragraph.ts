import { DocNode } from "../interfaces/DocNode";
import { DocRenderer } from "../interfaces/DocRenderer";
import { RenderEventPublisher } from "../RenderEventPublisher";

export class Paragraph implements DocNode {
  constructor(private text: string, private renderer: DocRenderer) {}

  render(): string {
    const start = performance.now();
    const result = this.renderer.renderParagraph(this.text);
    const end = performance.now();

    RenderEventPublisher.notify({
      type: "Paragraph",
      content: this.text,
      renderTime: end - start,
    });

    return result;
  }
}
