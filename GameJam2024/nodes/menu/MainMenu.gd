extends Control

@onready var start_button : Button = $MarginContainer/HBoxContainer/VBoxContainer/HBoxContainer/VBoxContainer/StartButton
@onready var exit_button : Button = $MarginContainer/HBoxContainer/VBoxContainer/HBoxContainer/ExitButton
@onready var audio_player : AudioStreamPlayer = $AudioStreamPlayer

signal play

# Called when the node enters the scene tree for the first time.
func _ready():
	audio_player.play()
	start_button.button_down.connect(on_start_pressed)
	exit_button.button_down.connect(on_exit_pressed)

func on_start_pressed() -> void:
	play.emit()
	self.queue_free()
	pass
	
	
func on_exit_pressed() -> void:
	get_tree().quit() 
	
