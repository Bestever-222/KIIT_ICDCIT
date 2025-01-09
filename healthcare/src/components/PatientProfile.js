import React, { useState } from "react";
import { v4 as uuidv4 } from "uuid";
import "./../styles/PatientProfile.css";

const PatientProfile = () => {
  const [biodata, setBiodata] = useState({
    userId: uuidv4(),
    name: "",
    parentsDetails: "",
    spouseDetails: "",
    age: "",
    bloodGroup: "",
    gender: "",
    phoneNumber: "",
    email: "",
  });

  const [medicalReports, setMedicalReports] = useState([]);
  const [medications, setMedications] = useState([]);
  const [lastDoctor, setLastDoctor] = useState({
    name: "Dr. Smith",
    contact: "123-456-7890",
  });

  const [aiDiagnostics, setAiDiagnostics] = useState([]);
  const [activeSection, setActiveSection] = useState("biodata");

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setBiodata((prev) => ({ ...prev, [name]: value }));
  };

  const handleReportUpload = (e) => {
    const file = e.target.files[0];
    if (file) {
      setMedicalReports((prev) => [
        ...prev,
        {
          id: uuidv4(),
          name: file.name,
          date: new Date().toLocaleDateString(),
        },
      ]);
    }
  };

  const handleMedicationUpdate = (index, key, value) => {
    const updatedMedications = medications.map((med, i) =>
      i === index ? { ...med, [key]: value } : med
    );
    setMedications(updatedMedications);
  };

  const addMedication = () => {
    setMedications((prev) => [...prev, { name: "" }]);
  };

  const analyzeReports = () => {
    const diagnostics = [
      "No anomalies detected in the last report.",
      "Slight irregularity in blood pressure levels.",
    ];
    setAiDiagnostics(diagnostics);
  };

  return (
    <div className="patient-profile">
      {/* Unique User ID */}
      <div className="unique-user-id">
        <p>User ID: {biodata.userId}</p>
      </div>

      {/* Navigation Bar */}
      <nav className="navbar">
        <ul>
          {["biodata", "medicalReports", "medications", "lastDoctor", "aiDiagnostics"].map((section) => (
            <li
              key={section}
              className={activeSection === section ? "active" : ""}
              onClick={() => setActiveSection(section)}
            >
              {section.replace(/([A-Z])/g, " $1").replace(/^./, (str) => str.toUpperCase())}
            </li>
          ))}
        </ul>
      </nav>

      {/* Content */}
      <div className="content">
        {activeSection === "biodata" && (
          <div className="section">
            <h3>Bio Data</h3>
            <form>
              {Object.keys(biodata).map(
                (key) =>
                  key !== "userId" && (
                    <div key={key} className="form-group">
                      <label>{key.replace(/([A-Z])/g, " $1").replace(/^./, (str) => str.toUpperCase())}</label>
                      <input
                        type="text"
                        name={key}
                        value={biodata[key]}
                        onChange={handleInputChange}
                        placeholder={`Enter ${key}`}
                      />
                    </div>
                  )
              )}
            </form>
          </div>
        )}
        {activeSection === "medicalReports" && (
          <div className="section">
            <h3>Medical Reports</h3>
            <input type="file" onChange={handleReportUpload} />
            {medicalReports.length ? (
              <ul>
                {medicalReports.map((report) => (
                  <li key={report.id}>
                    {report.name} (Uploaded on: {report.date})
                  </li>
                ))}
              </ul>
            ) : (
              <p>No reports uploaded yet.</p>
            )}
          </div>
        )}
        {activeSection === "medications" && (
          <div className="section">
            <h3>Medications</h3>
            {medications.length > 0 ? (
              medications.map((med, index) => (
                <div key={index} className="medication-item">
                  <input
                    type="text"
                    placeholder="Medication Name"
                    value={med.name}
                    onChange={(e) => handleMedicationUpdate(index, "name", e.target.value)}
                  />
                </div>
              ))
            ) : (
              <p>No medications added yet.</p>
            )}
            <button onClick={addMedication}>Add Medication</button>
          </div>
        )}
        {activeSection === "lastDoctor" && (
          <div className="section">
            <h3>Last Consulted Doctor</h3>
            <p>Name: {lastDoctor.name}</p>
            <p>Contact: {lastDoctor.contact}</p>
          </div>
        )}
        {activeSection === "aiDiagnostics" && (
          <div className="section">
            <h3>AI Diagnostics</h3>
            <button onClick={analyzeReports}>Analyze</button>
            {aiDiagnostics.length > 0 ? (
              <ul>
                {aiDiagnostics.map((diag, index) => (
                  <li key={index}>{diag}</li>
                ))}
              </ul>
            ) : (
              <p>No diagnostics available yet.</p>
            )}
          </div>
        )}
      </div>
    </div>
  );
};

export default PatientProfile;
