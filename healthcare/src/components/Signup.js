import React, { useState } from "react";
import { useNavigate, Link } from "react-router-dom";  // Add Link here for routing
import "./../styles/Signup.css";

const Signup = ({ userType }) => {
  // Define the state variables for email, password, confirmPassword, age, and gender
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [age, setAge] = useState("");  // Define state for age
  const [gender, setGender] = useState("");  // Define state for gender
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();

    // Validate password match
    if (password !== confirmPassword) {
      alert("Passwords do not match");
      return;
    }

    // Simulate successful signup and redirect to login page
    console.log(`${userType} Sign Up details:`, { email, password, age, gender });

    // Navigate to the appropriate login page based on userType
    if (userType === "Patient") {
      navigate("/patient/login");
    } else if (userType === "Doctor") {
      navigate("/doctor/login");
    }
  };

  return (
    <div className="signup-container">
      <h2>{userType} Sign Up</h2>
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
        <div>
          <label>Confirm Password:</label>
          <input
            type="password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            required
            placeholder="Confirm your password"
          />
        </div>
        <div>
          <label>Age:</label>
          <input
            type="number"
            value={age}
            onChange={(e) => setAge(e.target.value)}
            required
            placeholder="Enter your age"
          />
        </div>
        <div>
          <label>Gender:</label>
          <select
            value={gender}
            onChange={(e) => setGender(e.target.value)}
            required
          >
            <option value="">Select your gender</option>
            <option value="Male">Male</option>
            <option value="Female">Female</option>
            <option value="Other">Other</option>
            <option value="Prefer not to say">Prefer not to say</option>
          </select>
        </div>

        <button type="submit">Sign Up</button>
      </form>

      <div className="login-link">
        <p>
          Already have an account?{" "}
          <Link to={userType === "Patient" ? "/patient/login" : "/doctor/login"}>
            Login here
          </Link>
        </p>
      </div>
    </div>
  );
};

export default Signup;
