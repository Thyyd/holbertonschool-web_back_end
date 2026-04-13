const express = require('express')

// Création de l'instance express et du port
const app = express();
const port = 7865;

app.use(express.json());

// Route GET /
app.get('/', (req, res) => {
    res.status(200).send('Welcome to the payment system');
})

// Route GET /cart/:id
app.get('/cart/:id([0-9]+)', (req, res) => {
    res.status(200).send(`Payment methods for cart ${req.params.id}`);
})

// Route GET /available_payments
app.get('/available_payments', (req, res) => {
    res.status(200).json({payment_methods: {credit_cards: true, paypal: false}});
})

// Route POST /login
app.post('/login', (req, res) => {
    res.status(200).send(`Welcome ${req.body.userName}`);
})

// Initialisation du serveur
const server = app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});

module.exports = server;