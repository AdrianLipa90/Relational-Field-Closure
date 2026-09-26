import numpy as np, math, time, json
from pathlib import Path

# Reproducible finite-volume pilot only. Not a confinement proof.
L=4
d=4
beta=2.84903771431338
seed=260926
therm=80
nmeas=30
gap=2
eps=0.45
rng=np.random.default_rng(seed)

U=np.zeros((L,L,L,L,d,3,3),complex)
U[...] = np.eye(3)
pairs=[(0,1),(0,2),(1,2)]
coords=list(np.ndindex((L,L,L,L)))

def sh(x,mu,s=1):
    y=list(x); y[mu]=(y[mu]+s)%L
    return tuple(y)

def plaq(x,mu,nu):
    xp=sh(x,mu); xn=sh(x,nu)
    return U[x+(mu,)]@U[xp+(nu,)]@U[xn+(mu,)].conj().T@U[x+(nu,)].conj().T

def local_score(x,mu):
    out=0.0
    for nu in range(d):
        if nu==mu: continue
        out += np.trace(plaq(x,mu,nu)).real
        out += np.trace(plaq(sh(x,nu,-1),mu,nu)).real
    return out

def proposal():
    a,b=pairs[rng.integers(3)]
    axis=rng.normal(size=3); axis/=np.linalg.norm(axis)
    ang=rng.uniform(-eps,eps)
    c=math.cos(ang); s=math.sin(ang)
    xx,yy,zz=axis
    M=np.eye(3,dtype=complex)
    sub=np.array([
        [c+1j*zz*s,(yy+1j*xx)*s],
        [(-yy+1j*xx)*s,c-1j*zz*s]
    ],complex)
    M[np.ix_([a,b],[a,b])]=sub
    return M

def proposal_self_test(samples=1000):
    max_u=max_det=0.0
    for _ in range(samples):
        P=proposal()
        max_u=max(max_u,float(np.linalg.norm(P.conj().T@P-np.eye(3))))
        max_det=max(max_det,float(abs(np.linalg.det(P)-1.0)))
    return max_u,max_det

def sweep():
    accepted=total=0
    for x in coords:
        for mu in range(d):
            old=local_score(x,mu)
            oldU=U[x+(mu,)].copy()
            U[x+(mu,)]=proposal()@oldU
            new=local_score(x,mu)
            if math.log(rng.random()) < (beta/3.0)*(new-old):
                accepted += 1
            else:
                U[x+(mu,)]=oldU
            total += 1
    return accepted/total

def loop(x,mu,nu,R,T):
    M=np.eye(3,dtype=complex)
    y=x
    for _ in range(R):
        M=M@U[y+(mu,)]; y=sh(y,mu)
    for _ in range(T):
        M=M@U[y+(nu,)]; y=sh(y,nu)
    for _ in range(R):
        y=sh(y,mu,-1); M=M@U[y+(mu,)].conj().T
    for _ in range(T):
        y=sh(y,nu,-1); M=M@U[y+(nu,)].conj().T
    return np.trace(M).real/3.0

def measure():
    out={}
    for R,T in ((1,1),(1,2),(2,1),(2,2)):
        vals=[]
        for x in coords:
            for mu in range(d):
                for nu in range(mu+1,d):
                    vals.append(loop(x,mu,nu,R,T))
        out[f"W{R}{T}"]=float(np.mean(vals))
    return out

max_u,max_det=proposal_self_test()
assert max_u<1e-12 and max_det<1e-12

acc=[]
data=[]
for sw in range(therm+nmeas*gap):
    acc.append(sweep())
    if sw>=therm and (sw-therm)%gap==0:
        data.append(measure())

arr={k:np.array([m[k] for m in data]) for k in data[0]}
means={k:float(v.mean()) for k,v in arr.items()}
chi=None
if min(means.values())>0:
    chi=-math.log(means["W11"]*means["W22"]/(means["W12"]*means["W21"]))

result={
    "status":"FINITE_VOLUME_PILOT_ONLY",
    "L":L,
    "beta_W":beta,
    "seed":seed,
    "proposal_unitarity_max":max_u,
    "proposal_det_max":max_det,
    "acceptance":float(np.mean(acc)),
    "means":means,
    "std_errors":{k:float(v.std(ddof=1)/math.sqrt(len(v))) for k,v in arr.items()},
    "creutz_11":chi
}
print(json.dumps(result,indent=2,sort_keys=True))
