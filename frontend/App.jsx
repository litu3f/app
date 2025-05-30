import React from 'react';
import HeroSection from './components/HeroSection';
import UploadSection from './components/UploadSection';
import PreviewSection from './components/PreviewSection';
import ProToolsSection from './components/ProToolsSection';

function App() {
  return (
    <div className="min-h-screen bg-gray-100">
      <HeroSection />
      <UploadSection />
      <PreviewSection />
      <ProToolsSection />
    </div>
  );
}

export default App;
