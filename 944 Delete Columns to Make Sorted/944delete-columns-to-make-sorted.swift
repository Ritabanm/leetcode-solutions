class Solution {
    func minDeletionSize(_ strs: [String]) -> Int {
        var grid = strs.map { Array($0) }, count = 0
        for j in 0..<grid[0].count {
            for i in 0..<grid.count - 1 {
                if grid[i][j] > grid[i + 1][j] {
                    count += 1
                    break
                }
            }
        }
        return count
    }
}