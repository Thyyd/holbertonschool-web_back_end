const expect = require('chai').expect;
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', function () {
    it('Tests a Promise for Async function test : Returns an object when success is true', function (done) {
        getPaymentTokenFromAPI(true).then((response) => {
            // utilisation de deep.equal parce que je compare un objet complet, et pas que sa data
            expect(response).to.deep.equal({ data: 'Successful response from the API' });
            done();
        })
        // Si jamais le test échoue, le catch permet d'éviter un comportement inatendu
        .catch(done);
    });
    it('Tests a Promise for Async function test : Returns undefined when success is false', function () {
        expect(getPaymentTokenFromAPI(false)).to.be.undefined;
    });
});