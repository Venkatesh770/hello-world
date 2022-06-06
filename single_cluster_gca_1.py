import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

__author__ = 'Paolo Moretti'

def plot_configuration(xs,ys,rs):
    '''Plots current system configuration

    Args:
        xs, ys, rs (np.array): current positions and radii
    '''
    f, ax = plt.subplots(figsize=(10,10))
    ax.set_xlim([0,L])
    ax.set_ylim([0,L])

    for x, y, r in zip(xs, ys, rs):
        ax.add_artist(Circle(xy=(x, y), fc='none', ec='k', radius=r)) 
    plt.draw()


def reflect(x,y,xp,yp):
    '''Performs reflection around pivot

    Args:
        x, y (float): coorindates of particle to be reflected
        xp, yp: coordinates of pivot
    Returns:
        xx, yy: coordinates of reflected particle
    '''
    xx,yy = 2*xp - x, 2*yp - y
    while xx<0:
        xx = xx+L
    while xx>L:
        xx = xx-L
    while yy<0:
        yy = yy+L
    while yy>L:
        yy = yy-L    
    return xx,yy


def check_overlap(x1,y1,r1,x2,y2,r2):
    '''Checks if two particles overlap

    Args: 
        x1, y1, x2, y2 (float):  coordinates of the particles
        r1, r2 (float): radii of the particles
    Returns: True if particles overlap, False otherwise
    '''
    delta_x = np.abs(x2-x1)
    delta_x_alt = np.abs(L-delta_x)
    dx = np.minimum(delta_x, delta_x_alt) 
    delta_y = np.abs(y2-y1)
    delta_y_alt = np.abs(L-delta_y)
    dy = np.minimum(delta_y, delta_y_alt) 
    sr = r1+r2
    return ( (dx*dx) + (dy*dy) ) < sr*sr    


def cluster_move(source,xs,ys,xp,yp):
    '''Performs a single cluster move, modifying particle coordinates in place

    Args:
        source (int): first particle to be reflected
        xs, ys (np.array): coordinate vectors of previous configuration
        xp, yp (float): coordinates of pivot    
    '''
    N = len(xs)
    reflected = np.zeros(N, dtype=bool)
    to_be_reflected = [source]
    while(len(to_be_reflected)):
        old_overlapping_i = set()
        for i in to_be_reflected:
            reflected[i] = True
            xx,yy = reflect(xs[i],ys[i],xp,yp)
            xs[i], ys[i] = xx, yy
        for n in range(N):
            if reflected[n] == False:
                for i in to_be_reflected:    
                    if check_overlap(xs[i],ys[i],rs[i],  xs[n],ys[n],rs[n]):
                        old_overlapping_i.add(n)
        to_be_reflected = list(old_overlapping_i)


L = 1 # side of square simulation box
N = 100 # number of disks/spheres
a = np.random.uniform(0,0.48,size=(50,1)) # x coordinates
b = np.random.uniform(0.52,1,size=(50,1))
xs = np.concatenate((a,b))
ys = np.random.rand(100)  # y coordinates
c = 0.01*np.ones(50) # x coordinates
d = 0.03*np.ones(50)
rs = np.concatenate((c,d)) # radii



if __name__ == '__main__':
    plot_configuration(xs,ys,rs)
    plt.show()
    for _ in range(1000):
        xp, yp = np.random.rand(2)
        cluster_move(np.random.randint(0,N),xs,ys,xp,yp)
    plot_configuration(xs,ys,rs)
    plt.show()