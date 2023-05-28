import React from 'react';

import ReactDOM from 'react-dom/client';
import { BrowserRouter, createBrowserRouter } from 'react-router-dom';
import { RouterProvider } from 'react-router-dom';
import { Route } from 'react-router-dom';
import { Routes } from 'react-router-dom';

import './index.css';
import App from './App';
import 'bootstrap/dist/css/bootstrap.min.css';

import Profile from './components/profile/Profile';

{/*
const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    children: [
      {
        path: "#profile",
        element: <Profile />
      },
    ],
  },
]);
*/}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>
);