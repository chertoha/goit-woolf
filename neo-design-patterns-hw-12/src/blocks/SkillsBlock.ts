/**
 * Блок відображення навичок резюме
 */

import { Skills } from "../models/ResumeModel";
import { IBlock } from "./BlockFactory";

export class SkillsBlock implements IBlock {
  constructor(private d: Skills) {}

  /**
   * Рендеринг блоку навичок
   *
   * TODO: Реалізуйте метод для відображення категорій навичок
   * та їх списків у вигляді HTML елементів
   */
  render(): HTMLElement {
    // Створюємо секцію
    const sec = document.createElement("section");
    sec.className = "section skills";
    // sec.innerHTML = "<h2>Skills</h2>";

    // TODO: Створіть список навичок, згрупований за категоріями
    // Використайте Object.entries(this.d) для ітерації по всіх категоріях
    // Створіть для кожної категорії елемент списку з назвою категорії та списком навичок
    sec.innerHTML = `
      <h2>Skills</h2>
      <ul class="skills-list">
        <li><strong>core:</strong> ${this.d.core.join(", ")}</li>
        <li><strong>tools:</strong> ${this.d.tools.join(", ")}</li>
        <li><strong>languages:</strong> ${this.d.languages.join(", ")}</li>
      </ul>
    `;

    return sec;
  }
}
