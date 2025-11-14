import { Injectable } from "@nestjs/common";
import { CreatePostDto } from "./dto/create-post.dto";
import { PrismaService } from "./database/prisma.service";

@Injectable()
export class AppService {
  constructor(private readonly prisma: PrismaService) {}

  async save({ user, text }: CreatePostDto) {
    return await this.prisma.post.create({ data: { user, text } });
  }

  async find() {
    return await this.prisma.post.findMany({ orderBy: { id: "desc" } });
  }
}
