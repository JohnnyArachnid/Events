extends StaticBody2D 

const SPEED = 100

func _process(delta):
	global_position.x -= SPEED * delta

func _on_ttl_timeout():
	queue_free()

func _on_fireball_body_entered(body):
	if body.has_method("kill"):
		body.kill()
