const expect = require('chai').expect;
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi', function () {
    let consoleSpy

    beforeEach(function () {
        consoleSpy = sinon.spy(console, 'log');
    });

    afterEach(function () {
        consoleSpy.restore();
    });

    it('Uses a hook to see if the console logs 120 for 100 and 20 as parameters', function () {
        sendPaymentRequestToApi(100, 20);

        expect(consoleSpy.calledOnceWithExactly('The total is: 120')).to.be.true;
        // expect(consoleSpy.calledOnce).to.be.true;
    });
    it('Uses a hook to see if the console logs 20 for 10 and 10 as parameters', function () {
        sendPaymentRequestToApi(10, 10);

        expect(consoleSpy.calledOnceWithExactly('The total is: 20')).to.be.true;
        // expect(consoleSpy.calledOnce).to.be.true;
    });
});
