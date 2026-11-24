// node family-million.mjs [--records] (the records are ordered by matrix order).
import {readFileSync} from 'node:fs';
import assert from 'node:assert/strict';
const limit = 1_000_000;
const qcap = limit/8;
const file = name => readFileSync(new URL(name, import.meta.url),'utf8');
const sorted = set => [...new Set(set)].sort((a,b)=>a-b);
const union = (...sets) => sorted(sets.flat());
function combine(a,b,operation,scale=1,cap=qcap) {
  const result = new Set();
  for (const x of a) for (const y of b) {
    const n = scale*(operation==='sum'?x+y:x*y);
    if (n>cap) break;
    result.add(n);
  }
  return sorted(result);
}
const times = (a,b,scale=1,cap=qcap) => combine(a,b,'product',scale,cap);
const plus = (a,b,scale=1,cap=qcap) => combine(a,b,'sum',scale,cap);
const B = [], C = [];
for (let n=1;n<=limit/4;n++) {
  let rem=n;
  const [a,b,c,d,e]=[2,3,5,11,13].map(p=>{
    let k=0;
    while(rem%p===0){rem/=p;k++;}
    return k;
  });
  if(rem===1 && !b && !d && c+e<=a) B.push(n);
  if(n<=qcap && rem===1 && b+c+d+e<=a+Math.min(a,c+e)+1) C.push(n);
}
const D=times([7,9,15],B);
const input=union(C,D);
const actual=new Map();
for(const a of input)for(const b of input) {
  const n=16*(a+b);
  if(n>limit)break;
  if(a<=b && !actual.has(n))actual.set(n,[a,b]);
}
const old=new Array(limit+1);
function mark(n,reason){if(n<=limit && !old[n])old[n]=reason;}
const certificates=JSON.parse(file('family-kumar-orders.json'));
for(const n of certificates.hadamard)mark(n,'Kumar ordinary certificate');
for(const n of certificates.symmetric)mark(n,'Kumar symmetric certificate');
const prime=new Uint8Array(limit+1).fill(1);
prime[0]=prime[1]=0;
for(let p=2;p*p<=limit;p++)if(prime[p])for(let i=p*p;i<=limit;i+=p)prime[i]=0;
const pp=new Uint8Array(prime);
for(let p=2;p*p<=limit;p++)if(prime[p])for(let i=p*p;i<=limit;i*=p)pp[i]=1;
mark(1,'trivial');mark(2,'trivial');
const open=new Set(file('family-table-kumar-open.txt').trim().split(/\s+/).map(Number));
const high=new Map();
for (const [e,list] of [[4,[599,719,1319,1439,1579,1783,1979,1987,2207,2251,2287,2339,2371,2399,2543,2671,2677,2687,2699,2903,2939]],[5,[1567,2683,2879,2887,2995]],[6,[1499,2999]]])
  for(const m of list)high.set(m,e);
