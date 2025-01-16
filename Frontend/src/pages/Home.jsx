// Home.js
import React from 'react';
import Hero from '../components/homepage/Hero'; // Ensure paths are correct based on your folder structure
import Intro from '../components/homepage/Intro/Intro'; // Ensure paths are correct based on your folder structure


const Home = () => {
  return (
    <div className="min-h-screen bg-gray-100">
      <Hero />
      <Intro />
    </div>
  );
};

export default Home;
