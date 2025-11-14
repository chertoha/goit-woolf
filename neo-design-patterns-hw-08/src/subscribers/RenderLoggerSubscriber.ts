import { RenderEventSubscriber } from "../interfaces/RenderEventSubscriber";
import { RenderContext } from "../interfaces/RenderContext";

export class RenderLoggerSubscriber implements RenderEventSubscriber {
  update(context: RenderContext): void {
    const { type, content, items, level } = context;
    switch (type) {
      case "Paragraph":
        console.log(`[Log] Rendered Paragraph (${content.length} chars)`);
        break;
      case "List":
        console.log(`[Log] Rendered List (${items?.length ?? 0} items)`);
        break;
      case "Section":
        console.log(`[Log] Rendered Section ("${content}", level ${level})`);
        break;
    }
  }
}
