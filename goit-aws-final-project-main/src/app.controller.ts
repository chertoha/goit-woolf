import { Body, Controller, Get, Post } from "@nestjs/common";
import { AppService } from "./app.service";
import { CreatePostDto } from "./dto/create-post.dto";

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Post("posts")
  async save(@Body() createPostDto: CreatePostDto) {
    return await this.appService.save(createPostDto);
  }

  @Get("posts")
  async find() {
    return await this.appService.find();
  }
}
