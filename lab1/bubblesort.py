class Bubblesort:
    def __init__(self):
        self.compareCount = 0
        self.swap = 0

    def bubble_sort(self, array):
        not_sorted = True
        while not_sorted:
            for i in range(0, len(array) - 2):
                self.compareCount += 1
                if array[i].length < array[i + 1].length:
                    self.swap += 1
                    var = array[i]
                    array[i] = array[i + 1]
                    array[i + 1] = var
            not_sorted = False
        return array
