// Reproduce the positive historical witnesses. Only 38 targets and scalar inputs.
import {readFileSync} from 'node:fs';
import assert from 'node:assert/strict';

function prime(n) {
  if (!Number.isInteger(n) || n < 2) return false;
  for (let p = 2; p*p <= n; p++) if (n % p === 0) return false;
  return true;
}

// A prime p = 3 mod 4 gives a symmetric equivalent of Paley H(p+1).
// The second and third inputs also use the symmetric Sylvester H(2) or H(4).
const symmetricInputs = new Map([
  [8444, [8443]],
  [11360, [19, 283]],
  [14048, [3511]]
]);
assert.equal(2 * (19+1) * (283+1), 11360);
assert.equal(4 * (3511+1), 14048);
for (const primes of symmetricInputs.values())
  assert(primes.every(p => p % 4 === 3 && prime(p)));

const data = readFileSync(new URL('claude-fill.tsv', import.meta.url),'utf8');
const targets = data.trim().split('\n').slice(1).map(line => line.split('\t').map(Number));
assert.equal(targets.length, 38);
let earlier = 0;
console.log('order\todd_part\tpriority\tsource_or_scope\tverified_parameters');
for (const [order, oddPart] of targets) {
  let source, witness;
  const q = (oddPart-1)/2;
  const input = (q-1)/2;
  if (prime(q) && q % 4 === 1 && symmetricInputs.has(input) && order === 16*(2*q+1)) {
    source = 'Seberry-Yamada 1990, Corollaries 29(ii) and 40; doubling';
    witness = 'q=' + q + ', symmetric H(' + input + '), earlier H(' + order/2 + ')';
  }
  for (let t=1;t<=71;t+=2) {
    if (order % (4*t) !== 0) continue;
    const s = order/(4*t), Q = 4*s-1;
    if (!prime(Q)) continue;
    source = 'Balonin-Djokovic Prop. 8; Xia et al. Thm. 4; Finlayson-Seberry Thm. 4';
    witness = 'Q=' + Q + ', s=' + s + ', t=' + t;
  }
  if (source) earlier++;
  else {
    source = 'No prior witness found; no verified publication declaring this target open';
    witness = (order === 125360) ? 'Older H(250720)=8*(3840+27500)' : '';
  }
  console.log([order, oddPart, source.startsWith('No prior')?'unresolved':'previously constructible', source, witness].join('\t'));
}
assert.equal(earlier,9);
