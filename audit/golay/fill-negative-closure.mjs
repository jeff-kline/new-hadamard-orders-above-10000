import fs from 'node:fs';
const orders=fs.readFileSync(new URL('claude-fill.tsv',import.meta.url),'utf8').trim().split('\n').slice(1).map(x=>+x.split('\t')[0]);
function divisors(n){
  const list=[];
  for(let x=1;x*x<=n;x++)if(n%x===0){list.push(x);if(x*x<n)list.push(n/x);}
  return list.sort((a,b)=>a-b);
}
function pp(n){
  if(n<2)return false;
  const p=divisors(n)[1];
  while(n%p===0)n/=p;
  return n===1;
}
function golay(n){
  if(n===1)return true;
  return [2,10,26].some(g=>n%g===0&&golay(n/g));
}
function base(t){
  if(t%2===0)return;
  if(t===1)return 'bare NG pair';
  if(t<=87||golay((t-1)/2))return 'consecutive';
  if(t<=1497)return 'odd length upper bound';
  if(golay(t-1))return 'Golay+1';
  if((t+1)%6===0&&(t+1)/3<=46)return 'Turyn type';
}
function ng(v){
  for(const g of divisors(v).filter(golay)){
    const u=v/g;
    if(u===1)return [g,'Golay',1];
    if(u%2)continue;
    if(pp(u-1))return [g,'Prop6',u-1];
    if(pp(2*u-1))return [g,'Prop8',2*u-1];
    if(u<=2996)return [g,'small NG upper bound',u];
    if((u/2)%1===0&&divisors(u/2).every(d=>d===1||[2,3,5,11,13].some(p=>d%p===0)))return [g,'smooth complex length upper bound',u/2];
    for(const p of divisors(u))if(p%4===1&&pp(p)&&p*(p+1)===u)return [g,'Whiteman upper screen',p];
  }
}
const hits=[];
for(const D of orders){
  const p=Math.max(...divisors(D).filter(q=>q>2&&divisors(q).length===2));
  const wins=[];
  for(const H of divisors(2*D).filter(x=>x%4===0&&x%p===0)){
    // Agaian has output H*K/2, where K=2D/H must itself exist.
    const K=2*D/H;
    if(K!==2&&K%4!==0)continue;
    for(const t of divisors(H/4)){
      const bs=base(t);
      if(!bs)continue;
      const v=H/(2*t),src=ng(v);
      if(src)wins.push({H,K,t,v,bs,src});
    }
  }
  for(const H of divisors(2*D).filter(x=>x%4===0&&x%p!==0)){
    const K=2*D/H;
    if(K%4===0&&H>272)throw Error('large cofactor');
  }
  if(wins.length)hits.push(D);
  console.log(D,JSON.stringify(wins));
}
if(String(hits)!=='513296,670928,806608,812176,915760,953264')throw Error('unexpected hits');
