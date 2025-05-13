import { Injectable } from '@nestjs/common';
import axios from 'axios';

interface Message {
  role: 'user' | 'assistant';
  content: string;
}

@Injectable()
export class ChatbotService {
  async forwardToPython(message: string, history: Message[] = []) {
    const lower = message.toLowerCase();
    console.log("🟡 Incoming message:", lower);
    console.log("📜 Conversation history:", history);

    const disclaimer =
      "\n\n⚠️ *This chatbot is an experimental tool. Please verify all information with official housing resources before making decisions.*";

    // Only show disclaimer in first message
    const shouldShowDisclaimer = history.length === 0;

    // 🔒 Static Responses
    if (lower.includes('hello') || lower.includes('hi')) {
      console.log("💬 Matched static greeting");
      return {
        response: "👋 Hello! I'm Bloom Assist — your guide to affordable housing listings in the Bay Area." + (shouldShowDisclaimer ? disclaimer : ""),
      };
    }

    if (lower.includes('what do you do') || lower.includes('your job')) {
      console.log("💬 Matched static explanation");
      return {
        response: "🏡 I help you find available housing listings by connecting directly to Bloom Housing's system." + (shouldShowDisclaimer ? disclaimer : ""),
      };
    }

    if (lower.includes('bye')) {
      console.log("💬 Matched static goodbye");
      return {
        response: "👋 Thanks for stopping by!\n\n🔗 [Visit Bloom Housing](https://housingbayarea.org/)" + (shouldShowDisclaimer ? disclaimer : ""),
      };
    }

    if (lower.includes('thanks') || lower.includes('thank you')) {
      console.log("💬 Matched static thanks");
      return {
        response: "😊 You're very welcome! Let me know if you have any more housing questions." + (shouldShowDisclaimer ? disclaimer : ""),
      };
    }

    // 🧠 Fallback to FastAPI listing microservice
    console.log("📡 Forwarding to Python API...");

    try {
      const response = await axios.post(
        process.env.PYTHON_API_URL || 'http://localhost:8000/generate',
        { 
          message,
          history // Pass conversation history to Python service
        }
      );

      console.log("✅ Response from Python API:", response.data);

      // Only append disclaimer to first message
      return {
        response: response.data.response + (shouldShowDisclaimer ? disclaimer : ""),
      };
    } catch (error) {
      console.error("❌ Error calling Python API:", error.message);

      return {
        response: "Sorry, I couldn't reach the housing database. Please try again later." + (shouldShowDisclaimer ? disclaimer : ""),
      };
    }
  }
}


