import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  app.enableCors({
    origin: [
      'http://localhost:3000',                    // local dev
      'https://hero-app.vercel.app',              // Vercel preview
      'https://first-hero.dev'          // ✅ Replace with your real domain when ready
    ],
    methods: 'GET,POST,OPTIONS',
    credentials: true
  });

  await app.listen(3005);
}
bootstrap();
