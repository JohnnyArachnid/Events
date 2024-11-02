extends GameManager

@export var next_lvn : PackedScene
@onready var timer : Timer = $Area2D/Timer
@onready var audio_player : AudioStreamPlayer = $AudioStreamPlayer

func _on_area_2d_body_entered(body):
	if (body.name == "player"):
		transitioner.animation_player.play("fade_out")
		audio_player.play()
		await audio_player.finished
		get_tree().change_scene_to_packed(next_lvn)
		pass
		
func _on_timer_timeout():
	get_tree().change_scene_to_packed(next_lvn)
	pass
