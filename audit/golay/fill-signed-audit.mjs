import fs from 'node:fs';
const orders = fs.readFileSync(new URL('claude-fill.tsv',import.meta.url),'utf8').trim().split('\n').slice(1).map(row=>Number(row.split('\t')[0]));
function divisors(n){
  const result=[];
  for(let i=1;i*i<=n;i++)if(n%i===0){
    result.push(i);
    if(i*i!==n)result.push(n/i);
  }
  return result.sort((a,b)=>a-b);
}
function odd(n){while(n%2===0)n/=2;return n;}
const cap=Math.max(...orders)/4;
const spans=new Map([[0,0],[1,1]]);
// A pair of aligned length 23 and weight 29 can always be disjoined
// by placing one word in even positions and the other in odd positions.
for(const [g,d] of [[2,2],[5,6],[10,10],[13,14],[17,21],[26,26],[29,46]]){
  for(const [w,l] of [...spans])if(w)
    for(let v=w*g,s=l*d;v<=cap;v*=g,s*=d)
      spans.set(v,Math.min(spans.get(v)??Infinity,s));
}
const weights=[...spans.keys()].sort((a,b)=>a-b);

function admissible(m){return m<=2||m%4===0;}
function seedUpper(m){return divisors(m).filter(h=>m!==2||h!==2);}
function primal(n){return n>=2&&divisors(n).length===2;}
function had(n){return n===1||n===2||n%4===0&&(n<=1000||primal(n-1)||had(n/2));}
function seedKnown(m,h){
  if(h===1)return had(m);
  if(h===m&&Number.isInteger(Math.sqrt(m)))return had(Math.sqrt(m));
  if(h===2&&m===4)return true;
  // Corollary 16(2), k=2.
  if(h===2&&m%4===0&&divisors(m/4).some(a=>had(2*a)&&had(2*(m/4/a))))return true;
  // Corollary 16(3), k=2.
  if(h===2&&m%8===0&&divisors(m/8).some(a=>had(4*a)&&had(4*(m/8/a))))return true;
  return false;
}
for(const D of orders){
  const packed=new Set(), actual=new Set(), unconstrained=new Set();
  for(let H=D;H%4===0;H/=2)for(const M of divisors(H/4).filter(admissible))
  for(const N of divisors(H/(4*M)).filter(admissible)){
    if(odd(M)===odd(D)||odd(N)===odd(D))continue;
    const L=H/(4*M*N);
    for(const h of seedUpper(M))for(const k of seedUpper(N)){
      const counts=new Set([1,h,k,h*k]);
      if(h%2===0&&k%2===0)counts.add(h*k/4);
      const label=[H,M,N,h,k,L].join('/');
      // For an upper screen include repeated choices and omission of an arm.
      // For positive hits distinct OS from the actual source must be justified.
      for(const t of counts){
        for(const a of [0,...counts])for(const b of [0,...counts]){
          const w=(L-a-b)/t;
          if(!spans.has(w))continue;
          unconstrained.add([M,N].join('/'));
          if(t*spans.get(w)>L)continue;
          packed.add(label);
          if(seedKnown(M,h)&&seedKnown(N,k))actual.add(label);
        }
        for(const s of counts)for(const w of weights){
          if(t*w>L)break;
          const v=(L-t*w)/s;
          if(!spans.has(v))continue;
          unconstrained.add([M,N].join('/'));
          if(t*spans.get(w)+s*spans.get(v)>L)continue;
          packed.add(label);
          if(seedKnown(M,h)&&seedKnown(N,k))actual.add(label);
        }
      }
    }
  }
  const lengths=[...new Set([...packed].map(row=>Number(row.split("/")[5])))].sort((a,b)=>a-b);
  console.log(D,"packed lengths",lengths.join(","), 'packed tuples',packed.size,'seed-supported tuples',actual.size, [...actual].join(' '));
  if(D===125360)console.log('125360 arithmetic seed sizes', [...unconstrained].join(' '), 'packed seed sizes',[...new Set([...packed].map(row=>row.split('/').slice(1,3).join('/')))].join(' '));
}
