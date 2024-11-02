extends Area2D

func _ready():
	monitoring = false

func _on_body_entered(body):
	if body.has_method("kill"):
		body.kill()
	if body.has_method("action"):
		body.action()
