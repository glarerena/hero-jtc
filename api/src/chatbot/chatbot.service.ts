import { Injectable } from '@nestjs/common';
import axios from 'axios';

@Injectable()
export class ChatbotService {
  async forwardToPython(message: string) {
    const response = await axios.post(
      process.env.PYTHON_API_URL || 'http://localhost:8000/generate',
      { message }
    );
    return response.data;
  }
}
