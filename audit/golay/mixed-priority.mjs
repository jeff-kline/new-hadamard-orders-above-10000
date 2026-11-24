// Bounded arithmetic only. Run: node mixed-priority.mjs
const limit = 12000;
const primes = [2, 3, 5, 11, 13];
function complexGolay(n) {
  let rest = n;
  const powers = primes.map(prime => {
    let count = 0;
    while (rest % prime === 0) {
      rest /= prime;
      count++;
    }
    return count;
  });
  const [a, b, c, d, e] = powers;
  return rest === 1 && b + c + d + e <= a + Math.min(c + e, a) + 1;
}
const S = new Set([0]);
for (let n = 1; n <= limit; n++) if (complexGolay(n)) S.add(n);
function multiply(A, B, scale = 1) {
  const out = new Set();
  for (const a of A) for (const b of B) {
    const x = scale * a * b;
    if (x <= limit) out.add(x);
  }
  return out;
}
function sums(A, B, scale = 1) {
  const out = new Set();
  for (const a of A) for (const b of B) {
    const x = scale * (a + b);
    if (x <= limit) out.add(x);
  }
  return out;
}
const join = (...sets) => new Set(sets.flatMap(s => Array.from(s)));
const B = new Set([1]);
for (let j = 1; j <= 43; j++) B.add(2*j+1);
for (const j of S) if (2*j+1 <= limit) B.add(2*j+1);
const products = multiply(S, S);
let E = join(B, multiply(S, B, 2), sums(products, products, 2));
let F;
for (;;) {
  F = multiply(E, E);
  const expanded = join(E, multiply(S, F, 4));
  if (expanded.size === E.size) break;
  E = expanded;
}
const dense = join(F, multiply(S, B), multiply(S, sums(S, S)));
// Du & Jiang Corollary 4 permits scaling a quad by {2, 10, 26}S.
const scales = multiply([2, 10, 26], S);
for (const x of dense) for (const a of scales) if (a*x <= limit) dense.add(a*x);
const real = new Set();
for (let a = 1; a <= limit; a *= 2) {
  for (let b = a; b <= limit; b *= 10) {
    for (let c = b; c <= limit; c *= 26) real.add(c);
  }
}
const dgs = multiply([7, 9, 15], real);
const mixed = sums(dgs, S);
const oldDihedral = sums(dgs, real);
const oldComplex = sums(S, S);
for (const p of [599,719,1319,1439,1579,1783,1979,1987,2207,2251,2287,2339,2371,2399,2543,2671,2677,2687,2699,2903,2939,1567,2683,2879,2887,2995,1499,2999]) {
  const exponents = [3,4,5].filter(k => (p * 2**k)/8 <= limit);
  const hits = (set, divisor) => exponents.filter(k => set.has(p*2**k/divisor)).join(',') || '-';
  console.log(p, 'mixed(16)', hits(mixed,16), 'KK(8)', hits(oldDihedral,8), 'CHK(8)', hits(oldComplex,8), 'DJ(8)', hits(dense,8));
}
