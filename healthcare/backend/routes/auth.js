const express = require('express');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const User = require('../models/User'); // Assuming you have a User model
const dotenv = require('dotenv');

dotenv.config();

const router = express.Router();

// Signup Route
router.post('/signup', async (req, res) => {
  const { username, email, password } = req.body;
  try {
    const existingUser = await User.findOne({ email });
    if (existingUser) {
      return res.status(400).json({ message: 'User already exists' });
    }

    const newUser = new User({ username, email, password });
    await newUser.save();
    res.status(201).json({ message: 'User created successfully' });
  } catch (err) {
    res.status(500).json({ message: 'Server error' });
  }
});

router.post('/login', async (req, res) => {
    const { email, password } = req.body;
  
    try {
      console.log('Login request received for email:', email); // Log the incoming request
  
      // Step 1: Find user by email
      const user = await User.findOne({ email });
      if (!user) {
        console.log('User not found'); // Log if user is not found
        return res.status(400).json({ message: 'User not found' });
      }
  
      console.log('User found:', user); // Log the found user
  
      // Step 2: Compare the password
      const isMatch = await user.comparePassword(password);
      if (!isMatch) {
        console.log('Invalid password'); // Log if password does not match
        return res.status(400).json({ message: 'Invalid credentials' });
      }
  
      console.log('Password matched'); // Log if password matches
  
      // Step 3: Send the response (No token, just success message)
      res.status(200).json({ message: 'Login successful' });
    } catch (err) {
      console.error('Error during login:', err); // Log any errors
      res.status(500).json({ message: 'Server error', error: err.message });
    }
  });
  
  
  
module.exports = router;
