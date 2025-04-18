import { useState } from "react";
import ReactMarkdown from "react-markdown";
import styles from "./ChatBox.module.css"; // Keep your custom styles

export default function ChatBox() {
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [isMinimized, setIsMinimized] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError("");

    try {
      const res = await fetch("http://localhost:3000/chatbot", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: question }),
      });

      if (!res.ok) throw new Error("Something went wrong");

      const data = await res.json();
      setResponse(data.response);
    } catch (err) {
      setError("Failed to fetch response.");
    } finally {
      setLoading(false);
      setQuestion("");
    }
  };

  const toggleMinimize = () => {
    setIsMinimized(!isMinimized);
  };

  return (
    <div className={`${styles.chatboxContainer} ${isMinimized ? styles.minimized : ""}`}>
      {/* Header */}
      <div className={styles.header}>
        {!isMinimized && (
          <button className={styles.minimizeButton} onClick={toggleMinimize}>
            -
          </button>
        )}
      </div>

      {!isMinimized && (
        <div className={styles.headerBar}>
          Bloom Assist Chatbot
        </div>
      )}

      {isMinimized && (
        <div className={styles.minimizedContent}>
          <button className={styles.bloomAssistButton} onClick={toggleMinimize}>
            Bloom Assist
          </button>
        </div>
      )}

      {/* Chat Content */}
      {!isMinimized && (
        <div className={styles.chatContent}>
          {response && (
            <div className={styles.response}>
              <ReactMarkdown
                components={{
                  a: ({ node, ...props }) => (
                    <a {...props} target="_blank" rel="noopener noreferrer" />
                  )
                }}
              >
                {response}
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
            placeholder="Ask a question..."
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            required
          />
          <button className={styles.button} type="submit">Send</button>
        </form>
      )}
    </div>
  );
}


