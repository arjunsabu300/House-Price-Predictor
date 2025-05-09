import express from 'express';
import cors from 'cors';  
import { spawn } from 'child_process';
import bodyParser from 'body-parser';

const app = express();
const port = 5000;
let Result;

app.use(cors());
app.use(bodyParser.json()); 


const pythonPath = 'C:/Users/arjun/AppData/Local/Programs/Python/Python39/python.exe';
const predictPrice = (data) => {
  return new Promise((resolve, reject) => {
    
    const pythonProcess = spawn(pythonPath, ['testing.py']);  

   
    pythonProcess.stdin.write(JSON.stringify(data) + '\n');
    pythonProcess.stdin.end();  

    pythonProcess.stdout.on('data', (data) => {
      const output = data.toString(); 
      console.log("Python Output:", output);
      try {
        const result = JSON.parse(data.toString());  
        console.log(result.predicted_price)
        Result=result.predicted_price;
        resolve(result.predicted_price);  
      } catch (error) {
        reject('Error parsing Python output');
      }
    });

    
    pythonProcess.stderr.on('data', (data) => {
      console.error('Python error:', data.toString());
      reject('Error executing Python script');
    });

    pythonProcess.on('close', (code) => {
      if (code !== 0) {
        reject(`Python process exited with code ${code}`);
      }
    });
  });
};


app.post('/predict', async (req, res) => {
  try {
    const data = req.body;  

    if (!data) {
      return res.status(400).json({ error: 'Missing input data' });
    }
    console.log(data);

    
    const predictedPrice = await predictPrice(data);
    console.log(predictPrice)
    console.log(Result);
    res.json({ price: Result });  
  } catch (error) {
    console.error('Prediction error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});


app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
