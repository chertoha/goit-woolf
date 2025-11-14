import { ResumeImporter } from "../importer/ResumeImporter";

/**
 * Фасад: єдина точка входу.
 */
export class ResumePage {
  async init(jsonPath: string): Promise<void> {
    // TODO: Завантажити дані через fetchData
    // TODO: Імпортувати дані через ResumeImporter

    const data = await this.fetchData(jsonPath);
    const importer = new ResumeImporter(data);
    importer.import();
  }

  private async fetchData(path: string): Promise<unknown> {
    // TODO: Завантажити JSON з вказаного шляху
    const res = await fetch(path);
    if (!res.ok) throw new Error(`Failed to load JSON from ${path}`);
    return await res.json();
  }
}
