import React, { useState } from "react";
import { v4 as uuidv4 } from "uuid";
import "./../styles/PatientProfile.css";

const PatientProfile = () => {
  // State for biodata
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

  // State for medical reports
  const [medicalReports, setMedicalReports] = useState([]);

  // State for medications
  const [medications, setMedications] = useState([]);

  // State for last consulted doctor
  const [lastDoctor, setLastDoctor] = useState({
    name: "Dr. Smith",
    contact: "123-456-7890",
  });

  // State for AI diagnostics
  const [aiDiagnostics, setAiDiagnostics] = useState([]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setBiodata((prev) => ({ ...prev, [name]: value }));
  };

  const handleReportUpload = (e) => {
    const file = e.target.files[0];
    if (file) {
      const newReport = {
        id: uuidv4(),
        name: file.name,
        date: new Date().toLocaleDateString(),
      };
      setMedicalReports((prev) => [...prev, newReport]);
    }
  };

  const handleMedicationUpdate = (index, key, value) => {
    const updatedMedications = medications.map((med, i) =>
      i === index ? { ...med, [key]: value } : med
    );
    setMedications(updatedMedications);
  };

  const analyzeReports = () => {
    // Placeholder for AI logic
    const diagnostics = [
      "No anomalies detected in the last report.",
      "Slight irregularity in blood pressure levels.",
    ];
    setAiDiagnostics(diagnostics);
  };

  return (
    <div className="patient-profile">
      <h2>Patient Profile</h2>

      {/* Unique User ID */}
      <div className="section">
        <h3>Unique User ID</h3>
        <p>{biodata.userId}</p>
      </div>

      {/* Bio Data */}
      <div className="section">
        <h3>Bio Data</h3>
        <form>
          {Object.keys(biodata).map(
            (key) =>
              key !== "userId" && (
                <div key={key}>
                  <label>{key.replace(/([A-Z])/g, " $1")}:</label>
                  <input
                    type="text"
                    name={key}
                    value={biodata[key]}
                    onChange={handleInputChange}
                  />
                </div>
              )
          )}
        </form>
      </div>

      {/* Medical Reports Section */}
      <div className="section">
        <h3>Medical Reports</h3>
        <input type="file" onChange={handleReportUpload} />
        <ul>
          {medicalReports.map((report) => (
            <li key={report.id}>
              {report.name} (Uploaded on: {report.date})
              <button onClick={() => alert(`Viewing: ${report.name}`)}>
                View
              </button>
              <button onClick={() => alert(`Downloading: ${report.name}`)}>
                Download
              </button>
            </li>
          ))}
        </ul>
      </div>

      {/* Medication Section */}
      <div className="section">
        <h3>Medications</h3>
        {medications.length === 0 && (
          <button onClick={() => setMedications([{ name: "", dosage: "" }])}>
            Add Medication
          </button>
        )}
        {medications.map((med, index) => (
          <div key={index} className="medication">
            <input
              type="text"
              placeholder="Medication Name"
              value={med.name}
              onChange={(e) =>
                handleMedicationUpdate(index, "name", e.target.value)
              }
            />
            <input
              type="text"
              placeholder="Dosage"
              value={med.dosage}
              onChange={(e) =>
                handleMedicationUpdate(index, "dosage", e.target.value)
              }
            />
          </div>
        ))}
      </div>

      {/* Last Consulted Doctor */}
      <div className="section">
        <h3>Last Consulted Doctor</h3>
        <p>Name: {lastDoctor.name}</p>
        <p>Contact: {lastDoctor.contact}</p>
      </div>

      {/* AI Diagnostics */}
      <div className="section">
        <h3>AI Diagnostics</h3>
        <button onClick={analyzeReports}>Analyze Reports</button>
        <ul>
          {aiDiagnostics.map((diag, index) => (
            <li key={index}>{diag}</li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default PatientProfile;
