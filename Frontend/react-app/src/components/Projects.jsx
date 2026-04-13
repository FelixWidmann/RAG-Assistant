import { useState, useEffect } from "react";

export default function HandleProjects({

    selectedCollection,
    setSelectedCollection,

}) {

  const [collections, setCollections] = useState([]);
  const [status, setStatus] = useState("");

  useEffect(() => {
    fetchCollections();
  }, []);

  //clean status after 3 seconds. 
  useEffect(() => {
    if (!status) return;
  
    const timer = setTimeout(() => {
      setStatus("");
    }, 3000);
  
    return () => clearTimeout(timer);
  }, [status]);

  const fetchCollections = async () => {
    try {
      const API_URL =
        import.meta.env.VITE_API_URL || "http://localhost:8000";

      const response = await fetch(`${API_URL}/collections`, {
        method: "GET",
      });

      if (response.ok) {
        const data = await response.json();
        setCollections(data);
        setSelectedCollection(prev => prev || data[0]); //only select default if nothing selected yet
      } else {
        setStatus("List Projects failed.");
      }
    } catch (error) {
      console.error(error);
      setStatus("Error listing Projects");
    }
  };

  const handleSubmit = async (e) => {
    
    e.preventDefault();

    // Read the form data
    const form = e.target;
    const formData = new FormData(form);

    // You can pass formData as a fetch body directly:
    try {
        const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";
    
        const response = await fetch(`${API_URL}/addcollection`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
          },
        body: JSON.stringify({ "name": formData.get("name") })
        });
          if (response.ok) {
            setStatus("Successfully created")
            fetchCollections(); 
            setSelectedCollection(formData.get("name"));
            form.reset();              // clear input
          } else {
            setStatus("Creation failed.");
          }
        } catch (error) {
          console.error(error);
          setStatus("Error creating Projects");
        }
      };
    

    const handleDelete = async(col) => {

        try{
        const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";
    
        const response = await fetch(`${API_URL}/deletecollection`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
          },
        body: JSON.stringify({ "name": col })
        });
          if (response.ok) {
            setStatus("Successfully deleted")
            fetchCollections(); 
          } else {
            setStatus("Deletion failed.");
          }
        } catch (error) {
          console.error(error);
          setStatus("Error deleting Projects");
        }

        };

  return (
        <div className="sidebar">
          <h2>Projects</h2>
          <hr></hr>
      
          {collections.length === 0 && <p>No collections found</p>}
      
          <div className="project-list">
            {collections.map((col) => (
              <div
                key={col}
                className={`project-item ${selectedCollection === col ? "selected" : ""}`} //checks if current col is selected and assigns correct css class accordingly
                onClick={() => setSelectedCollection(col)}
              >
                <span className="project-name">{col}</span>
            
                <button
                  className="project-delete"
                  onClick={(e) => {
                    e.stopPropagation();
                    handleDelete(col);
                  }}
                >
                  −
                </button>
              </div>
            ))}
          </div>
      
          <hr />
      
          <form className="project-form" onSubmit={handleSubmit}>
            <input name="name" placeholder="New Project..." />
            <button type="submit">+</button>
          </form>
      
          {status && <p>{status}</p>}
        </div>
      );
}



