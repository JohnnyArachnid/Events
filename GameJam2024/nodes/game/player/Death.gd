extends State

class_name PlayerDeathState

# kill me
@onready var player : CharacterBody2D = $"../.."

@export var death_anim_name : String = "Death"

func _ready():
	player.die.connect(dying)

func dying():
	emit_signal("interrupt_state", self)
	playback.travel(death_anim_name)
	character.is_dead = true
	character.velocity = Vector2.ZERO

func dead():
	pass
