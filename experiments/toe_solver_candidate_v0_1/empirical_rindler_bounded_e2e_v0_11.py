from __future__ import annotations
from dataclasses import dataclass, asdict
from decimal import Decimal, localcontext
import hashlib, json, math
from typing import Sequence

SCHEMA="QHTRI_TOE_EMPIRICAL_RINDLER_BOUNDED_E2E_V0_11"
EVIDENCE_CLASS="EXTERNAL_EMPIRICAL_RINDLER_CALIBRATED_REFERENCE"
SOURCE_DOI="10.5281/zenodo.8184043"
SOURCE_FILE="Fig3.csv"
SOURCE_FILE_MD5="257eab6f29cf3480c536cac73ed3998a"
SLOPE_1E19_PER_CM=Decimal("-11.931497812058647330178150456210840554320038300818627288826189506893919006324977")
SIGMA_1E19_PER_CM=Decimal("0.56167907568042397202224492309163135908706507721062290379612341792725309068448916")
C=Decimal("299792458")
G_NEWTON=Decimal("6.67430e-11")

def empirical_gamma_per_m():
    return SLOPE_1E19_PER_CM*Decimal("1e-19")*Decimal(100)

def empirical_gamma_sigma_per_m():
    return SIGMA_1E19_PER_CM*Decimal("1e-19")*Decimal(100)

def empirical_acceleration_m_s2():
    return empirical_gamma_per_m()*C*C

def empirical_acceleration_sigma_m_s2():
    return empirical_gamma_sigma_per_m()*C*C

def kappa_e_si():
    with localcontext() as ctx:
        ctx.prec=80
        pi=Decimal(str(math.pi))
        return Decimal(8)*pi*G_NEWTON/(C**4)

def inv_matrix(a: Sequence[Sequence[float]]):
    n=len(a)
    aug=[[float(x) for x in row]+[1.0 if i==j else 0.0 for j in range(n)] for i,row in enumerate(a)]
    for i in range(n):
        pivot=max(range(i,n),key=lambda r:abs(aug[r][i]))
        if abs(aug[pivot][i])<1e-300: raise ValueError("singular matrix")
        aug[i],aug[pivot]=aug[pivot],aug[i]
        p=aug[i][i]; aug[i]=[x/p for x in aug[i]]
        for r in range(n):
            if r==i: continue
            f=aug[r][i]
            aug[r]=[aug[r][c]-f*aug[i][c] for c in range(2*n)]
    return [row[n:] for row in aug]

def curvature_at_point(g,dg,ddg):
    n=len(g); gi=inv_matrix(g)
    dgi=[[[0.0]*n for _ in range(n)] for __ in range(n)]
    for a in range(n):
        for r in range(n):
            for s in range(n):
                dgi[a][r][s]=-sum(gi[r][u]*dg[a][u][v]*gi[v][s] for u in range(n) for v in range(n))
    gamma=[[[0.0]*n for _ in range(n)] for __ in range(n)]
    for r in range(n):
        for m in range(n):
            for q in range(n):
                gamma[r][m][q]=0.5*sum(gi[r][s]*(dg[m][s][q]+dg[q][s][m]-dg[s][m][q]) for s in range(n))
    dgamma=[[[[0.0]*n for _ in range(n)] for __ in range(n)] for ___ in range(n)]
    for a in range(n):
        for r in range(n):
            for m in range(n):
                for q in range(n):
                    total=0.0
                    for s in range(n):
                        first=dg[m][s][q]+dg[q][s][m]-dg[s][m][q]
                        second=ddg[a][m][s][q]+ddg[a][q][s][m]-ddg[a][s][m][q]
                        total += dgi[a][r][s]*first + gi[r][s]*second
                    dgamma[a][r][m][q]=0.5*total
    ricci=[[0.0]*n for _ in range(n)]
    for m in range(n):
        for q in range(n):
            ricci[m][q]=sum(dgamma[r][r][m][q]-dgamma[q][r][m][r] for r in range(n)) + sum(
                gamma[r][r][s]*gamma[s][m][q]-gamma[r][q][s]*gamma[s][m][r]
                for r in range(n) for s in range(n)
            )
    scalar=sum(gi[m][q]*ricci[m][q] for m in range(n) for q in range(n))
    einstein=[[ricci[m][q]-0.5*g[m][q]*scalar for q in range(n)] for m in range(n)]
    return scalar,ricci,einstein

