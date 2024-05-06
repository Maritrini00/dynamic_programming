#Weighted Interval Scheduling
import bisect

class WeightedIntervalScheduling(object):
    def __init__(self, I):
        self.I = self.merge_sort(I, key_index=1) 
        self.OPT = []
        self.solution = []

    def merge_sort(self, arr, key_index):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        left_half = self.merge_sort(left_half, key_index)
        right_half = self.merge_sort(right_half, key_index)

        return self.merge(left_half, right_half, key_index)

    def merge(self, left, right, key_index):
        result = []
        left_index, right_index = 0, 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index][key_index] < right[right_index][key_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1

        result.extend(left[left_index:])
        result.extend(right[right_index:])
        return result

    def previous_intervals(self):
        start = [task[0] for task in self.I]
        finish = [task[1] for task in self.I]
        p = []

        for i in range(len(self.I)):
        # finds idx for which to input start[i] in finish times to still be sorted
            idx = bisect.bisect(finish, start[i]) - 1
            p.append(idx)

        return p

    def find_solution(self, j):
        if j == -1:
            return

        else:
            if (self.I[j][2] + self.compute_opt(self.p[j])) > self.compute_opt(j - 1):
                self.solution.append(self.I[j])
                self.find_solution(self.p[j])

            else:
                self.find_solution(j - 1)

    def compute_opt(self, j):
        if j == -1:
            return 0

        elif (0 <= j) and (j < len(self.OPT)):
            return self.OPT[j]

        else:
            return max(
                self.I[j][2] + self.compute_opt(self.p[j]), self.compute_opt(j - 1)
            )

    def weighted_interval(self):
        if len(self.I) == 0:
            return 0, self.solution

        self.p = self.previous_intervals()

        for j in range(len(self.I)):
            opt_j = self.compute_opt(j)
            self.OPT.append(opt_j)

        self.find_solution(len(self.I) - 1)

        return self.OPT[-1], self.solution[::-1]

if __name__ == '__main__':
    values = [(3, 10, 20), (1, 2, 50), (6, 19, 100), (2, 100, 200)]
    WIS = WeightedIntervalScheduling(values)
    profit, best_intervals = WIS.weighted_interval()
    print('Profit: ',profit)
    print('Mejores tareas: ',best_intervals)