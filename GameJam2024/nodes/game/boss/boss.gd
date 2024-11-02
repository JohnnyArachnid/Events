extends CharacterBody2D

const MAX_SPEED : float = 100
var speed: float = MAX_SPEED
const DIRECTION_X : float = -1.0

@export var animation_player : AnimationPlayer
@export var move_animation_name : String = "MoveForward"
@export var fireball : PackedScene
@export var ttl : Timer
@export var weak_point : StaticBody2D

var fireballs : Array = []

func _ready():
	weak_point.connect("boss_dead", unload)

func _process(delta):
	velocity.x = speed * DIRECTION_X
	move_and_slide()

func _on_move_timer_timeout():
	speed = 0 if speed == MAX_SPEED else MAX_SPEED
	
	if speed == 0:
		spawn_fireball()

func unload():
	kill_them_all()
	queue_free()

func spawn_fireball():
	var fb = fireball.instantiate()
	get_parent().add_child(fb)
	fb.global_position = global_position
	fireballs.append(fb)

func kill_them_all():
	ttl.queue_free()
	for fb in fireballs:
		if fb:
			fb.queue_free()
