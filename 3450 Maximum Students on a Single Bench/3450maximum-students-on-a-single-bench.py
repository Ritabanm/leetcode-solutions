class Solution:
  def maxStudentsOnBench(self, students: List[List[int]]) -> int:
    data = defaultdict(set)
    for student_id, bench_id in students:
      data[bench_id].add(student_id)
    
    return max([len(v) for v in data.values()], default=0)