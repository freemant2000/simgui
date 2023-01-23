from simgui.transforms import Map2D
import pytest

def test_map():
  m=Map2D((3, 4), (5, 8), (9, 14), (15, 12))
  x, y=m.map((3, 4))
  assert x==pytest.approx(9, 0.1)
  assert y==pytest.approx(14, 0.1)
  x, y=m.map((5, 8))
  assert x==pytest.approx(15, 0.1)
  assert y==pytest.approx(12, 0.1)
  x, y=m.map((3, 8))
  assert x==pytest.approx(9, 0.1)
  assert y==pytest.approx(12, 0.1)
  x, y=m.map((4, 6))
  assert x==pytest.approx(12, 0.1)
  assert y==pytest.approx(13, 0.1)