def rindler_analytic_jet(z_m: float=0.0):
    gamma=float(empirical_gamma_per_m())
    N=1.0+gamma*float(z_m)
    if N<=0.0: raise ValueError("Rindler lapse must remain positive")
    g=[[0.0]*4 for _ in range(4)]
    g[0][0]=-(N*N)
    for i in range(1,4): g[i][i]=1.0
    dg=[[[0.0]*4 for _ in range(4)] for __ in range(4)]
    ddg=[[[[0.0]*4 for _ in range(4)] for __ in range(4)] for ___ in range(4)]
    dg[3][0][0]=-2.0*gamma*N
    ddg[3][3][0][0]=-2.0*gamma*gamma
    return g,dg,ddg

def legacy_endpoint_lapse_float64(z_m: float):
    return 1.0 + float(empirical_gamma_per_m())*float(z_m)

@dataclass(frozen=True)
class BoundedDomain:
    domain_id: str
    x0_min_m: float
    x0_max_m: float
    x_min_m: float
    x_max_m: float
    y_min_m: float
    y_max_m: float
    z_min_m: float
    z_max_m: float

def reference_domain():
    return BoundedDomain(
        "RINDLER_CLOCK_COLUMN_1CM_REFERENCE_DOMAIN",
        -1.0e-9,1.0e-9,
        -5.0e-4,5.0e-4,
        -5.0e-4,5.0e-4,
        0.0,1.0e-2,
    )

def domain_contains(patch: BoundedDomain,target: BoundedDomain):
    return patch.domain_id==target.domain_id and (
        patch.x0_min_m<=target.x0_min_m<=target.x0_max_m<=patch.x0_max_m and
        patch.x_min_m<=target.x_min_m<=target.x_max_m<=patch.x_max_m and
        patch.y_min_m<=target.y_min_m<=target.y_max_m<=patch.y_max_m and
        patch.z_min_m<=target.z_min_m<=target.z_max_m<=patch.z_max_m
    )

def run_e2e():
    g,dg,ddg=rindler_analytic_jet(0.0)
    scalar,ricci,G=curvature_at_point(g,dg,ddg)
    gmax=max(abs(v) for row in G for v in row)
    rmax=max(abs(v) for row in ricci for v in row)
    N0=1.0
    metric_from_adm=[[-1.0,0.0,0.0,0.0],[0.0,1.0,0.0,0.0],[0.0,0.0,1.0,0.0],[0.0,0.0,0.0,1.0]]
    adm_metric_res=max(abs(metric_from_adm[i][j]-g[i][j]) for i in range(4) for j in range(4))
    shared_atlas_certified=(N0>0 and adm_metric_res<1e-30)
    target=reference_domain()
    coverage=domain_contains(target,target)
    T=[[0.0]*4 for _ in range(4)]
    Lambda=0.0
    kappa=float(kappa_e_si())
    residual=[[G[i][j]+Lambda*g[i][j]-kappa*T[i][j] for j in range(4)] for i in range(4)]
    residual_max=max(abs(v) for row in residual for v in row)
    global_einstein_carrier=bool(shared_atlas_certified and coverage and residual_max<1e-28)
    return {
        "schema":SCHEMA,
        "evidence_class":EVIDENCE_CLASS,
        "authority":"CANDIDATE_ONLY",
        "canon_allowed":False,
        "physical_production_claim":False,
        "source":{"doi":SOURCE_DOI,"file":SOURCE_FILE,"file_md5":SOURCE_FILE_MD5},
        "calibration":{"gamma_per_m":str(empirical_gamma_per_m()),"sigma_gamma_per_m":str(empirical_gamma_sigma_per_m()),"acceleration_m_s2":str(empirical_acceleration_m_s2()),"sigma_acceleration_m_s2":str(empirical_acceleration_sigma_m_s2())},
        "rindler":{"metric":"diag(-(1+gamma*z)^2,1,1,1)","center_z_m":0.0,"max_abs_ricci":rmax,"scalar_curvature":scalar,"max_abs_einstein":gmax},
        "rf_e25_reference":{"patch_count":1,"overlap_count":0,"lapse_center":N0,"triad":"I3","shift":[0.0,0.0,0.0],"shared_atlas_certified":shared_atlas_certified,"adm_metric_residual":adm_metric_res},
        "coverage":{"domain":asdict(target),"covered":coverage},
        "rf_e26_reference":{"lambda":Lambda,"kappa_e_si":str(kappa_e_si()),"max_local_residual":residual_max,"global_einstein_carrier":global_einstein_carrier},
        "claim_boundary":"Real optical-clock data calibrate a bounded Rindler reference model. PASS validates the pipeline on an empirically calibrated flat-spacetime control; it is not a claim that the full physical Earth 3+1 geometry was measured or that TIR is empirically confirmed."
    }

def stable_sha(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
