import redis from "redis";

const client = redis.createClient();

client.on("error", (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`)
})

client.on("connect", () => {
    console.log(`Redis client connected to the server`)
})

// 6 Appels hset explicites
client.hset("HolbertonSchools", 'Portland', '50', redis.print);
client.hset("HolbertonSchools", 'Seattle', '80', redis.print);
client.hset("HolbertonSchools", 'New York', '20', redis.print);
client.hset("HolbertonSchools", 'Bogota', '20', redis.print);
client.hset("HolbertonSchools", 'Cali', '40', redis.print);
client.hset("HolbertonSchools", 'Paris', '2', redis.print);

// variante utilisant un for
/*const values = {
  "Portland": "50",
  "Seattle": "80",
  "New York": "20",
  "Bogota": "20",
  "Cali": "40",
  "Paris": "2"
};

for (const city in values) {
    client.hset("HolbertonSchools", city, values[city], redis.print);
}

// Variante avec forEach
/*const values =[
  ["Portland", "50"],
  ["Seattle", "80"],
  ["New York", "20"],
  ["Bogota", "20"],
  ["Cali", "40"],
  ["Paris", "2"]
];

values.forEach(([city, value]) => {
    client.hset("HolbertonSchools", city, value, redis.print);
});*/

client.hgetall("HolbertonSchools", function(err, value) {
    if (err) {
        console.log(err);
        return;
    }
    console.log(value);
})