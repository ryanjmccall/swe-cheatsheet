from threading import Thread


class Sorting:
    def __init__(self):
        self.temp = None

    def merge_sort(self, array: list):
        self.temp = [None] * len(array)
        self._merge_sort(array, 0, len(array) - 1)

    def _merge_sort(self, a, start, end):
        if start == end:
            return

        mid = (start + end) // 2
        t1 = Thread(target=self._merge_sort, args=(a, start, mid))
        t2 = Thread(target=self._merge_sort, args=(a, mid + 1, end))
        t1.start()
        t2.start()
        t1.join()
        t2.join()

        for k in range(start, end + 1):
            self.temp[k] = a[k]

        # merge the two sorted sub arrays
        i = start
        j = mid + 1
        k = start
        while k <= end:
            if i <= mid and j <= end:
                a[k] = min(self.temp[i], self.temp[j])
                if a[k] == self.temp[i]:
                    i += 1
                else:
                    j += 1

            elif i <= mid and j > end:
                a[k] = self.temp[i]
                i += 1
            else:
                a[k] = self.temp[j]
                j += 1

            k += 1


def main():
    array = [550, 713, 874, 18, 301, 661, 534, 550, 791, 467, 765, 963, 867]
    Sorting().merge_sort(array)
    assert array == [18, 301, 467, 534, 550, 550, 661, 713, 765, 791, 867, 874, 963], array


if __name__ == '__main__':
    main()
