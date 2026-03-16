import { useState } from "react";

export default function UploadDocumentComponent() {

  const [file, setFile] = useState(null);
  const [status, setStatus] = useState("");

  const uploadFile = async () => {

    if (!file) {
      setStatus("Please select a file.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {

      const response = await fetch("http://localhost:8000/upload", {
        method: "POST",
        body: formData
      });

      if (response.ok) {
        const data = await response.json()
        const text = `Successfully uploaded file: ${data.filename} and ${data.status}`;
        setStatus(text);
      } else {
        setStatus("Upload failed.");
      }

    } catch (error) {
      setStatus("Error uploading file.");
    }

  };

  return (

    <div style={{ marginBottom: "30px" }}>

      <h2>Upload Document</h2>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button
        onClick={uploadFile}
        style={{ marginLeft: "10px", padding: "8px" }}
      >
        Upload
      </button>

      <div style={{ marginTop: "10px" }}>
        {status}
      </div>

    </div>

  );

}