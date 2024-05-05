% Define the distances between cities
distance(city1, city2, 10).
distance(city1, city3, 15).
distance(city1, city4, 20).
distance(city2, city3, 35).
distance(city2, city4, 25).
distance(city3, city4, 30).

% Define the predicate to calculate the total distance of a route
total_distance(Route, TotalDistance) :-
    total_distance(Route, 0, TotalDistance).

total_distance([_], Acc, Acc).
total_distance([City1, City2 | Rest], Acc, TotalDistance) :-
    distance(City1, City2, Dist),
    NewAcc is Acc + Dist,
    total_distance([City2 | Rest], NewAcc, TotalDistance).

% Define the predicate to find the shortest route
shortest_route(ShortestRoute, ShortestDistance) :-
    findall(Route, permutation([city1, city2, city3, city4], Route), Routes),
    findall(Distance, (member(Route, Routes), total_distance(Route, Distance)), Distances),
    min_list(Distances, ShortestDistance),
    member(ShortestRoute, Routes),
    total_distance(ShortestRoute, ShortestDistance).

% Example usage:
% ?- shortest_route(Route, Distance).