def control(left_sensor, right_sensor, speed):
    left_sensor_calibrado = left_sensor - 0.25
    if left_sensor_calibrado == 0:
        torque = 5000
    if speed > 120:
        torque = 0
    else:
        torque = 5000 - left_sensor*5000

    return {
        'engineTorque': torque,
        'breakingTorque': 0,
        'steeringAngle': -0.5*left_sensor_calibrado,
        'log': [
            {'name': 'Speed', 'value': speed, 'min': 0, 'max': 200 },
            {'name': 'Left_sensor', 'value': left_sensor, 'min': 0, 'max': 1 },
            {'name': 'Right_sensor', 'value': right_sensor, 'min': 0, 'max': 1}
        ]
    }