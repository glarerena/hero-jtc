import { useState } from "react"
import ReactMarkdown from "react-markdown"
import styles from "./Chatbox.module.scss" // Keep your custom styles

interface Message {
  role: 'user' | 'assistant';
  content: string;
}

export default function ChatBox() {
  console.log("✅ Chatbox component is rendering...")
  const [question, setQuestion] = useState("")
  const [messages, setMessages] = useState<Message[]>([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState("")
  const [isMinimized, setIsMinimized] = useState(true)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    setError("")

    // Add user message to chat history
    const userMessage: Message = { role: 'user', content: question }
    const updatedMessages = [...messages, userMessage]
    setMessages(updatedMessages)

    try {
      const res = await fetch("http://localhost:3005/chatbot", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ 
          message: question,
          history: messages // Send conversation history
        }),
      })

      if (!res.ok) throw new Error("Something went wrong")

      const data = await res.json()
      
      // Add assistant response to chat history
      const assistantMessage: Message = { role: 'assistant', content: data.response }
      setMessages([...updatedMessages, assistantMessage])
    } catch {
      setError("Failed to fetch response.")
    } finally {
      setLoading(false)
      setQuestion("")
    }
  }

  const toggleMinimize = () => {
    if (isMinimized) {
      // Initialize chat with welcome message
      setMessages([{
        role: 'assistant',
        content: "👋 Hello! I'm Bloom Assist — your guide to affordable housing listings in the Bay Area.\n\n⚠️ *This chatbot is an experimental tool. Please verify all information with official housing resources before making decisions.*\n\nHow can I help you today?"
      }])
    }
    setIsMinimized(!isMinimized)
  }

  return (
    <div
      className={`${styles.chatboxContainer} ${isMinimized ? styles.minimized : styles.maximized}`}
    >
      {/* Header */}
      <div className={styles.header}>
        {!isMinimized && (
          <button className={styles.minimizeButton} onClick={toggleMinimize}>
            -
          </button>
        )}
      </div>

      {!isMinimized && <div className={styles.headerBar}>Bloom Assist Chatbot</div>}

      {isMinimized && (
        <div className={styles.minimizedContent}>
          <button className={styles.bloomAssistButton} onClick={toggleMinimize}>
            BLOOM ASSISTANT
          </button>
        </div>
      )}

      {/* Chat Content */}
      {!isMinimized && (
        <div className={styles.chatContent}>
          {messages.map((message, index) => (
            <div 
              key={index} 
              className={`${styles.message} ${message.role === 'user' ? styles.userMessage : styles.assistantMessage}`}
            >
              <ReactMarkdown
                components={{
                  a: (props) => (
                    <a {...props} target="_blank" rel="noopener noreferrer">
                      {props.children || "Link"}
                    </a>
                  ),
                }}
              >
                {message.content}
              </ReactMarkdown>
            </div>
          ))}
          {messages.length >= 10 && (
            <div className={`${styles.message} ${styles.assistantMessage}`}>
              <ReactMarkdown>
                {"I've reached my conversation limit. To continue, please click the minimize button (-) and then click 'BLOOM ASSISTANT' to start a new chat. Thank you for using Bloom Assist!"}
              </ReactMarkdown>
            </div>
          )}
          {loading && <p className={styles.loading}>Loading...</p>}
          {error && <p className={styles.error}>{error}</p>}
        </div>
      )}

      {/* Input */}
      {!isMinimized && (
        <form onSubmit={handleSubmit} className={styles.form}>
          <input
            className={styles.input}
            type="text"
            placeholder={messages.length >= 10 ? "Click minimize (-) to start over" : "Ask a question..."}
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            required
            disabled={messages.length >= 10}
          />
          <button 
            className={styles.button} 
            type="submit"
            disabled={messages.length >= 10}
          >
            Send
          </button>
        </form>
      )}
    </div>
  )
}

