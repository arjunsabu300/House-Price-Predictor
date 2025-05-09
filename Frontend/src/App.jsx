import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Building from "./buildingweb";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Building/>} />
      </Routes>
    </Router>
  );
}

export default App;
