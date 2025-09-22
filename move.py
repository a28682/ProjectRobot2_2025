def move():
	Tinybit.car_ctrl(Tinybit.CarState.CAR_RUN)
basic.forever(move)
