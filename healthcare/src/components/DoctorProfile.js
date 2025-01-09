import React from "react";
import "./../styles/DoctorProfile.css";

const DoctorProfile = () => {
  return (
    <div className="doctor-profile">
      <h2>Doctor Profile</h2>

      {/* Search for Patient */}
      <div className="search-section">
        <input type="text" placeholder="Enter Patient ID" />
        <button>Search</button>
      </div>

      {/* Patient Profile Access */}
      <div className="patient-profile-section">
        <h3>Patient Profile: John Doe</h3>

        <div className="medications-section">
          <h4>Current Medications</h4>
          <ul>
            <li>Med1 - 10mg</li>
            <li>Med2 - 20mg</li>
          </ul>
        </div>

        <div className="reports-section">
          <h4>Uploaded Medical Reports</h4>
          <ul>
            <li>BloodTest1.pdf (Uploaded on: 2025-01-01)</li>
            <li>XRay1.pdf (Uploaded on: 2025-01-05)</li>
          </ul>
        </div>

        <div className="upload-report-section">
          <h4>Upload New Reports</h4>
          <input type="file" />
        </div>
      </div>
    </div>
  );
};

export default DoctorProfile;
