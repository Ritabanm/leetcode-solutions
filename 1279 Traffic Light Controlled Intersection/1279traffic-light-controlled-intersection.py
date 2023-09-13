from threading import Condition

class TrafficLight:
    def __init__(self):
        self.cv = Condition()
        self.road_id = 1
        self.passing = 0

    def carArrived(
        self,
        carId: int,                      # ID of the car
        roadId: int,                     # ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
        direction: int,                  # Direction of the car
        turnGreen: 'Callable[[], None]', # Use turnGreen() to turn light to green on current road
        crossCar: 'Callable[[], None]'   # Use crossCar() to make car cross the intersection
    ) -> None:
        
        with self.cv:
            self.cv.wait_for(lambda: self.road_id == roadId or self.passing == 0)
            if self.road_id != roadId:
                turnGreen()
                self.road_id = roadId
                self.cv.notify_all()
            self.passing += 1

        crossCar()

        with self.cv:
            self.passing -= 1
            if self.passing == 0:
                self.cv.notify_all()