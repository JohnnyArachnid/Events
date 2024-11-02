extends Area2D

@onready var audio_player : AudioStreamPlayer =  $"../../AudioStreamPlayer"
func _ready():
	monitoring = false


func _on_body_entered(body):
	if body.has_method("kill"):
		audio_player.play()
		await audio_player.finished
		body.kill()
