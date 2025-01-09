import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./../styles/Login.css";

const Login = ({ userType }) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(`${userType} Login details:`, { email, password });

    // Simulate a login check
    if (userType === "Doctor" && email === "doctor@example.com" && password === "password") {
      localStorage.setItem("doctorLoggedIn", "true"); // Set login flag
      navigate("/doctor/profile");
    } else if (userType === "Patient" && email === "patient@example.com" && password === "password") {
      navigate("/patient/profile");
    } else {
      alert("Invalid login credentials");
    }
  };

  return (
    <div className="login-container">
      <h2>{userType} Login</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Email:</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Password:</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit">Login</button>
      </form>
    </div>
  );
};

export default Login;
