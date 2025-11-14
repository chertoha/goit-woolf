import { IsString } from "class-validator";

export class CreatePostDto {
  @IsString()
  user: string;

  @IsString()
  text: string;
}
