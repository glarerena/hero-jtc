import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  // ✅ Enable CORS so your frontend can access this backend
  app.enableCors();

  await app.listen(3005);

}
bootstrap();
