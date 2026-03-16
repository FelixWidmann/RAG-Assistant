import { useState } from "react";

export default function ChatComponent() {

  const [messages, setMessages] = useState([]);
  const [question, setQuestion] = useState("");

  const sendMessage = async () => {

    if (!question) return;

    const userMessage = {
      role: "user",
      text: question
    };

    setMessages(prev => [...prev, userMessage]);

    try {

      const response = await fetch("http://localhost:8000/ask", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ question })
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

    <div>

      <h2>Chat</h2>

      <div style={{
        border: "1px solid #ccc",
        height: "500px",
        width: "500px",
        overflowY: "auto",
        padding: "10px",
        marginBottom: "10px"
      }}>

        {messages.map((msg, index) => (

          <div key={index} style={{ marginBottom: "10px" }}>

            <b>{msg.role === "user" ? "You" : "Assistant"}:</b>
            <div>{msg.text}</div>

          </div>

        ))}

      </div>

      <input
        type="text"
        value={question}
        placeholder="Ask a question..."
        onChange={(e) => setQuestion(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter") sendMessage();
        }}
        style={{ width: "70%", padding: "8px" }}
      />

      <button
        onClick={sendMessage}
        style={{ padding: "8px", marginLeft: "10px" }}
      >
        Send
      </button>

    </div>

  );

}