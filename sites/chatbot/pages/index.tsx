import { useState } from "react";
import ChatBox from "../components/ChatBox";

export default function Home() {
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

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
    }
  };

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial" }}>
      <h1>RAG Chatbot</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Ask a question..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          required
          style={{ padding: "0.5rem", width: "300px", marginRight: "1rem" }}
        />
        <button type="submit" style={{ padding: "0.5rem 1rem" }}>
          Send
        </button>
      </form>

      {loading && <p>Loading...</p>}
      {error && <p style={{ color: "red" }}>{error}</p>}
      {response && <ChatBox response={response} />}
    </div>
  );
}

