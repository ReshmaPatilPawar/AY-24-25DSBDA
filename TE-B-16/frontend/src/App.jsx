import React, { useEffect } from 'react';
import Navbar from './Navbar.jsx';
import Footer from './Footer.jsx';
import './App.css';
import {
    BrowserRouter,
    Routes,
    Route,
} from "react-router-dom";
import Predict from './components/Predict.jsx';
import Home from './pages/Home.jsx';
import About from './components/About.jsx';
import ArticlesPage from './components/ArticlesPage.jsx';
import GoodThoughts from './pages/GoodThoughts.jsx';


function App() {
  useEffect(() => {
    window.watsonAssistantChatOptions = {
      integrationID: "468bb670-777b-42e0-90e5-09540d6da062",
      region: "au-syd",
      serviceInstanceID: "a81b5e4b-2cb1-4991-87ac-009ac65c7e7c",
      onLoad: async (instance) => { await instance.render(); }
    };
    setTimeout(() => {
      const t = document.createElement('script');
      t.src = "https://web-chat.global.assistant.watson.appdomain.cloud/versions/" + 
              (window.watsonAssistantChatOptions.clientVersion || 'latest') + 
              "/WatsonAssistantChatEntry.js";
      document.head.appendChild(t);
    });
  }, []);

  return (
    <BrowserRouter>
    
    <div className="h-screen">
      <Navbar />
      <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/predict" element={<Predict />} />
      <Route path="/about" element={<About />} />
      <Route path="/articles" element={<ArticlesPage />} />
      <Route path="/thoughts" element={<GoodThoughts />} />
    </Routes>
      <Footer />
    </div>
   
      </BrowserRouter>
  );
}

export default App;
