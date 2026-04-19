import kue from "kue";

export default function createPushNotificationsJobs(jobs, queue)
{
    if (!Array.isArray(jobs)) {
        throw new Error("Jobs is not an array");
    }
    jobs.forEach(jobData => {
        const job = queue.create('push_notification_code_3', jobData);

        job.on("progress", (progress, data) => {
            console.log(`Notification job ${job.id} ${progress}% complete`);
        })

        job.on("failed", (err) => {
            console.log(`Notification job ${job.id} failed: ${err}`);
        })

        job.on("complete", () => {
            console.log(`Notification job ${job.id} completed`);
        })

        job.save((err) => {
            if (err) {
                console.log(err);
                return;
            }
            console.log(`Notification job created: ${job.id}`);
        })
    });
}