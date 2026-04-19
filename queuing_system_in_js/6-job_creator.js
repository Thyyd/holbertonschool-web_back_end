import kue from "kue";

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '3141592654',
  message: '2750 is the code to verify your acount',
}

const job = queue.create('push_notification_code', jobData);

job.on("failed", () => {
    console.log(`Notification job failed`)
})

job.on("complete", () => {
    console.log(`Notification job completed`)
})

job.save((err) => {
    if (err) {
        console.log(err);
        return;
    }
    else {
        console.log(`Notification job created: ${job.id}`)
    }
})
