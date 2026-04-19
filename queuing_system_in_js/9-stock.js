import express from 'express';
import redis from "redis";
import { promisify } from 'util';

// Création de la liste des produits
const listProducts = [
    {id: 1, name: 'Suitcase 250', price: 50, stock: 4},
    {id: 2, name: 'Suitcase 450', price: 100, stock: 10},
    {id: 3, name: 'Suitcase 650', price: 350, stock: 2},
    {id: 4, name: 'Suitcase 1050', price: 550, stock: 5},
];

// Création de l'instance express et du port
const app = express();
const port = 1245;

const client = redis.createClient();

client.on("error", (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`)
})

const getAsync = promisify(client.get).bind(client);


// fonction getItemById
function getItemById(id)
{
    return listProducts.find((product) => product.id === id);
}


// Route GET /list_products
app.get('/list_products', (req, res) => {
    res.status(200).json(listProducts.map((product) => {
        return {
            itemId: product.id,
            itemName: product.name,
            price: product.price,
            initialAvailableQuantity: product.stock
        };
    }));
})

// Route GET /list_products/:itemId
app.get('/list_products/:itemId([0-9]+)', async (req, res) => {
    // Récupération de l'id pour récupérer le produit
    const reqId = parseInt(req.params.itemId, 10);
    const product = getItemById(reqId);
    if (!product) {
        return res.status(404).json({"status":"Product not found"});
    }

    // Récupération du stock
    const reservedStock = await getCurrentReservedStockById(reqId);
    const currentQuantity = product.stock - reservedStock;
    res.status(200).json({
            itemId: product.id,
            itemName: product.name,
            price: product.price,
            initialAvailableQuantity: product.stock,
            currentQuantity: currentQuantity
        });
})

// Route GET /reserve_product/:itemId
app.get('/reserve_product/:itemId([0-9]+)', async (req, res) => {
    // Récupération de l'id pour récupérer le produit
    const reqId = parseInt(req.params.itemId, 10);
    const product = getItemById(reqId);
    if (!product) {
        return res.status(404).json({"status":"Product not found"});
    }

    // Récupération du stock
    const currentReservedStock = await getCurrentReservedStockById(reqId);
    const currentQuantity = product.stock - currentReservedStock;
    if (currentQuantity < 1) {
        return res.status(404).json({"status":"Not enough stock available","itemId":reqId});
    }

    // Réservation de l'item
    const newReservedStock = currentReservedStock + 1;
    reserveStockById(reqId, newReservedStock);
    res.status(200).json({"status":"Reservation confirmed","itemId":reqId});
})


// Initialisation du serveur
const server = app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});


function reserveStockById(itemId, stock)
{
    client.set(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
    const value = await getAsync(`item.${itemId}`);
    if (value === null) {
        return 0;
    }
    return parseInt(value, 10);
}


module.exports = server;