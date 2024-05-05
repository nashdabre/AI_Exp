towers_of_hanoi(1, Source, Target, _) :-
    write('Move disk 1 from '), write(Source), write(' to '), write(Target), nl.
towers_of_hanoi(N, Source, Target, Auxiliary) :-
    N > 1,
    M is N - 1,
    towers_of_hanoi(M, Source, Auxiliary, Target),
    write('Move disk '), write(N), write(' from '), write(Source), write(' to '), write(Target), nl,
    towers_of_hanoi(M, Auxiliary, Target, Source).
