import { Module } from '@nestjs/common';
import { ChatbotController } from './chatbot/chatbot.controller';
import { ChatbotService } from './chatbot/chatbot.service';

@Module({
  controllers: [ChatbotController],
  providers: [ChatbotService],
})
export class AppModule {}

