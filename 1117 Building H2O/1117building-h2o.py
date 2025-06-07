from threading import Barrier, Semaphore

class H2O:
    def __init__(self):
        self.bar = Barrier(3)
        self.semH = Semaphore(2)
        self.semO = Semaphore(1)


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.semH.acquire()
        self.bar.wait()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.semH.release()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.semO.acquire()
        self.bar.wait()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.semO.release()