from __future__ import annotations
import math
from typing import Callable, Sequence

STATUS='CANDIDATE_NUMERICAL_ADAPTER_NOT_CANONICAL'
SCOPE='metric callable -> g,dg,ddg via centered finite differences'

def _mat4(m):
    if len(m)!=4 or any(len(r)!=4 for r in m): raise ValueError('metric must be 4x4')
    out=[[float(x) for x in r] for r in m]
    if not all(math.isfinite(x) for r in out for x in r): raise ValueError('metric must be finite')
    return out

def metric_jet_4d(metric_fn: Callable[[Sequence[float]], Sequence[Sequence[float]]], point: Sequence[float], h: float=1e-4):
    x=[float(v) for v in point]
    if len(x)!=4 or not all(math.isfinite(v) for v in x): raise ValueError('point must be finite 4-vector')
    h=float(h)
    if not math.isfinite(h) or h<=0: raise ValueError('h must be finite positive')
    g=_mat4(metric_fn(x))
    dg=[[[0.0]*4 for _ in range(4)] for __ in range(4)]
    ddg=[[[[0.0]*4 for _ in range(4)] for __ in range(4)] for ___ in range(4)]
    def ev(y): return _mat4(metric_fn(y))
    plus=[]; minus=[]
    for a in range(4):
        xp=x.copy(); xm=x.copy(); xp[a]+=h; xm[a]-=h
        gp,gm=ev(xp),ev(xm); plus.append(gp); minus.append(gm)
        for m in range(4):
            for n in range(4):
                dg[a][m][n]=(gp[m][n]-gm[m][n])/(2*h)
                ddg[a][a][m][n]=(gp[m][n]-2*g[m][n]+gm[m][n])/(h*h)
    for a in range(4):
        for b in range(a+1,4):
            xpp=x.copy(); xpm=x.copy(); xmp=x.copy(); xmm=x.copy()
            xpp[a]+=h; xpp[b]+=h
            xpm[a]+=h; xpm[b]-=h
            xmp[a]-=h; xmp[b]+=h
            xmm[a]-=h; xmm[b]-=h
            gpp,gpm,gmp,gmm=ev(xpp),ev(xpm),ev(xmp),ev(xmm)
            for m in range(4):
                for n in range(4):
                    v=(gpp[m][n]-gpm[m][n]-gmp[m][n]+gmm[m][n])/(4*h*h)
                    ddg[a][b][m][n]=v; ddg[b][a][m][n]=v
    return g,dg,ddg
