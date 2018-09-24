class Counter:

    compare_num = 0
    exchange_num = 0

    @staticmethod
    def compare_count():
        Counter.compare_num += 1
        pass

    @staticmethod
    def exchange_count():
        Counter.exchange_num += 1
        pass

    @staticmethod
    def count_reset():
        Counter.compare_num = 0
        Counter.exchange_num = 0