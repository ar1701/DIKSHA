if(process.env.NODE_ENV != "production") {
    require("dotenv").config(); 
  }
  
  const cloudinary = require("cloudinary").v2;
  const express = require("express");
  const app = express();
  
  const mongoose = require("mongoose");
  const path = require("path");
  const axios = require('axios');
  const methodOverride = require("method-override");
  const ejsMate = require("ejs-mate");
  const User = require("./model/user.js");
  const Profile = require("./model/profile.js");
  
  const session = require("express-session");
  const bodyParser = require("body-parser");
  const MongoStore = require("connect-mongo");
  const LocalStrategy = require("passport-local");
  const passport = require("passport");
  const flash = require("connect-flash");
  const { isLoggedIn } = require("./middleware.js");
  const multer = require("multer");
  
  const dbUrl = process.env.ATLASDB_URL;
  // const { storage } = require("./cloudConfig.js");
  
  async function extractImage(url) {
    try {
        const response = await axios({
            method: 'GET',
            url: url,
            responseType: 'arraybuffer'
        });
        return response.data;
    } catch (error) {
        console.error('Error extracting image:', error);
        throw error;
    }
  }
  
  
  const storage = multer.diskStorage({
    destination: function (req, file, cb) {
        cb(null, 'uploads/');
    },
    filename: function (req, file, cb) {
        cb(null, file.originalname);
    }
  });
  
  const upload = multer({ storage });
  
  const store = MongoStore.create({
    mongoUrl: dbUrl,
    crypto: {
        secret: process.env.SECRET,
    },
    touchAfter: 24*60*60,
  });
  
  store.on("error", (error) => {
    console.log("Error in MONGO SESSION STORE: ", error);
  });
  
  const sessionOptions = {
    store,
    secret: process.env.SECRET,
    resave: false,
    saveUninitialized: true,
    cookie: {
        expires: Date.now() + 7 * 24 * 60 * 60 * 1000,
        maxAge: 7 * 24 * 60 * 60 * 1000,
        httpOnly: true,
    },
  };
  