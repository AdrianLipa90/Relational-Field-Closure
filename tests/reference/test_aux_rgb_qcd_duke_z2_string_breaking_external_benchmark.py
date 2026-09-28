from pathlib import Path
import importlib.util

ROOT=Path(__file__).resolve().parents[2]
SCRIPT=ROOT/'experiments'/'duke_z2_string_breaking_external_benchmark_v0_17.py'
spec=importlib.util.spec_from_file_location('duke_z2_v017',SCRIPT)
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)

def test_external_benchmark_v017_passes():
    result=mod.run()
    assert result['status']=='PASS'
    assert result['checks']['dimension_exact_2pow13']
    assert result['checks']['virtual_field_symmetric']
    assert result['checks']['all_nine_exact_scans_edge_excess_positive']
    assert result['checks']['all_confined_perturbative_initial_states_edge_enhanced']
    assert result['checks']['published_velocity_identity']
    assert result['checks']['published_period_identity']

def test_provenance_firewall_is_explicit():
    result=mod.run()
    assert 'full_SU3_QCD_confirmation' in result['not_claimed']
    assert 'PhaseNav_confirmation' in result['not_claimed']
    assert 'priority_or_independent_prediction_provenance' in result['not_claimed']
