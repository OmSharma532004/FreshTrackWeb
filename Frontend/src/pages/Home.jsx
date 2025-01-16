// Home.js
import React from 'react';
import { Link } from 'react-router-dom'; 

const Home = () => {
  return (
    <div className="min-h-screen bg-gray-100">
     HomePage
     <Link to="/auth/login">
            <button>Register / Sign In</button>
     </Link>
    </div>
  );
};

export default Home;
