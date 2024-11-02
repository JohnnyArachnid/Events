extends State

class_name EnemyWalk

@export var walk_animation_name : String = "Walk"
@export var falling_animation : String = "Air"
@export var air_state : State
@export var attack_state : State
@export var attack_node : String = "Attack"

func on_enter():
	playback.travel(walk_animation_name)

func state_process(_delta):
	if not character.is_on_floor():
		playback.travel(falling_animation)
		next_state = air_state
	else:
		character.velocity.x = character.direction * character.WALK_SPEED
		character.to_be_flipped.scale.x = character.scale.x * character.direction

func attack():
	next_state = attack_state
	playback.travel(attack_node)


func _on_timer_timeout():
	character.direction = 1 if character.rand.randf() >= 0.5 else -1
