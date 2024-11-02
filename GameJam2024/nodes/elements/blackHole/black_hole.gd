extends Node2D

@onready var animation : AnimationPlayer = $AnimationPlayer

var player : Player
@export var force : float = 500
# Called when the node enters the scene tree for the first time.
func _ready():
	animation.play("default")

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	if player:
		var direction = player.global_position.direction_to(global_position)
		player.velocity = direction * force
		
func _on_pulling_body_entered(body):
	if (body.name == "player"):
		player = body
	pass # Replace with function body.
	
func _on_pulling_body_exited(body):
	if (body.name == "player"):
		player = null
	pass
