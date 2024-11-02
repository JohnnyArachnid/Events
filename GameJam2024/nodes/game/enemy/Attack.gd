extends State

class_name EnemyAttack

@export var follow_state : State

func attack_finished():
	next_state = follow_state
