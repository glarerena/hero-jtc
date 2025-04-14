import { useState } from "react";
import styles from './ChatBox.module.css'; // Adjust the path as needed


export default function ChatBox() {
 const [question, setQuestion] = useState("");
 const [response, setResponse] = useState("");
 const [loading, setLoading] = useState(false);
 const [error, setError] = useState("");
 const [isMinimized, setIsMinimized] = useState(false); // State to track if the box is minimized


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
     setQuestion(""); // Clear input after submit
   }
 };


 const toggleMinimize = () => {
   setIsMinimized(!isMinimized); // Toggle between minimized and maximized states
 };


 return (
   <div
     className={`${styles.chatboxContainer} ${isMinimized ? styles.minimized : ""}`} // Add minimized class dynamically
   >
     {/* Header - only show the minimize button when not minimized */}
     <div className={styles.header}>
       {!isMinimized && (
         <button className={styles.minimizeButton} onClick={toggleMinimize}>
           -
         </button>
       )}
     </div>
    {/* Header Title */}
    {!isMinimized && (
      <div className={styles.headerBar}>
        Bloom Assist Chatbot
      </div>
    )}

     {/* Minimized content */}
     {isMinimized && (
       <div className={styles.minimizedContent}>
         <button
           className={styles.bloomAssistButton}
           onClick={toggleMinimize} // Toggle maximize/minimize on button click
         >
           Bloom Assist
         </button>
       </div>
     )}


     {/* Chatbox content (only visible when not minimized) */}
     {!isMinimized && (
       <div className={styles.chatContent}>
         {response && <div className={styles.response}>{response}</div>}
         {loading && <p className={styles.loading}>Loading...</p>}
         {error && <p className={styles.error}>{error}</p>}
       </div>
     )}


     {/* Input form */}
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


