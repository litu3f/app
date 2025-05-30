import React, { useState } from 'react';
import axios from 'axios';

function UploadSection() {
  const [file, setFile] = useState(null);
  const [downloadUrl, setDownloadUrl] = useState("");

  const handleUpload = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("file", file);
    const response = await axios.post('https://your-backend-url.com/remove-background/', formData);
    setDownloadUrl(response.data.download_url);
  };

  return (
    <div className="text-center py-6">
      <input type="file" onChange={(e) => setFile(e.target.files[0])} className="mb-4" />
      <button onClick={handleUpload} className="bg-blue-500 text-white px-4 py-2 rounded">
        Upload & Process
      </button>
      {downloadUrl && <p className="mt-4"><a href={downloadUrl} className="text-green-600 underline">Download Result</a></p>}
    </div>
  );
}

export default UploadSection;
