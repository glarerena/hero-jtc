import { Injectable } from '@nestjs/common';
import axios from 'axios';

@Injectable()
export class ChatbotService {
  async forwardToPython(message: string) {
    const lower = message.toLowerCase();

    // 🔒 Static Responses
    if (lower.includes('hello') || lower.includes('hi')) {
      return {
        response: "👋 Hello! I'm Bloom Assist — your guide to affordable housing listings in the Bay Area.",
      };
    }

    if (lower.includes('what') && lower.includes('do')) {
      return {
        response: "🏡 I help you find available housing listings by connecting directly to Bloom Housing's system.",
      };
    }

    if (lower.includes('bye') || lower.includes('thanks')) {
      return {
        response:
          "👋 Thanks for stopping by!\n\n🔗 [Visit Bloom Housing](https://housingbayarea.org/)",
      };
    }

    // 🧠 Always send everything else to your existing FastAPI listings endpoint
    const response = await axios.post(
      process.env.PYTHON_API_URL || 'http://localhost:8000/generate',
      { message }
    );

    return response.data;
  }
}

