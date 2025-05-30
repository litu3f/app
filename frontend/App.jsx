import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [file, setFile] = useState(null);
  const [downloadUrl, setDownloadUrl] = useState("");

  const handleUpload = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("file", file);
    const response = await axios.post('https://your-runpod-url:8000/remove-background/', formData);
    setDownloadUrl(response.data.download_url);
  };

  return (
    <div className="p-8 text-center">
      <h1 className="text-3xl font-bold mb-4">AI Background Remover</h1>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} className="mb-4" />
      <button onClick={handleUpload} className="bg-blue-500 text-white px-4 py-2 rounded">Upload</button>
      {downloadUrl && (
        <div className="mt-4">
          <a href={downloadUrl} className="text-green-500 underline">Download Processed Image</a>
        </div>
      )}
    </div>
  );
}

export default App;
