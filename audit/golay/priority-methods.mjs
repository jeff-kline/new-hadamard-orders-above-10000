// Called by node family-million.mjs --priority. Keep the original census
// reproducible and test published constructions independently of new inputs.
export function checkPriorMethods({old,B,C,consecutive,realBase,quads,dense,base,csum,normals,tseq,yang,w,limit,union,times,plus,propagate,file}){
  const baseline=old.slice();
  const targets=file('family-candidates.tsv').trim().split('\n').slice(1).map(row=>Number(row.split('\t')[0]));
  function mark(n,reason){if(n<=limit && !old[n])old[n]=reason;}
  // Livinskyi 4.7 permits an arbitrary real base sequence on the first side.
  // The two factors of 2 in 4.8 (complex) and B <-- 2*quads are essential.
  let bases=realBase, realQuads=quads;
  const lengths=union(consecutive,normals.map(n=>2*n+1));
  for(;;){
    realQuads=union(realQuads,times(B,times(lengths,bases,1,limit/4),1,limit/4));
    const next=union(bases,realQuads.filter(n=>n<=limit/8).map(n=>2*n));
    if(next.length===bases.length)break;
    bases=next;
  }
  for(const n of realQuads) {
    mark(4*n,'Yang real quadruple, length '+n);
    mark(64*(n+1),'Craigen–Kharaghani Corollary 10, real quad '+n);
  }
  const apT=union(tseq,bases,times(yang,bases,1,limit/4));
  for(const h of [1,5,9])for(const t of apT){
    for(const z of w){
      const n=4*h*t*z;
      if(n>limit)break;
      if(!old[n])mark(n,'Baumert–Hall–Welch and T-sequences h='+h+', t='+t+', WT='+z);
    }
  }
  const complexBases=union(csum,base,times(C,bases),dense.filter(n=>n<=limit/16).map(n=>2*n));
  const complexQuads=times(complexBases,base,2,limit/8);
  for(const n of complexQuads)mark(8*n,'complex Yang quadruple, length '+n);
  const cbs=union(complexBases,complexQuads.map(n=>2*n));

  // Build every permitted union of aperiodic pairs and base quadruples for
  // the shifts in Craigen (1995), Thm. 6 and Livinskyi (2012), Thm. 3.11.
  function halfLengths(pair,quad){
    const sums=[[0]];
    for(let t=1;4**(t+1)<=limit;t++){
      const cap=Math.floor(limit/(2*4**(t+1)));
      sums[t]=plus(sums[t-1],pair,1,cap);
      if(t>=2)sums[t]=union(sums[t],plus(sums[t-2],quad,1,cap));
    }
    return sums;
  }
  const real=halfLengths(B,bases), complex=halfLengths(C,cbs), rules=[];
  function transfer(source,degree,order,detail){
    if(order>limit)return;
    mark(order,source+' '+detail);
    rules.push({degree,order,source,detail});
  }
  for(let t=1;t<real.length;t++){
    const scale=4**(t+1);
    for(const l of real[t]){
      const label='t='+t+', L='+l;
      transfer('Craigen 6(1,5)',scale/2,scale*(2*l+1),label);
      for(const h of [3,5,11,13])transfer('Craigen 6(2,3,6)',scale,2*scale*(2*l+h),label+', shift='+h);
      for(const g of C){
        const p=2*l+2*g+1;
        if(2*scale*p>limit)break;
        mark(2*scale*p,'Craigen 6(4), '+label+', g='+g);
        // Part 7 uses a larger degree than Part 4.
        transfer('Craigen 6(7)',4*scale,8*scale*p,label+', g='+g);
      }
    }
    for(const l of complex[t])mark(2*scale*(2*l+1),'Livinskyi 3.11, t='+t+', L='+l);
  }
  const baselineCount=()=>old.reduce((s,v)=>s+Boolean(v),0);
  for(;;){
    const before=baselineCount();
    for(const {degree,order,source,detail} of rules){
      for(let q=2;order*q<=limit;q++)if(old[degree*q])
        mark(order*q,source+' '+detail+', q='+q+', H('+degree*q+')');
    }
    propagate(old);
    if(baselineCount()===before)break;
  }
  for(const n of targets)if(old[n])console.log(n,old[n]);
  console.log('Additional older orders among the 94:',targets.filter(n=>old[n]).length);
  for(const n of [25072,46192,47968])if(old[n])console.log('Original frontier row',n,old[n]);
  if(process.argv.includes('--trace')){
    for(const arg of process.argv.slice(process.argv.indexOf('--trace')+1)){
      const n=Number(arg);
      console.log(n,old[n]??'no witness',baseline[n]??'absent from baseline');
    }
  }
}