// 2999's listed exponent six is not used as a certificate.
for(let m=3;m<=2999;m+=2){if(m!==2999)mark(m*2**(high.get(m)??(open.has(m)?3:2)),'Kumar frontier');}
for(let n=1;n<=limit;n*=2)mark(n,'Sylvester');
for(let q=3;q<=limit;q+=2)if(pp[q])mark(q%4===3?q+1:2*(q+1),'Paley');
const conf=new Set([2,66,86]);
for(let q=5;q<=limit;q+=4)if(pp[q])conf.add(q+1);
for(let q=3;2*(q*q*(q+2)+1)<=limit;q+=4)if(pp[q]&&pp[q+2])conf.add(q*q*(q+2)+1);
for(let x=45;2*(x+1)<=limit;x*=81)conf.add(x+1);
let sym=sorted([2,...certificates.symmetric,...[...conf].map(x=>2*x)].filter(n=>n<=limit));
for(;;){const next=union(sym,times(sym,sym,1,limit));if(next.length===sym.length)break;sym=next;}
for(const n of sym)mark(n,'symmetric construction or tensor product');
const symSet=new Set(sym);
for(let p=3;(p+1)**2<=limit;p+=2){
  if(pp[p]&&pp[p+2])mark((p+1)**2,'twin prime powers');
}
const skew=new Set([2,276,292,...certificates.skew]);
for(let i=1;4*i<250;i+=2)skew.add(4*i);
for(let q=3;q<=limit;q+=4)if(pp[q])skew.add(q+1);
for(let q=5;2*(q+1)<=limit;q+=8)if(pp[q])skew.add(2*(q+1));
for(let q=2;4*(1+q+q*q)<=limit;q++)if(pp[q]){
  const s=1+q+q*q;
  if((prime[s] && [3,5,7].includes(s%8)) || pp[2*q*q+2*q+3])skew.add(4*s);
}
for(const n of skew){mark(n,'skew');if(2*n<=limit)skew.add(2*n);}
const all=(max,start=1,step=1)=>Array.from({length:Math.floor((max-start)/step)+1},(_,i)=>start+i*step);
const tcap=limit/4;
const consecutive=union(all(87,1,2),B.map(x=>2*x+1)).filter(x=>x<=tcap);
const initialBase=union(consecutive,plus(B,B,1,tcap),all(46,2,2).map(n=>3*n-1));
const normals=union(B,[3,5,7,9,11,12,13,15,18,19,25,29]);
const yang=union([3,7,11,15,19,23,25,27,31,37,39,51,59], B.map(x=>2*x+1),all(81,5,4));
const fromGolay=sorted(B.map(x=>2*x+1));
// 1997 section 4, items 6–14. A real complementary quadruple at r supplies
// a new base-sequence sum 2r. Only aperiodic T-sequences enter the recursion.
let realBase=initialBase, quads=[], tseq=[];
const smallT=all(100).filter(n=>n!==97);
for(;;){
  tseq=union(smallT,B,realBase,times(yang,realBase,1,tcap));
  const first=union(realBase,times(normals,realBase,1,tcap),times(normals,tseq,1,tcap),
    times(fromGolay,tseq,1,tcap),times(consecutive,consecutive,1,tcap));
  quads=times(B,first,1,tcap);
  const next=union(realBase,quads.filter(n=>2*n<=tcap).map(n=>2*n));
  if(next.length===realBase.length)break;
  realBase=next;
}
const t=new Set(union(tseq,all(108).filter(n=>n!==97 && n!==103),[97,103,109,151,163,181,197]));
for(const n of quads)mark(4*n,'real complementary quadruple');
const wt=new Set(union(all(69,1,2),[73,79,83,91,93,95,97,103,109,111,127,133,181]));
for(let n=2;n<=64;n+=2)wt.add(n);
for(let q=5;(q+1)/2<=tcap;q+=4)if(pp[q])wt.add((q+1)/2);
// Keys w4, w5, wi, wj, wk and wn in the Seberry-Yamada index.
for(let q=5;q<=tcap;q+=4)if(pp[q]){
  if(q*(q+1)/2<=tcap)wt.add(q*(q+1)/2);
  if(pp[(q+1)/2] || conf.has((q+3)/2))wt.add(q+2);
  if(conf.has((q-1)/2) || symSet.has((q-1)/2))wt.add(q);
}
for(let u=1;u<=31;u+=2){wt.add(u*(4*u+3));wt.add(u*(4*u-1));}
let w=sorted(wt);
for(;;){const next=union(w,times(w,w,2,tcap),times(w,sorted(conf),1,tcap));if(next.length===w.length)break;w=next;}
const T=sorted(t);
for(const n of times(T,w,4,limit))mark(n,'Cooper-Wallis');
const s=all(Math.floor(tcap),1,2).filter(i=>pp[4*i-1]);
for(const n of times(T,s,4,limit))mark(n,'Paley blocks with T-matrices');
for(const n of w){const q=2*n+1;if(pp[q] && q%4===3)mark(8*q,'Seberry-Yamada');}
for(let q=3;8*q<=limit;q+=4)if(pp[q]&&pp[2*q-3])mark(8*q,'Miyamoto prime powers');
for(const h of certificates['complex-hadamard']){
  mark(2*h,'quaternary realification');
  if(prime[h+1] && (h+1)%4===3)mark(8*(h+1),'complex Miyamoto');
}
for(let q=5;4*q<=limit;q+=2)if(pp[q]&&pp[q-2])mark((q%4===1?4:8)*q,'Spence twin prime powers');
for(let q=5;4*(q+2)<=limit;q+=4)if(pp[q]){
  if(q%8===1 && conf.has((q+3)/2))mark(4*(q+2),'Yamada conference');
  if(q%8===5 && skew.has((q+3)/2))mark(4*(q+2),'Yamada skew');
}
for(const n of plus(D,B))mark(8*n,'1998 dihedral-binary');
const c0=[0,...C];
const csum=plus(c0,c0);
for(const n of csum)if(n)mark(8*n,'scalar complex Golay');
const base=union(all(87,1,2),C.map(n=>2*n+1)).filter(n=>n<=qcap);
const prod=times(c0,c0);
// Theorem 1 accepts any BS(m,n) as its second input, and Proposition 2
// accepts a real equal-length complementary quadruple as a complex one.
let E=union(base,times(C,realBase,2),times(C,base,2),plus(prod,prod,2)).filter(Boolean);
let dense=union(quads.filter(n=>n<=qcap),times(C,realBase),times(C,base),times(C,csum)).filter(Boolean);
const scales=times([2,10,26],C);
for(;;){
  const nextE=union(E,times(C,dense,4));
  const nextDense=union(dense,times(nextE,nextE),times(scales,dense));
  if(nextDense.length===dense.length && nextE.length===E.length)break;
  E=nextE;
  dense=nextDense;
}
for(const n of dense)mark(8*n,'Du-Jiang quad');
// Corollary 6 adds l*m at cost one or (s1+s2)*t at cost two.
// A total cost j gives multiplier 4^(j+1). All summands are positive.
const golayProduct=times(C,C);
const cbsSum=union(base,realBase,csum,dense.map(n=>2*n)).filter(n=>n>0 && n<=qcap);
const cbsProduct=times(C,cbsSum);
const sumsByCost=[[0]];
for(let j=1;4**(j+1)<=limit;j++){
  const scale=4**(j+1), cap=Math.floor(limit/scale);
  const sums=plus(sumsByCost[j-1],golayProduct,1,cap);
  sumsByCost[j]=j===1?sums:union(sums,plus(sumsByCost[j-2],cbsProduct,1,cap));
  for(const n of sumsByCost[j])mark(scale*n,'Du-Jiang Corollary 6');
}
// Four binary complementary sequences at length r imply H(64(r+1)).
// Normal lengths and Yang rules here use primarily Craigen-Kharaghani 1997 §4.
for(const r of quads)mark(64*(r+1),'Craigen-Kharaghani four sequences');
// Craigen 1995 Theorem 6(1) on one binary pair or one base-sequence quadruple.
for(const r of B)mark(16*(2*r+1),'Craigen single pair');
for(const r of realBase)mark(64*(2*r+1),'Craigen base sequences');
for(const r of B)for(const c of [3,5,11,13])mark(32*(2*r+c),'Craigen shifted pair');
for(const r of realBase)for(const c of [3,5,11,13])mark(128*(2*r+c),'Craigen shifted base sequences');
// Prop. 3.1 and the independently constructed 2335 avoid the Miyamoto symmetry issue.
for(const m of [787,823,883,1063,1303,2143,2335,3533,5441,5449,8237,8573])mark(4*m,'Djokovic 2010');
function divisors(n,predicate){for(let d=1;d*d<=n;d++)if(n%d===0 && predicate(d,n/d))return true;return false;}
function propagate(data,extra=new Set()){
  const pairs=new Uint8Array(1+limit/16);
  for(let n=4;n<=limit;n+=4){
    if(n%16===0){const r=n/16;pairs[r]=divisors(r,(a,b)=>data[4*a]&&data[4*b]);}
    if(data[n])continue;
    const q=n/4;
    if(data[n/2])data[n]='doubling';
    else if(q%4===1 && pp[q] && data[q-1])data[n]='Miyamoto I';
    else if(q%8===1 && pp[q] && data[(q-1)/2])data[n]='Yamada Hadamard';
    else if(n%8===0 && divisors(n/8,(a,b)=>data[4*a]&&data[4*b]))data[n]='Agaian';
    else if(n%16===0 && divisors(n/16,(a,b)=>pairs[a]&&pairs[b]))data[n]='Craigen-Seberry-Zhang';
    else if(extra.has(n))data[n]='direct family input';
  }
}
propagate(old);
if(process.argv.includes('--later')){
  const {checkLater}=await import('./priority-later-closure.mjs');
  const laterInputs={old,limit,prime,pp,sym,skew,conf,w,T,certificates,propagate,file};
  if(process.argv.includes('--priority')){
    const {checkPriorMethods}=await import('./priority-methods.mjs');
    const count=()=>old.reduce((n,r)=>n+Boolean(r),0);
    for(;;){
      const result=checkLater(laterInputs);
      const before=count();
      checkPriorMethods({old,B,C,consecutive,realBase,quads,dense,base,csum,normals,tseq,yang,
        w:sorted(result.wt.keys()),limit,union,times,plus,propagate,file});
      if(count()===before)break;
    }
    if(process.argv.includes('--claude-fill')){
      const {checkFill}=await import('./claude-fill.mjs');
      checkFill({old,actual,binaryLengths:B,pairLengths:input,limit,propagate});
    }
  }else checkLater(laterInputs);
  process.exit(0);
}
if(process.argv.includes('--priority')){
  const {checkPriorMethods}=await import('./priority-methods.mjs');
  checkPriorMethods({old,B,C,consecutive,realBase,quads,dense,base,csum,normals,tseq,yang,w,limit,union,times,plus,propagate,file});
  process.exit(0);
}
function oddPart(n){while(n%2===0)n/=2;return n;}
const byOdd=new Map();
const residual=sorted(actual.keys()).filter(n=>!old[n]);
for(const n of residual){const p=oddPart(n);if(!byOdd.has(p))byOdd.set(p,n);}
const outside=residual.filter(n=>oddPart(n)>2999);
function firstOlder(n){
  for(let order=n*2;order<=limit;order*=2)if(old[order])return [order,old[order]];
  return ['',''];
}
const known3=[25072,46192,47968];
for(const n of known3)assert(residual.includes(n));
assert.deepEqual(residual.filter(n=>oddPart(n)<=2999),known3);
const afterThree=old.slice();
propagate(afterThree,new Set(known3));
const afterFamily=old.slice();
propagate(afterFamily,new Set(residual));
if(process.argv.includes('--length19')){
  const unrestricted=times([19],B);
  const sizes=union(plus(unrestricted,B,16,limit),plus(unrestricted,union(input,unrestricted),32,limit));
  const unique=sizes.filter(n=>!afterFamily[n]);
  const outside19=unique.filter(n=>oddPart(n)>2999);
  console.log('Length-19 comparison after older constructions and the propagated original family');
  console.log('Orders',sizes.length,'additional orders',unique.length,'outside',outside19.length,
    'outside odd parts',new Set(outside19.map(oddPart)).size);
  console.log('Additional inside the current frontier',unique.filter(n=>oddPart(n)<=2999));
  console.log('Earlier comparison at 191936',old[191936]??'none found');
  process.exit(0);
}
function provenance(n){
  if(afterThree[n])return 'from original three: '+afterThree[n];
  if(afterFamily[n]!=='direct family input')return 'from earlier family orders: '+afterFamily[n];
  return 'direct family input';
}
if(process.argv.includes('--records')){
  console.log('order\todd_part\tpower_of_two\tlength_1\tlength_2\tfirst_surviving_order\tolder_order_in_window\tolder_source\tafter_family_propagation');
  for(const n of outside){const p=oddPart(n);console.log([n,p,n/p,...actual.get(n),byOdd.get(p),...firstOlder(n),provenance(n)].join('\t'));}
}else{
  console.log({orders:actual.size,older:[...actual.keys()].filter(n=>old[n]).length,remaining:residual.length,outside:outside.length,distinctOutside:new Set(outside.map(oddPart)).size});
  console.log('From original three',outside.filter(n=>afterThree[n]).length,'and direct additions needed',outside.filter(n=>afterFamily[n]==='direct family input').length);
  for(const bound of [100000,250000,500000,1000000]){
    const hit=outside.filter(n=>n<=bound);
    console.log(bound,hit.length,new Set(hit.map(oddPart)).size);
  }
  for(const lo of [9999,39999]){
    const hit=outside.filter(n=>oddPart(n)>lo);
    console.log('Odd part above',lo,hit.length,'orders and',new Set(hit.map(oddPart)).size,'distinct odd parts');
  }
  console.log('First outside',outside.slice(0,20).map(n=>[n,oddPart(n),...actual.get(n)]));
}

