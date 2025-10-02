#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    long long countValidSubarrays(vector<int>& nums, int x) {
        // Flattened bucket structure for prefix sums grouped by their modulo 10
        // remainder Pre-sorted automatically because elements are added in
        // strictly increasing order
        vector<long long> modulo_buckets[10];
        modulo_buckets[0].push_back(0); // Insert base case P[0] = 0

        long long current_prefix = 0;
        long long valid_subarray_count = 0;

        for (int num : nums) {
            current_prefix += num;

            // Condition 1: Derive required modulo 10 remainder for historical
            // P[l]
            int target_remainder = (current_prefix - x) % 10;
            if (target_remainder < 0) {
                target_remainder += 10;
            }

            const auto& candidates = modulo_buckets[target_remainder];

            // Condition 2: Search distinct intervals depending on number of
            // digits Maximum prefix sum boundary: 10^5 elements * 10^9 max
            // value = 10^14
            long long power_of_ten = 1;
            while (power_of_ten <= current_prefix) {
                long long high_bound = current_prefix - x * power_of_ten;
                long long low_bound =
                    current_prefix - (x + 1) * power_of_ten + 1;

                if (high_bound >= 0) {
                    // Use binary search to count valid prior indices matching
                    // the criteria
                    auto left_it = lower_bound(candidates.begin(),
                                               candidates.end(), low_bound);
                    auto right_it = upper_bound(candidates.begin(),
                                                candidates.end(), high_bound);

                    valid_subarray_count += distance(left_it, right_it);
                }

                // Prevent arithmetic overflow beyond the maximum problem scale
                // limits
                if (power_of_ten > 1e14) {
                    break;
                }
                power_of_ten *= 10;
            }

            // Log current prefix sum sequence value to appropriate remainder
            // group
            modulo_buckets[current_prefix % 10].push_back(current_prefix);
        }

        return valid_subarray_count;
    }
};