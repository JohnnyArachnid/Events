extends State

@export var alive_state : State

func res():
	emit_signal("interrupt_state", alive_state)
