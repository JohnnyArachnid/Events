extends StaticBody2D

signal boss_dead

func kill():
	emit_signal("boss_dead")
