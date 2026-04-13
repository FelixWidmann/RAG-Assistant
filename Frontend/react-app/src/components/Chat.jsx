import { useState } from "react";

export default function ChatComponent({
  selectedCollection
}) {

  const [messages, setMessages] = useState([]);
  const [question, setQuestion] = useState("");

  const sendMessage = async () => {


    if (!question) return;

    const userMessage = {
      role: "user",
      text: question
    };

    setQuestion(""); 

    setMessages(prev => [...prev, userMessage]);

    try {

      const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";
      
      console.log(selectedCollection)

      const response = await fetch(`${API_URL}/ask`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ "question": userMessage.text, "collection": selectedCollection })
      });

      const data = await response.json();

      const assistantMessage = {
        role: "assistant",
        text: data.answer
      };

      setMessages(prev => [...prev, assistantMessage]);

    } catch (error) {

      setMessages(prev => [
        ...prev,
        { role: "assistant", text: "Error contacting backend." }
      ]);
      
    }

    setQuestion("");

  };

  return (
    <div className="chat-container">
  
      <div className="chat-messages">
        {messages.map((msg, index) => (
          <div key={index} className="chat-message">
            <b>
              {msg.role === "user" ? "You" : "Assistant"}:
            </b>
            <div>{msg.text}</div>
          </div>
        ))}
      </div>
  
      <div className="chat-input-area">
        <input
          type="text"
          value={question}
          placeholder="Ask a question..."
          onChange={(e) => setQuestion(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") sendMessage();
          }}
          className="chat-input"
        />
  
        <button onClick={sendMessage} className="chat-send">
          Send
        </button>
      </div>
  
    </div>
  );

}