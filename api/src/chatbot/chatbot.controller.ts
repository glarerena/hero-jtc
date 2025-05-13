import { Controller, Post, Body } from '@nestjs/common';
import { ChatbotService } from './chatbot.service';

interface ChatRequest {
  message: string;
  history: Array<{
    role: 'user' | 'assistant';
    content: string;
  }>;
}

@Controller('chatbot')
export class ChatbotController {
  constructor(private readonly chatbotService: ChatbotService) {}

  @Post()
  async handleChat(@Body() request: ChatRequest) {
    return this.chatbotService.forwardToPython(request.message, request.history);
  }
}
