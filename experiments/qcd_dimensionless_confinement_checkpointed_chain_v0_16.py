import numpy as np, math, json, pickle, sys, os, time
from pathlib import Path
L=4; d=4; beta=2.84903771431338; eps=1.0
state_path=Path('/mnt/data/qcd_chain_state.pkl')
data_path=Path('/mnt/data/qcd_chain_measurements.jsonl')
pairs=[(0,1),(0,2),(1,2)]; coords=list(np.ndindex((L,L,L,L)))
def sh(x,mu,s=1):
 y=list(x); y[mu]=(y[mu]+s)%L; return tuple(y)
def proposal(rng):
 a,b=pairs[rng.integers(3)]; axis=rng.normal(size=3); axis/=np.linalg.norm(axis); ang=rng.uniform(-eps,eps)
 c=math.cos(ang); s=math.sin(ang); xx,yy,zz=axis
 M=np.eye(3,dtype=complex); sub=np.array([[c+1j*zz*s,(yy+1j*xx)*s],[(-yy+1j*xx)*s,c-1j*zz*s]],complex); M[np.ix_([a,b],[a,b])]=sub
 return M
def plaq(U,x,mu,nu):
 xp=sh(x,mu); xn=sh(x,nu)
 return U[x+(mu,)]@U[xp+(nu,)]@U[xn+(mu,)].conj().T@U[x+(nu,)].conj().T
def local(U,x,mu):
 v=0.
 for nu in range(d):
  if nu==mu: continue
  v+=np.trace(plaq(U,x,mu,nu)).real; v+=np.trace(plaq(U,sh(x,nu,-1),mu,nu)).real
 return v
def sweep(U,rng):
 acc=0; tot=0
 for x in coords:
  for mu in range(d):
   old=local(U,x,mu); oldU=U[x+(mu,)].copy(); U[x+(mu,)]=proposal(rng)@oldU; new=local(U,x,mu)
   if math.log(rng.random()) < (beta/3)*(new-old): acc+=1
   else: U[x+(mu,)]=oldU
   tot+=1
 return acc/tot
def loop(U,x,mu,nu,R,T):
 M=np.eye(3,dtype=complex); y=x
 for _ in range(R): M=M@U[y+(mu,)]; y=sh(y,mu)
 for _ in range(T): M=M@U[y+(nu,)]; y=sh(y,nu)
 for _ in range(R): y=sh(y,mu,-1); M=M@U[y+(mu,)].conj().T
 for _ in range(T): y=sh(y,nu,-1); M=M@U[y+(nu,)].conj().T
 return np.trace(M).real/3
def measure(U):
 out={}
 for R,T in ((1,1),(1,2),(2,1),(2,2)):
  vals=[]
  for x in coords:
   for mu in range(d):
    for nu in range(mu+1,d): vals.append(loop(U,x,mu,nu,R,T))
  out[f'W{R}{T}']=float(np.mean(vals))
 return out
def save(U,rng,meta):
 with open(state_path,'wb') as f: pickle.dump({'U':U,'rng_state':rng.bit_generator.state,'meta':meta},f,protocol=5)
def load():
 with open(state_path,'rb') as f: st=pickle.load(f)
 rng=np.random.default_rng(); rng.bit_generator.state=st['rng_state']; return st['U'],rng,st['meta']
mode=sys.argv[1]
if mode=='init':
 ns=int(sys.argv[2]); rng=np.random.default_rng(260928); U=np.zeros((L,L,L,L,d,3,3),complex); U[...] = np.eye(3); meta={'sweeps':0,'measurements':0}; acc=[]; t=time.time()
 for i in range(ns):
  acc.append(sweep(U,rng)); meta['sweeps']+=1
  if (i+1)%50==0: print(json.dumps({'mode':'init','done':i+1,'target':ns,'acc_recent':float(np.mean(acc[-50:])),'elapsed':time.time()-t}),flush=True)
 save(U,rng,meta); print(json.dumps({'status':'SAVED','meta':meta,'acc_mean':float(np.mean(acc))}))
elif mode=='measure':
 n=int(sys.argv[2]); gap=int(sys.argv[3]); U,rng,meta=load(); acc=[]; rows=[]; t=time.time()
 for i in range(n):
  for _ in range(gap): acc.append(sweep(U,rng)); meta['sweeps']+=1
  row=measure(U); row['measurement_index']=meta['measurements']; row['sweeps']=meta['sweeps']; rows.append(row); meta['measurements']+=1
  if (i+1)%10==0: print(json.dumps({'mode':'measure','done':i+1,'target':n,'W22_recent':float(np.mean([r['W22'] for r in rows[-10:]])),'elapsed':time.time()-t}),flush=True)
 with open(data_path,'a') as f:
  for row in rows: f.write(json.dumps(row,sort_keys=True)+'\n')
 save(U,rng,meta); print(json.dumps({'status':'SAVED','meta':meta,'acc_mean':float(np.mean(acc)),'chunk_means':{k:float(np.mean([r[k] for r in rows])) for k in ['W11','W12','W21','W22']}}))
elif mode=='summary':
 rows=[json.loads(x) for x in data_path.read_text().splitlines() if x.strip()]; rng=np.random.default_rng(99); keys=['W11','W12','W21','W22']; arr={k:np.array([r[k] for r in rows]) for k in keys}; means={k:float(v.mean()) for k,v in arr.items()}; ses={k:float(v.std(ddof=1)/math.sqrt(len(v))) for k,v in arr.items()}; chi=None
 if min(means.values())>0: chi=-math.log(means['W11']*means['W22']/(means['W12']*means['W21']))
 chis=[]
 for _ in range(5000):
  idx=rng.integers(0,len(rows),len(rows)); m={k:float(v[idx].mean()) for k,v in arr.items()}
  if min(m.values())>0: chis.append(-math.log(m['W11']*m['W22']/(m['W12']*m['W21'])))
 print(json.dumps({'n':len(rows),'means':means,'ses':ses,'chi':chi,'bootstrap_valid':len(chis),'chi_boot_mean':float(np.mean(chis)) if chis else None,'chi_boot_sd':float(np.std(chis,ddof=1)) if len(chis)>1 else None,'chi_quantiles':np.quantile(chis,[.025,.5,.975]).tolist() if chis else None},sort_keys=True))
