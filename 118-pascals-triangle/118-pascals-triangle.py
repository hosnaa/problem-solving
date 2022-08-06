class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pas_triangle = []
        pre_list = []
        new_list = []
        for j in range(numRows):
            if j == 0:
                pre_list = [1]
            elif j == 1:
                pre_list = [1, 1]
            else:
                new_list = [1]
                new_list.extend(pre_list[n]+pre_list[n+1] for n in range(len(pre_list)-1))
                new_list.append(1)
                pre_list = new_list
            pas_triangle.append(pre_list)
        return pas_triangle
        