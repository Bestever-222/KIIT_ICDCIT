import React from "react";
import { useNavigate } from "react-router-dom";
import "./../styles/LandingPage.css";

const LandingPage = () => {
  const navigate = useNavigate();

  return (
    <div className="landing-page">
      <h1>Welcome to Our Platform</h1>
      <p>Choose an option to proceed:</p>
      <div className="button-container">
        <button onClick={() => navigate("/doctor/login")} className="doctor-btn">
          I am a Doctor
        </button>
        <button onClick={() => navigate("/patient/login")} className="patient-btn">
          I am a Patient
        </button>
      </div>
    </div>
  );
};

export default LandingPage;
