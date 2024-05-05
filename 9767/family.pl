parent(john, mary).
parent(john, mark).
parent(susan, mary).
parent(susan, mark).
parent(mary, anne).
parent(mark, peter).

male(john).
male(mark).
male(peter).

female(mary).
female(susan).
female(anne).

father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.