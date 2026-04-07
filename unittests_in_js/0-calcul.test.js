const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function () {
  it('should return 5 when inputs are 2 and 3.0', function () {
    assert.strictEqual(calculateNumber(2, 3.0), 5);
  });
  it('should return 7 when inputs are 1.2 and 6.4', function () {
    assert.strictEqual(calculateNumber(1.2, 6.4), 7);
  });
  it('should return 10 when inputs are 2.5 and 7.2', function () {
    assert.strictEqual(calculateNumber(2.5, 7.2), 10);
  });
  it('should return 4 when inputs are 1.2 and 2.5', function () {
    assert.strictEqual(calculateNumber(1.2, 2.5), 4);
  });
  it('should return 7 when inputs are 1.49 and 6.49', function () {
    assert.strictEqual(calculateNumber(1.49, 6.49), 7);
  });
  it('should return 7 when inputs are 2.51 and 4.49', function () {
    assert.strictEqual(calculateNumber(2.51, 4.49), 7);
  });
  it('should return 5 when inputs are 2.5 and 2', function () {
    assert.strictEqual(calculateNumber(2.5, 2), 5);
  });
  it('should return 5 when inputs are 2.5 and 1.5', function () {
    assert.strictEqual(calculateNumber(2.5, 1.5), 5);
  });
  it('should return 25 when inputs are 17.4999 and 8.2', function () {
    assert.strictEqual(calculateNumber(17.4999, 8.2), 25);
  });

  it('should return -5 when inputs are -2 and -3', function () {
    assert.strictEqual(calculateNumber(-2, -3), -5);
  });
  it('should return -17 when inputs are -12.2 and -4.7', function () {
    assert.strictEqual(calculateNumber(-12.2, -4.7), -17);
  });
  it('should return -25 when inputs are -17.5 and -8.2', function () {
    assert.strictEqual(calculateNumber(-17.5, -8.2), -25);
  });
  it('should return -7 when inputs are -2.8 and -4.5', function () {
    assert.strictEqual(calculateNumber(-2.8, -4.5), -7);
  });
  it('should return -10 when inputs are -7.5 and -3.5', function () {
    assert.strictEqual(calculateNumber(-7.5, -3.5), -10);
  });
});