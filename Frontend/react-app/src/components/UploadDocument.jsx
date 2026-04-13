import { useState, useEffect } from "react";

export default function UploadDocumentComponent({
  selectedCollection
}) {
  
  const [status, setStatus] = useState("");

    //clean status after 3 seconds. 
    useEffect(() => {
      if (!status) return;
    
      const timer = setTimeout(() => {
        setStatus("");
      }, 3000);
    
      return () => clearTimeout(timer);
    }, [status]);
  

  const handleFileSelect = async (event) => {
    
    event.preventDefault();
    
    const file = event.target.files[0];
    if (!file) return;

    setStatus(`Uploading ... `); //${file.name} ...`);

    const formData = new FormData();
    formData.append("file", file);
    formData.append("collection", selectedCollection);

    try {
      const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

      const response = await fetch(`${API_URL}/upload`, {
        method: "POST",
        body: formData
      });

      if (response.ok) {
        const data = await response.json();
        setStatus(`Successfully \n uploaded  `); //file: ${data.filename} (${data.status})`);
      } else {
        setStatus("Upload failed.");
      }
    } catch (error) {
      console.error(error);
      setStatus("Error Upload failed.");
    }
  };
  return (
    <div className="upload-container">
  
      {/* Hidden file input */}
      <input
        type="file"
        id="fileInput"
        className="upload-input-hidden"
        onChange={handleFileSelect}
      />
  
      {/* Upload button */}
      <label htmlFor="fileInput" className="upload-button">
        Upload
      </label>
  
      {/* Status message */}
      {status && (
        <div className="upload-status">
          {status}
        </div>
      )}
  
    </div>
  );
}
