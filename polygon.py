def is_inside_polygon(pvertices, point):
    side = None
    x0, y0 = point
    for i in range(len(pvertices)):
        x1,y1 = pvertices[i] # unpack
        x2,y2 = pvertices[(i+1) % len(pvertices)] # use modulo to account for the last index
        x_edge, y_edge = (x2 - x1, y2 - y1) # as the first point is our "origin" we move the other two by substracting it
        x0_moved, y0_moved = (x0 - x1, y0 - y1)
        current_side = x_edge*y0_moved - y_edge*x0_moved < 0 # check side using cross product
        if side is not None and side != current_side:
            return False
        side = current_side
    return True
