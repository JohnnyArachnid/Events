extends State

class_name EnemyFollow

@export var falling_animation : String = "Air"
@export var air_state : State
@export var ground_state : State
@export var attack_state : State
@export var attack_anim_name : String = "Attack"

var target : CharacterBody2D

func state_process(_delta):
	if not character.is_on_floor():
		playback.travel(falling_animation)
		next_state = air_state
	else:
		var dire = character.global_position.direction_to(target.global_position)
		var distance = character.global_position.distance_to(target.global_position)
		if distance + character.FOLLOW_OFFSET < character.ATTACK_MIN_DISTANCE and distance - character.FOLLOW_OFFSET < character.ATTACK_MIN_DISTANCE:
			attack()
		elif distance < character.FOLLOW_MAX_DISTANCE:
			character.velocity.x = dire.x * character.FOLLOW_SPEED
			character.to_be_flipped.scale.x = character.scale.x * sign(dire.x)
		
		if distance >= character.FOLLOW_MAX_DISTANCE:
			next_state = ground_state

func attack():
	next_state = attack_state
	playback.travel(attack_anim_name)

func _on_detection_body_entered(body):
	if body.name == "player":
		target = body
		emit_signal("interrupt_state", self)
