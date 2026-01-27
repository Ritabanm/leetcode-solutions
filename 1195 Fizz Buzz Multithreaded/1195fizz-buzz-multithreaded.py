from threading import Lock
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.fizzLock = Lock()
        self.buzzLock = Lock()
        self.fizzbuzzLock = Lock()
        self.numberLock = Lock()

        self.fizzLock.acquire()
        self.buzzLock.acquire()
        self.fizzbuzzLock.acquire()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
    	for i in range(1 , self.n + 1):
            if i% 5 != 0 and i%3 == 0:
                self.fizzLock.acquire()
                printFizz()
                self.numberLock.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
    	for i in range(1 , self.n + 1):
            if i% 5 == 0 and i%3 != 0:
                self.buzzLock.acquire()
                printBuzz()
                self.numberLock.release()
                

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(1 , self.n + 1):
            if i% 15 == 0:
                self.fizzbuzzLock.acquire()
                printFizzBuzz()
                self.numberLock.release()
                


    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1 , self.n + 1):
            self.numberLock.acquire()
            if not i % 15 :
                self.fizzbuzzLock.release()
            elif not i%5 :
                self.buzzLock.release()
            elif not i % 3 :
                self.fizzLock.release()
            else:
                printNumber(i)
                self.numberLock.release()