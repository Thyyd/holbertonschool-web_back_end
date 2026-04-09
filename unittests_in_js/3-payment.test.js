const expect = require('chai').expect;
const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', function () {
    it('Uses sendPaymentRequestToApi that calls Utils.calculateNumber with SUM and the provided parameters', function () {
        const utilsSpy = sinon.spy(Utils, 'calculateNumber')
        const consoleSpy = sinon.spy(console, 'log')

        sendPaymentRequestToApi(100, 20);

        expect(utilsSpy.calledWith('SUM', 100, 20)).to.be.true;
        expect(consoleSpy.calledWith('The total is: 120')).to.be.true;

        utilsSpy.restore();
        consoleSpy.restore();
    });
});
