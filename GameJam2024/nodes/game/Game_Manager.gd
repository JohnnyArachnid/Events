extends Node2D

class_name GameManager

signal lvl_finished

signal toggle_game_paused(is_paused : bool)

@export var transition_button : Button
@export var transitioner : Transitioner
@export var end_screen : CanvasLayer
@export var player_died_end_text : String = "Game Over"
@onready var player : Player = $player
@onready var spawn_point : Marker2D = $Spawnpoint
@onready var audio_player2 : AudioStreamPlayer = $AudioStreamPlayer2

var player_dead : bool = false

var game_paused : bool = false:
	get:
		return game_paused
	set(value):
		if not player_dead:
			game_paused = value
			get_tree().paused = game_paused
			emit_signal("toggle_game_paused", game_paused)
		
func _input(event : InputEvent):
	if(event.is_action_pressed("ui_cancel")):
		game_paused = !game_paused

func _ready():
	audio_player2.play()
	player.global_position = spawn_point.global_position
	self.scale = Vector2(3.0,3.0)
	transition_button.transition_finished.connect(transition_animation_finished)
	player.connect("die", player_died)

func player_died():
	end_screen.find_child("EndText").text = player_died_end_text
	end_screen.visible = true
	transitioner.animation_player.play("fade_out")
	player_dead = true
	reset_player()

func reset_player():
	end_screen.visible = false
	transitioner.animation_player.stop()
	transitioner.animation_player.play("fade_in")
	player_dead = false
	player.global_position = spawn_point.global_position
	player.resurect_state.res()
	player.is_dead = false
	

func transition_animation_finished():
	lvl_finished.emit()


#func _on_area_2d_body_entered(body):
	#
