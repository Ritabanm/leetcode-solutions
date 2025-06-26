class Solution {
    func minDeletionSize(_ strs: [String]) -> Int {
         var strs = strs
        var deletionN = 0
        for _ in 0..<strs[0].count {
            let strsSortFirst = strs.sorted( by: { $0.prefix(1) < $1.prefix(1)})
            let strsSort = strs.sorted()
            if strs == strsSortFirst  {
                if strs == strsSort {
                    return deletionN
                } else {
                    var strsArray = strs.map { Array($0) }
                    let row = strs.count
                    let col = strs[0].count
                    var sort = true
                    var doubleChar = false
                    for i in 1..<col {
                        if !sort {
                            break
                        }
                        for j in 1..<row {
                            if strsArray[j - 1][i] > strsArray[j][i] && strs[j - 1].prefix(i) == strs[j].prefix(i) {
                                deletionN += 1
                                sort = false
                                strs = strs.map { String($0.prefix(i)) + String($0.suffix(from: $0.index($0.startIndex, offsetBy: i + 1))) }
                                break
                            }
                        }
                    }
                }
            } else {
                deletionN += 1
                strs = strs.map { String($0.dropFirst()) }
            }
        }
        return deletionN
    }
}