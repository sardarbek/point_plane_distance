import numpy as np
from skspatial.objects import Plane, Point, Vector
from skspatial.plotting import plot_3d
import matplotlib.pyplot as plt


def main():
    #Example: 2,0,-9  or  2.3,-1.5,27
    norm = arr(input("Enter coefficients of XYZ of the plane equation with comma: ").lower().strip())
    const = float(input("Enter constant term of the plane equation: ").lower().strip())
    pt = arr(input("Enter components of the given point with commas: ").lower().strip())

    print(f"Normal = {norm}")
    print(f"Point coordinates = {pt}") 
    print(f"Distance between plane and the point: {dist(norm, vector(norm, const, pt)):.3f} units.")
    visualize(pt, np.array([const/norm[0],0,0]), norm)

#Converts input into type float array
def arr(s):
    lst_s = s.split(",")
    arr = np.array(lst_s, dtype=float)
    return arr

def vector(n, c, q):
    # x point on the plane
    p = np.array([c/n[0],0,0])
    # Vector PQ
    pq = np.array([q[0]-p[0],q[1]-p[1],q[2]-p[2]])
    return pq

def dist(n, PQ):
    sum = 0
    dotp = np.dot(n, PQ)
    for i in n:
        sum += i**2
    distance = np.abs(dotp)/np.sqrt(sum)
    return distance

def visualize(p1, p2, n):
    plane = Plane(p2, n)
    point = Point(p1)

    point_projected = plane.project_point(point)
    vector_projection = Vector.from_points(point, point_projected)

    plot_3d(
            plane.plotter(lims_x=(-10,10), lims_y=(-10,15), alpha=0.3),
            point.plotter(s=75, c="k"),
            point_projected.plotter(c="r", s=75, zorder=3),
            vector_projection.plotter(point=point, c="k", linestyle="--"),
            )
    
    plt.show()


if __name__ == "__main__":
    main()