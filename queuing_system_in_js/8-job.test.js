import createPushNotificationsJobs from './8-job.js'
import kue from "kue";
import { expect } from "chai";


describe('createPushNotificationsJobs', function() {
    const queue = kue.createQueue();

    // Initialisation du test
    before(function() {
        queue.testMode.enter();
    });
    // Nettoyage entre chaque test
    afterEach(function() {
        queue.testMode.clear();
    });
    // Fin du test
    after(function() {
        queue.testMode.exit();
    });

    it('Throws an error when jobs is not an array', function () {
        expect(() => {
            createPushNotificationsJobs("Albaz", queue);
        }).to.throw("Jobs is not an array");
    });

    it('Creates 3 new jobs to the queue', function () {
        const jobs = [
            {phoneNumber: '3141592654', message: '2750 is the code to verify your acount'},
            {phoneNumber: '4136201457', message: '4275 is the code to verify your acount'},
            {phoneNumber: '7502851475', message: '2583 is the code to verify your acount'}
        ]

        createPushNotificationsJobs(jobs, queue);
        expect(queue.testMode.jobs.length).to.equal(3);
        queue.testMode.jobs.forEach((job, index) => {
            expect(job.type).to.equal('push_notification_code_3');
            expect(job.data).to.deep.equal(jobs[index]);
        });
    });

    it("Doesn't create any new job to the queue", function () {
        const jobs = [];
        createPushNotificationsJobs(jobs, queue);
        expect(queue.testMode.jobs.length).to.equal(0);
    });
})