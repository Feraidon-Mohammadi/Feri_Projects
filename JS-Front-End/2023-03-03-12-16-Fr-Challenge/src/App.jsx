import React from "react";
import ReactDOM from "react-dom/client";
import Header from "./components/Header.jsx";
import Content from "./components/Content.jsx";
import Footer from "./components/Footer.jsx";
import "./App.css";

export default function App() {
  return (
    <>
      <Header />
      <Content />
      <Footer />
    </>
  );
}
