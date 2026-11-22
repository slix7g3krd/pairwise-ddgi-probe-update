import pytest
import render.ddgi_probe_update as mod

CASES = [
    ("probe_update_queue", (1, 2)),
    ("cascade_blend", (1, 2)),
    ("moving_mark", (1, 2)),
    ("irradiance_reset", (1, 2)),
    ("probe_grid", (8, 4)),
    ("update_budget", (64, 32)),
    ("leak_detect", (1, 2)),
    ("border_seam", (1, 2)),
    ("probe_classify", (1, 2)),
    ("relocation", (1, 2)),
    ("frame_budget", (1, 2)),
    ("occlusion_bias", (0.1, 0.2)),
    ("hysteresis", (2, 3)),
    ("validation", (1, 2)),
    ("light_leak_metric", (1.0, 2.0)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
