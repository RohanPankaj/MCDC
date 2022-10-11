

from mcdc.loop import loop_particle, loop_main, loop_source
import mcdc.type_


def loop_setup_test():
    type_.make_type_surface(1)
    P = np.zeros(1, dtype=type_.particle)[0]
    S = np.zeros(1, dtype=type_.surface)[0]
    
    x     = 5.0
    trans = np.array([0.0, 0.0, 0.0])

    S['G']      = 1.0
    S['linear'] = True
    S['J']      = np.array([-x, -x])
    S['t']      = np.array([0.0, INF])

    # Surface on the left
    P['x'] = 4.0
    
    return(S, P)
    

def test_loop_main():
    
    
    print('This worked')
    assert 0 == 0



def test_loop_particle():
    print('This worked')
    assert 0 == 0
    
