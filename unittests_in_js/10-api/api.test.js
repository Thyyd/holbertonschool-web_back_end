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

describe('cart page', function () {
    it('Test GET "/cart/:id" route return the expected message when :is is a number', function (done) {
        request.get('http://localhost:7865/cart/750', (error, response, body) => {
            expect(error).to.equal(null);
            expect(response.statusCode).to.equal(200);
            expect(body).to.equal('Payment methods for cart 750');
            done();
        });
    });

    it("Test GET '/cart/:id' route returns an error if :id isn't a number", function (done) {
        request.get('http://localhost:7865/cart/albaz', (error, response, body) => {
            expect(error).to.equal(null);
            expect(response.statusCode).to.equal(404);
            expect(body).to.contain('Cannot GET /cart/albaz');
            done();
        });
    });

    it("Test GET '/cart/:id' route returns an error if :id isn't only a number", function (done) {
        request.get('http://localhost:7865/cart/iru666', (error, response, body) => {
            expect(error).to.equal(null);
            expect(response.statusCode).to.equal(404);
            expect(body).to.contain('Cannot GET /cart/iru666');
            done();
        });
    });
})

describe('available_payments page', function () {
    it('Test API returns status 200 and the right object', function (done) {
        request.get('http://localhost:7865/available_payments', (error, response, body) => {
            expect(error).to.equal(null);
            expect(response.statusCode).to.equal(200);
            const JSON_body = JSON.parse(body);
            expect(JSON_body).to.deep.equal({payment_methods: {credit_cards: true, paypal: false}});
            done();
        });
    });
})

describe('login page', function () {
    it('Test API returns status 200 and the right message', function (done) {
        request.post({url: 'http://localhost:7865/login', json: { userName: 'Albaz' }}, (error, response, body) => {
            expect(error).to.equal(null);
            expect(response.statusCode).to.equal(200);
            expect(body).to.equal('Welcome Albaz');
            done();
        });
    });
})