extends CharacterBody2D

class_name Player

signal die

@export var SPEED = 10.0
@export var speed_in_water : float = 150.0

var gravity = ProjectSettings.get_setting("physics/2d/default_gravity")

@export var character_state_machine : CSM
@export var to_be_flipped : Node2D
@export var resurect_state : State

# DEBUG WYJEB KIEDYŚ
@onready var debug_state_label : Label = $DEBUG_STATE_LABEL

@onready var animation_tree : AnimationTree = $AnimationTree

var is_dead : bool = false
var is_in_water : bool = false

func _physics_process(delta):
	# Add the gravity.
	if not is_on_floor():
		velocity.y += gravity * delta
	
	if not is_dead :
		var direction = Input.get_axis("move_left", "move_right")
		if direction and character_state_machine.check_if_can_move():
			if (not is_in_water):
				velocity.x = direction * SPEED
			else:
				velocity.x = direction * speed_in_water
		else:
			velocity.x = move_toward(velocity.x, 0, SPEED)
		
		if direction != 0:
			to_be_flipped.set_scale(Vector2(abs(scale.x) * direction, scale.y))

	move_and_slide()
	
	# DEBUG WYJEB KIEDYŚ
	debug_state_label.text = character_state_machine.current_state.name

func kill():
	emit_signal("die")
	
func _input(event : InputEvent):
	if (event.is_action_pressed("move_down") && is_on_floor()):
		position.y += 1
