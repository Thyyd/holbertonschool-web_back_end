const expect = require('chai').expect;
const request = require('request');

describe('Index page', function () {
    it('Test API returns status 200', function (done) {
        request.get('http://localhost:7865', (error, response) => {
            expect(error).to.equal(null);
            expect(response.statusCode).to.equal(200);
            done();
        });
    });

    it('Test GET route return the expected message', function (done) {
        request.get('http://localhost:7865', (error, response, body) => {
            expect(error).to.equal(null);
            expect(response.statusCode).to.equal(200);
            expect(body).to.equal('Welcome to the payment system');
            done();
        });
    });
})