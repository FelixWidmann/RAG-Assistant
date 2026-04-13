import { useState } from "react";

import ChatComponent from "./components/Chat";
import UploadDocumentComponent from "./components/UploadDocument";
import HandleProjects from "./components/Projects";


function App() {

  // pass down information of selected Project to Chat, Project and Upload Component
  const [selectedCollection, setSelectedCollection] = useState(null);

  return (

    <div style={{ flex: 1, display: "flex", flexDirection: "column", width: "100%", height: "100%", overflow: "hidden"}}>

      {/* Top headline */}
      <div style={{}}>
        <h1 style={{ margin: 20 }}>RAG Study Assistant</h1>
      </div>

      {/* Three-column layout below headline */}
      <div style={{flex: 1, display: "flex", flexDirection: "row",   minWidth: 0, overflow: "hidden"
      }}>

      {/* Left sidebar (small) */}
      <div style={{
        width: "15%",      
        padding: "20px",
        boxSizing: "border-box",
        flexShrink: 0,
        //backgroundColor: "#101015", //maybe darker background color for extra information on left sidebar
      }}>
        {/* Future features can go here */}
        <HandleProjects  selectedCollection={selectedCollection} setSelectedCollection={setSelectedCollection} style={{ flex: 1 }}/>
      </div>

      {/* Middle chat panel (large) */}
      <div style={{
        flex: 1,       
        display: "flex",
        flexDirection: "column",
        minWidth: 0, 
        boxSizing: "border-box"
      }}>
        <ChatComponent selectedCollection={selectedCollection} style={{ flex: 1 }} />
      </div>

      {/* Right sidebar (small) */}
      <div style={{
        width: "10%",
        display: "flex",
        justifyContent: "flex-start",
        alignContent:"center",
        flexShrink: 0,
        minWidth: 0,
        padding: "20px",
        boxSizing: "border-box"
      }}>
        <UploadDocumentComponent selectedCollection={selectedCollection} style={{ }} />
      </div>

      </div>

    </div>
  );
}

export default App;

