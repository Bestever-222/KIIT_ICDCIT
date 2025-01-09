import React from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import LandingPage from "./components/LandingPage";
import Login from "./components/Login";
import Signup from "./components/Signup";
import PatientProfile from "./components/PatientProfile";
import DoctorProfile from "./components/DoctorProfile";

const App = () => {
  const isAuthenticated = localStorage.getItem("doctorLoggedIn"); // Check if doctor is logged in

  return (
    <Router>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/patient/login" element={<Login userType="Patient" />} />
        <Route path="/patient/signup" element={<Signup userType="" />} />
        <Route path="/patient/profile" element={<PatientProfile />} />
        <Route path="/doctor/login" element={<Login userType="Doctor" />} />
        <Route path="/doctor/profile" element={isAuthenticated ? <DoctorProfile /> : <Navigate to="/doctor/login" />} />
      </Routes>
    </Router>
  );
};

export default App;
