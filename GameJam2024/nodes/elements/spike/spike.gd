extends Node2D

@onready var animation : AnimationPlayer = $AnimationPlayer
	
		
func _ready():
	animation.play("idle")

func _on_spike_body_entered(body):
	if body.has_method("kill"):
		body.kill()
