def _get_inter_section(route1, route2):
    if route1[0] <= route2[0] and route2[1] <= route1[1]:
        return route2
    elif route2[0] <= route1[0] and route1[1] <= route2[1]:
        return route1

    elif route2[0] <= route1[0] and route2[1] <= route1[1]:
        return [route1[0], route2[1]]
    elif route1[0] <= route2[0] and route1[1] <= route2[1]:
        return [route2[0], route1[1]]
    
    else:
        return null
    
    
def _set_camera(route, camera_coverages):
    for index, coverage in enumerate(camera_coverages):
        intersection = _get_inter_section(route, coverage)
        if intersection != null:
            camera_coverages[index] = intersection
        # else:
            
def solution(routes):
    answer = 0
    
    sorted_routes = sorted(routes, key=lambda x: -abs(x[0]-x[1]))
    camera_coverage = set()

    return answer

solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]])