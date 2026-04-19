import redis from "redis";
import { promisify } from 'util';

const client = redis.createClient();

client.on("error", (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`)
})

client.on("connect", () => {
    console.log(`Redis client connected to the server`)
})

// Fonction setNewSchool
function setNewSchool(schoolName, value)
{
    client.set(schoolName, value, redis.print);
}

// Création du promisify de client.get en le liant à client.
const getAsync = promisify(client.get).bind(client);

// Fonction displaySchoolValue
async function displaySchoolValue(schoolName)
{
    try {
        const value = await getAsync(schoolName);
        console.log(value);
    }
    catch (error) {
        console.log(error);
    }
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
