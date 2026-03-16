import ChatComponent from "./components/Chat";
import UploadDocumentComponent from "./components/UploadDocument";

function App() {

  return (
    <div style={{ padding: "30px" }}>

      <h1>RAG Study Assistant</h1>

      <div
        style={{
          display: "flex",
          gap: "100px",
          alignItems: "flex-start"
        }}
      >

        {/* Upload panel */}
        <div>
          <UploadDocumentComponent />
        </div>

        {/* Chat panel */}
        <div>
          <ChatComponent />
        </div>

      </div>

    </div>
  );

}

export default App;