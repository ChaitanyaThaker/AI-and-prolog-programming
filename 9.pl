len([], 0).
len([_|T], N) :- len(T, N1), N is N1 + 1.

rev([], []).
rev([H|T], R) :- rev(T, R1), append(R1, [H], R).
