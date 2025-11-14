/**
 * Патерн Factory Method (Фабричний метод)
 *
 * Клас BlockFactory відповідає за створення різних типів блоків резюме
 * залежно від типу, переданого як параметр.
 */

import {
  ResumeModel,
  Education,
  Experience,
  Skills,
} from "../models/ResumeModel";
import { HeaderBlock } from "./HeaderBlock";
import { SummaryBlock } from "./SummaryBlock";
import { ExperienceBlock } from "./ExperienceBlock";
import { EducationBlock } from "./EducationBlock";
import { SkillsBlock } from "./SkillsBlock";

export interface IBlock {
  render(): HTMLElement;
}

export type BlockType =
  | "header"
  | "summary"
  | "experience"
  | "education"
  | "skills";

export class BlockFactory {
  /**
   * Метод для створення блоку відповідного типу
   *
   * @param type Тип блоку для створення
   * @param model Дані моделі для цього блоку
   * @returns Створений блок, готовий для рендерингу
   *
   * TODO: Реалізуйте метод createBlock, який створює і повертає
   * відповідний блок залежно від типу, використовуючи патерн Factory Method.
   */
  createBlock(type: BlockType, model: ResumeModel): IBlock {
    // TODO: Реалізуйте логіку створення відповідного об'єкта IBlock
    switch (type) {
      case "header":
        // TODO: Поверніть новий HeaderBlock з відповідними даними
        return new HeaderBlock(model.header);
      case "summary":
        // TODO: Поверніть новий SummaryBlock з відповідними даними
        return new SummaryBlock(model.summary);
      case "experience":
        // TODO: Поверніть новий ExperienceBlock з відповідними даними
        // return new ExperienceBlock(model.experience[0]);
        return new ExperienceBlock(model.experience);
      case "education":
        // TODO: Поверніть новий EducationBlock з відповідними даними
        // return new EducationBlock(model.education[0]);
        return new EducationBlock(model.education);
      case "skills":
        // TODO: Поверніть новий SkillsBlock з відповідними даними
        return new SkillsBlock(model.skills);
      default:
        throw new Error(`Unknown block type: ${type}`);
    }
  }
}
