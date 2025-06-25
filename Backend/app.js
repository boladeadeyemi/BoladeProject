const express = require('express');
const cors = require('cors');

const app = express();
app.use(cors());

const groupMembers = [
  'Bolade', 'Felix', 'Idowu', 'James', 'Agape', 'Oyerinde',
  'John', 'Folashade', 'Ifeoluwa', 'Paul', 'Peter', 'Peace',
  'Esther', 'Covenant', 'Hassan', 'Ingrid'
];

app.get('/api/groupmembers', (req, res) => {
  res.json({ groupMembers });
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Backend running on http://localhost:${PORT}`);
});
