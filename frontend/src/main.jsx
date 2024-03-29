import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import ContactApp from './ContactApp.jsx'; // Updated import
import './index.css';
import './ContactApp.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route index element={<ContactApp />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);
