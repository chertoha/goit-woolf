import { NestFactory } from "@nestjs/core";
import { AppModule } from "./app.module";
import { ValidationPipe } from "@nestjs/common";
import { NestExpressApplication } from "@nestjs/platform-express";
import { join } from "node:path";

async function bootstrap() {
  const app = await NestFactory.create<NestExpressApplication>(AppModule);

  app.enableCors({
    origin: "*",
  });

  app.useStaticAssets(join(__dirname, "..", "public"));

  app.useGlobalPipes(
    new ValidationPipe({ whitelist: true, forbidNonWhitelisted: true, transform: true })
  );

  const PORT = process.env.PORT ?? 9999;

  await app.listen(PORT, () => console.log(`\x1b[34mServer started on port = ${PORT}`));
}
bootstrap();
