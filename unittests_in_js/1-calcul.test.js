const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function () {
  it('should return 25 when inputs are SUM, 20 and 3', function () {
    assert.strictEqual(calculateNumber("SUM", 20, 5), 25);
  });
  it('should return -50 when inputs are SUM, -40 and -10', function () {
    assert.strictEqual(calculateNumber("SUM", -40, -10), -50);
  });
  it('should return 2 when inputs are SUM, 0.3 and 2', function () {
    assert.strictEqual(calculateNumber("SUM", 0.3, 2), 2);
  });
  it('should return 2 when inputs are SUM, 3.6 and -2', function () {
    assert.strictEqual(calculateNumber("SUM", 3.6, -2), 2);
  });
  it('should return 18 when inputs are SUM, 12 and 5.7', function () {
    assert.strictEqual(calculateNumber("SUM", 12, 5.7), 18);
  });
  it('should return -2 when inputs are SUM, -1 and -1.5', function () {
    assert.strictEqual(calculateNumber("SUM", -1, -1.5), -2);
  });
  it('should return 12 when inputs are SUM, 7.8 and 4.3', function () {
    assert.strictEqual(calculateNumber("SUM", 7.8, 4.3), 12);
  });
  it('should return 20 when inputs are SUM, 18.499 and 2', function () {
    assert.strictEqual(calculateNumber("SUM", 18.499, 2), 20);
  });
  it('should return 18 when inputs are SUM, 15 and 3.499', function () {
    assert.strictEqual(calculateNumber("SUM", 15, 3.499), 18);
  });
  it('should return 10 when inputs are SUM, 7.5 and 1.5', function () {
    assert.strictEqual(calculateNumber("SUM", 7.5, 1.5), 10);
  });
  it('should return 100 when inputs are SUM, 75.499 and 25.499', function () {
    assert.strictEqual(calculateNumber("SUM", 75.499, 25.499), 100);
  });
  it('should return 25 when inputs are SUM, 25 and 0.25', function () {
    assert.strictEqual(calculateNumber("SUM", 25, 0.25), 25);
  });


  it('should return 15 when inputs are SUBTRACT, 20 and 5', function () {
    assert.strictEqual(calculateNumber("SUBTRACT", 20, 5), 15);
  });
  it('should return -30 when inputs are SUBTRACT, -40 and -10', function () {
    assert.strictEqual(calculateNumber("SUBTRACT", -40, -10), -30);
  });
  it('should return -2 when inputs are SUBTRACT, 0.3 and 2', function () {
    assert.strictEqual(calculateNumber("SUBTRACT", 0.3, 2), -2);
  });
  it('should return 6 when inputs are SUBTRACT, 3.6 and -2', function () {
    assert.strictEqual(calculateNumber("SUBTRACT", 3.6, -2), 6);
  });
  it('should return 6 when inputs are SUBTRACT, 12 and 5.7', function () {
    assert.strictEqual(calculateNumber("SUBTRACT", 12, 5.7), 6);
  });
  it('should return 0 when inputs are SUBTRACT, -1 and -1.5', function () {
    assert.strictEqual(calculateNumber("SUBTRACT", -1, -1.5), 0);
  });
  it('should return 4 when inputs are SUBTRACT, 7.8 and 4.3', function () {
    assert.strictEqual(calculateNumber("SUBTRACT", 7.8, 4.3), 4);
  });
  it('should return 16 when inputs are SUBTRACT, 18.499 and 2', function () {
    assert.strictEqual(calculateNumber("SUBTRACT", 18.499, 2), 16);
  });
  it('should return 12 when inputs are SUBTRACT, 15 and 3.499', function () {
    assert.strictEqual(calculateNumber("SUBTRACT", 15, 3.499), 12);
  });
  it('should return 6 when inputs are SUBTRACT, 7.5 and 1.5', function () {
    assert.strictEqual(calculateNumber("SUBTRACT", 7.5, 1.5), 6);
  });
  it('should return 50 when inputs are SUBTRACT, 75.499 and 25.499', function () {
    assert.strictEqual(calculateNumber("SUBTRACT", 75.499, 25.499), 50);
  });
  it('should return 25 when inputs are SUBTRACT, 25 and 0.25', function () {
    assert.strictEqual(calculateNumber("SUBTRACT", 25, 0.25), 25);
  });


  it('should return 4 when inputs are DIVIDE, 20 and 5', function () {
    assert.strictEqual(calculateNumber("DIVIDE", 20, 5), 4);
  });
  it('should return 4 when inputs are DIVIDE, -40 and -10', function () {
    assert.strictEqual(calculateNumber("DIVIDE", -40, -10), 4);
  });
  it('should return 0 when inputs are DIVIDE, 0.3 and 2', function () {
    assert.strictEqual(calculateNumber("DIVIDE", 0.3, 2), 0);
  });
  it('should return -2 when inputs are DIVIDE, 3.6 and -2', function () {
    assert.strictEqual(calculateNumber("DIVIDE", 3.6, -2), -2);
  });
  it('should return 2 when inputs are DIVIDE, 12 and 5.7', function () {
    assert.strictEqual(calculateNumber("DIVIDE", 12, 5.7), 2);
  });
  it('should return 1 when inputs are DIVIDE, -1 and -1.5', function () {
    assert.strictEqual(calculateNumber("DIVIDE", -1, -1.5), 1);
  });
  it('should return 2 when inputs are DIVIDE, 7.8 and 4.3', function () {
    assert.strictEqual(calculateNumber("DIVIDE", 7.8, 4.3), 2);
  });
  it('should return 9 when inputs are DIVIDE, 18.499 and 2', function () {
    assert.strictEqual(calculateNumber("DIVIDE", 18.499, 2), 9);
  });
  it('should return 5 when inputs are DIVIDE, 15 and 3.499', function () {
    assert.strictEqual(calculateNumber("DIVIDE", 15, 3.499), 5);
  });
  it('should return 4 when inputs are DIVIDE, 7.5 and 1.5', function () {
    assert.strictEqual(calculateNumber("DIVIDE", 7.5, 1.5), 4);
  });
  it('should return 3 when inputs are DIVIDE, 75.499 and 25.499', function () {
    assert.strictEqual(calculateNumber("DIVIDE", 75.499, 25.499), 3);
  });
  it('should return "Error" when inputs are DIVIDE, 25 and 0.25', function () {
    assert.strictEqual(calculateNumber("DIVIDE", 25, 0.25), "Error");
  });
});