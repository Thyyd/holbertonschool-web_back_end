import redis from "redis";

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

// Fonction displaySchoolValue
function displaySchoolValue(schoolName)
{
    client.get(schoolName, function(err, value) {
        if (err) {
            console.log(err);
            return;
        }
        console.log(value);
    })
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
