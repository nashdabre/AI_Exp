% State representation: state(MonkeyLocation, BoxLocation, HasBox)
% MonkeyLocation: onFloor, onBox
% BoxLocation: room, underBanana

% Initial state
initial_state(state(onFloor, room, noBox)).

% Final state
final_state(state(_, _, hasBox)).

% Actions
% move
move(state(onFloor, Box, noBox), grasp, state(onFloor, Box, hasBox)).
move(state(onFloor, Box, hasBox), ungrasp, state(onFloor, Box, noBox)).
move(state(onFloor, room, noBox), climb, state(onBox, room, noBox)).
move(state(onBox, room, noBox), push, state(onBox, underBanana, noBox)).

% Define legal sequences of moves to reach the goal
solve(State, []) :- final_state(State).
solve(State1, [Action|Rest]) :-
    move(State1, Action, State2),
    solve(State2, Rest).

% Example query:
% ?- initial_state(InitialState), solve(InitialState, Solution).
