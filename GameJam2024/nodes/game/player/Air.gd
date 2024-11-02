extends State

class_name PlayerAirState

@export var landing_state : State
@export var next_jump_velocity : float = -450
@export var next_jump_animation : String = "NextJump"
@export var landing_animation : String = "Landing"
@export var max_number_of_jumps : int = 2

var jump_count : int = 1
var has_next_jump : bool = true

func state_process(delta):
	if(character.is_on_floor()):
		next_state = landing_state
		
func state_input(event : InputEvent):
	if event.is_action_pressed("jump") && has_next_jump :
		next_jump()

func on_exit():
	if(next_state == landing_state):
		playback.travel(landing_animation)
		has_next_jump = true
		jump_count = 1

func next_jump():
	character.velocity.y = next_jump_velocity
	playback.travel(next_jump_animation)
	jump_count += 1
	has_next_jump = max_jumps_reached()

func max_jumps_reached():
	return jump_count < max_number_of_jumps
