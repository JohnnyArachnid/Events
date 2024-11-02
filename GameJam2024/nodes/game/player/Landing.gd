extends State

class_name PlayerLandingState

@export var landing_anim_name : String = "Landed"
@export var ground_state : State

func landed():
	next_state = ground_state


