/**
 * Блок відображення освіти в резюме
 */

import { Education } from "../models/ResumeModel";
import { IBlock } from "./BlockFactory";

export class EducationBlock implements IBlock {
  constructor(private d: Education[]) {}

  /**
   * Рендеринг блоку освіти
   *
   * TODO: Реалізуйте метод для відображення інформації про освіту
   */
  render(): HTMLElement {
    // Створюємо секцію
    const el = document.createElement("section");
    el.className = "section education";
    el.innerHTML = "<h2>Education</h2>";

    // TODO: Додайте до секції інформацію про навчальний заклад (this.d.institution),
    // отриманий ступінь (this.d.degree) та період навчання (this.d.graduation)

    this.d.forEach((edu) => {
      const item = document.createElement("div");
      item.className = "education-item";
      item.innerHTML = `
        <p><strong>${edu.degree} з ${edu.field}</strong></p>
        <p>${edu.institution}, ${edu.graduation}</p>
      `;
      el.appendChild(item);
    });

    // el.innerHTML = `
    //   <h2>Education</h2>
    //   <div class="education-item">
    //     <p><strong>${this.d.degree} з ${this.d.field}</strong></p>
    //     <p>${this.d.institution}, ${this.d.graduation}</p>
    //   </div>
    // `;
    return el;
  }
}
