// services/authService.js
export const login = async ({ email, password }) => {
    try {
      const response = await fetch('http://localhost:5000/api/auth/Login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
      });
  
      if (!response.ok) {
        throw new Error(`Error: ${response.statusText}`);
      }
  
      return await response.json();
    } catch (error) {
      console.error('Login failed:', error);
      throw error; // Re-throw error to be handled in the calling component
    }
  };
  
  // Add the signup function
  export const signup = async ({ email, password, age, gender, userType }) => {
    try {
      const response = await fetch('http://localhost:5000/api/auth/Signup', {  // Changed to 'Signup' (capitalized)
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password, age, gender, userType }),
      });
  
      if (!response.ok) {
        throw new Error(`Error: ${response.statusText}`);
      }
  
      return await response.json();
    } catch (error) {
      console.error('Signup failed:', error);
      throw error; // Re-throw error to be handled in the calling component
    }
  };
  