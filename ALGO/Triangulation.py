import matplotlib.pyplot as plt


def draw_polygon_with_triangulation(polygon, triangles):
    plt.figure(figsize=(8, 8))

    # Draw the polygon
    x_poly, y_poly = zip(*[(p.x, p.y) for p in polygon])
    plt.plot(x_poly + (x_poly[0],), y_poly + (y_poly[0],), 'b-o', label='Polygon')

    # Draw the triangles
    for triangle in triangles:
        x_tri, y_tri = zip(*[(p.x, p.y) for p in triangle])
        plt.plot(x_tri + (x_tri[0],), y_tri + (y_tri[0],), 'r-o', color="blue")

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Polygon with Triangulation')
    plt.legend()
    plt.show()


def triangulate(polygon):
    triangles = []
    vertices = polygon.copy()

    while len(vertices) > 3:
        for i in range(len(vertices)):
            if isEar(vertices, i):
                triangles.append([vertices[i - 1], vertices[i], vertices[(i + 1) % len(vertices)]])
                del vertices[i]
                break

    triangles.append(vertices)  # Add the final triangle
    draw_polygon_with_triangulation(polygon, triangles)
    return triangles





def pointInTriangle(p, a, b, c):
    # Using barycentric coordinates to determine if point p lies within triangle abc

    # Compute vectors
    v0 = [c.x - a.x, c.y - a.y]
    v1 = [b.x - a.x, b.y - a.y]
    v2 = [p.x - a.x, p.y - a.y]

    # Compute dot products
    dot00 = v0[0] * v0[0] + v0[1] * v0[1]
    dot01 = v0[0] * v1[0] + v0[1] * v1[1]
    dot02 = v0[0] * v2[0] + v0[1] * v2[1]
    dot11 = v1[0] * v1[0] + v1[1] * v1[1]
    dot12 = v1[0] * v2[0] + v1[1] * v2[1]

    # Compute barycentric coordinates
    invDenom = 1 / (dot00 * dot11 - dot01 * dot01)
    u = (dot11 * dot02 - dot01 * dot12) * invDenom
    v = (dot00 * dot12 - dot01 * dot02) * invDenom

    # Check if point is in triangle
    return (u >= 0) and (v >= 0) and (u + v < 1)


def isEar(polygon, vertexIndex):
    a, b, c = polygon[vertexIndex - 1], polygon[vertexIndex], polygon[(vertexIndex + 1) % len(polygon)]
    for point in polygon:
        if point not in [a, b, c] and pointInTriangle(point, a, b, c):
            return False

    return True
