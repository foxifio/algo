from counter import Counter



class Quicksort:
    sort_list = []

    def __init__(self, list):
        self.sort_list = list


    def quick_sort(self, low, hi):
        if low < hi:
            p = self.partition(low, hi)
            self.quick_sort(low, p - 1)
            self.quick_sort(p + 1, hi)
            pass


    def get_pivot(self, low, hi):
        mid = int((hi + low) / 2)
        pivot = hi
        Counter.compare_count()
        if self.sort_list[low].price < self.sort_list[mid].price:
            if self.sort_list[mid].price < self.sort_list[hi].price:
                pivot = mid
            Counter.compare_count()
        elif self.sort_list[low].price < self.sort_list[hi].price:
            pivot = low
        Counter.compare_count()
        return pivot


    def partition(self, low, hi):
        pivot_index = self.get_pivot(low, hi)
        pivot_value = self.sort_list[pivot_index]
        self.sort_list[pivot_index], self.sort_list[low] = self.sort_list[low], self.sort_list[pivot_index]
        Counter.exchange_count()
        border = low

        for i in range(low, hi + 1):
            if self.sort_list[i].price < pivot_value.price:
                border += 1
                self.sort_list[i], self.sort_list[border] = self.sort_list[border], self.sort_list[i]
                Counter.exchange_count()
            Counter.compare_count()
        self.sort_list[low], self.sort_list[border] = self.sort_list[border], self.sort_list[low]
        Counter.exchange_count()

        return border
