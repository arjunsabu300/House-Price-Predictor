
import React, { useState } from 'react';
import axios from 'axios';
import { motion } from "framer-motion";

function Building() {
  const [formData, setFormData] = useState({
    bedrooms: "",
    bathrooms: "",
    living_area: "",
    lot_area: "",
    floors: "",
    waterfront: "",
    views: "",
    condition: "",
    grade: "",
    area_excluding_basement: "",
    basement_area: "",
    built_year: "",
    renovation_year: "",
    postal_code: "",
    latitude: "",
    longitude: "",
    living_area_renov: "",
    lot_area_renov: "",
    nearby_schools: "",
    distance_airport: "",
  });

  const [price, setPrice] = useState(0);
  const [showResult, setShowResult] = useState(false);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: parseFloat(e.target.value) });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/predict', formData);
      console.log(response.data.price)
      setPrice(response.data.price);
      setShowResult(true); 
    } catch (error) {
      console.error('Prediction error:', error);
      alert('Prediction failed. Try again.');
    }
  };
  const formatIndianCurrency = (price) => {
    return new Intl.NumberFormat('en-IN').format(price);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-100 via-blue-100 to-cyan-100 flex items-center justify-center p-6">
      <motion.div
        initial={{ opacity: 0, y: -30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8 }}
        className="bg-white p-10 rounded-3xl shadow-2xl w-full max-w-4xl"
      >
        <motion.h1
          initial={{ scale: 0.8, opacity: 0 }}
          animate={{ scale: 1, opacity: 1 }}
          transition={{ delay: 0.2, duration: 0.5 }}
          className="text-4xl font-bold text-center text-indigo-700 mb-10"
        >
          🏡 Building Price Predictor
        </motion.h1>

        <form
          onSubmit={handleSubmit}
          className="grid grid-cols-1 sm:grid-cols-2 gap-6 place-items-center"
        >
          {Object.keys(formData).map((key, idx) => (
            <motion.div
              key={key}
              className="w-full flex flex-col items-center"
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.05 * idx }}
            >
              <label className="text-sm font-semibold text-gray-600 mb-2 text-center capitalize">
                {key.replace(/_/g, " ")}
              </label>
              <input
                type="number"
                name={key}
                value={formData[key]}
                onChange={handleChange}
                className="w-4/5 px-4 py-2 text-gray-800 bg-gray-100 border border-gray-300 rounded-xl shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-400"
                required
              />
            </motion.div>
          ))}

          <motion.div
            className="col-span-2 mt-8"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 1.2 }}
          >
            <button
              type="submit"
              className="bg-indigo-600 hover:bg-indigo-700 text-white font-bold px-10 py-3 rounded-xl shadow-md transition transform hover:scale-105 duration-300"
            >
              🔍 Predict Price
            </button>
          </motion.div>
        </form>

        {showResult && (
          <motion.div
            className="text-center mt-10 text-2xl font-semibold text-green-700"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.3 }}
          >
            💰 Predicted Price: ₹{formatIndianCurrency(price)}
          </motion.div>
        )}
      </motion.div>
    </div>
  );
}

export default Building;

