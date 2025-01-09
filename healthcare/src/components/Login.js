import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { login } from "../services/authService"; // Import the login service
import "./../styles/Login.css";

const Login = ({ userType }) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Call the login service
      const response = await login({ email, password, userType });

      if (response.message === "Login successful") {
        // Store the user type locally and redirect based on it
        localStorage.setItem("userType", userType);

        if (userType === "Doctor") {
          navigate("/doctor/profile");
        } else if (userType === "Patient") {
          navigate("/patient/profile");
        }
      } else {
        setError("Invalid login credentials.");
      }
    } catch (err) {
      setError(err.message || "An error occurred during login.");
    }
  };

  return (
    <div className="login-container">
      <h2>{userType} Login</h2>
      {error && <p style={{ color: "red" }}>{error}</p>}
      <form onSubmit={handleSubmit}>
        <div>
          <label>Email:</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            placeholder="Enter your email"
          />
        </div>
        <div>
          <label>Password:</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            placeholder="Enter your password"
          />
        </div>
        <button type="submit">Login</button>
      </form>

      <div className="signup">
        <p>
          New user?{" "}
          <a href={userType === "Patient" ? "/patient/signup" : "/doctor/signup"}>
            Sign Up
          </a>
        </p>
      </div>
    </div>
  );
};

export default Login;
