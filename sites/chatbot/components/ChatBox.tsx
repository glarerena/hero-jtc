import styles from "./ChatBox.module.css";

type Props = {
  response: string;
};

export default function ChatBox({ response }: Props) {
  return (
    <div className={styles.chatbox}>
      <h2>Chatbot Response</h2>
      <pre>{response}</pre>
    </div>
  );
}
