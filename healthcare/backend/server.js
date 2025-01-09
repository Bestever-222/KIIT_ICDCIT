const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const authRoutes = require('./routes/auth'); // Assuming the routes are in 'routes/auth.js'

const app = express();

// Middleware to parse incoming JSON data
app.use(bodyParser.json());

// Use the '/api/auth' prefix for the auth routes
app.use('/api/auth', authRoutes); // This maps the routes from 'auth.js' to '/api/auth'

// MongoDB connection (example)
mongoose.connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB Atlas'))
  .catch(err => console.log('MongoDB connection error:', err));

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

const cors = require('cors');
app.use(cors()); // Allow all origins
// Or specify a specific frontend URL like:
// app.use(cors({ origin: 'http://localhost:3000' }));
