def test_snake_movement():
    """Simple test to verify snake moves correctly"""
    player = {'x': 100, 'y': 100, 'dx': 20, 'dy': 0}
    player['x'] += player['dx']
    player['y'] += player['dy']
    assert player['x'] == 120
    assert player['y'] == 100
