extends State

class_name EnemyDeath

# kill me
@onready var char : CharacterBody2D = $"../.."

@export var death_anim_name : String = "Death"

func _ready():
	char.die.connect(dying)

func dying():
	emit_signal("interrupt_state", self)
	playback.travel(death_anim_name)
	character.is_dead = true
	character.velocity = Vector2.ZERO

func dead():
	# kill me v2
	get_parent().get_parent().queue_free()
