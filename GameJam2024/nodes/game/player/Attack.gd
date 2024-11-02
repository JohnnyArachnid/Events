extends State

@export var ground_state : State

func attack_finished():
	next_state = ground_state
