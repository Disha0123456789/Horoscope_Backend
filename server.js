const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const { spawn } = require('child_process');

const app = express();
const PORT = 5000;

app.use(cors());
app.use(bodyParser.json());

app.post('/api/run-script', (req, res) => {
    const { scriptName, args } = req.body;

    console.log(`Running script: ${scriptName} with args: ${args}`);

    const pythonProcess = spawn('python', [`scripts/${scriptName}`, ...args]);

    let scriptOutput = '';
    pythonProcess.stdout.on('data', (data) => {
        scriptOutput += data.toString();
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error(`Error from Python script: ${data}`);
    });

    pythonProcess.on('close', (code) => {
        if (code === 0) {
            try {
                const jsonResponse = JSON.parse(scriptOutput);
                res.json(jsonResponse);
            } catch (error) {
                console.error('Failed to parse Python script output:', error);
                res.status(500).json({ error: 'Failed to parse Python script output.' });
            }
        } else {
            console.error(`Python script exited with code ${code}`);
            res.status(500).json({ error: `Python script exited with code ${code}` });
        }
    });

    pythonProcess.on('error', (error) => {
        console.error('Failed to start Python process:', error);
        res.status(500).json({ error: 'Failed to start Python process.' });
    });
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
