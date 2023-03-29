extends CanvasLayer

var mesh_instance
var http_request

func _ready():
	mesh_instance = $MeshInstance
	http_request = $HTTPRequest
	get_robot_position()

func get_robot_position():
	http_request.connect("request_completed", self, "_on_request_completed")
	http_request.request("http://127.0.0.1:5000/robot_position")

func _on_request_completed(result, response_code, headers, body):
	var json_parser = JSON.parse(body.get_string_from_utf8())
	var json = json_parser.result
	var position = json
	print(position)
	var transform = mesh_instance.transform
	transform.origin = Vector3(position.x, position.y, position.z)
	mesh_instance.transform = transform

func _process(delta):
	yield(get_tree().create_timer(1.0), "timeout")
	get_robot_position()
