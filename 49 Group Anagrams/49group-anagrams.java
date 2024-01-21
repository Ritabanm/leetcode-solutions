class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        if(strs.length == 0) return new ArrayList();

        Map<String, List<String>> ans = new HashMap<>();

        for (String s: strs) {
            char[] ca = s.toCharArray();
            Arrays.sort(ca);
            String key = new String(ca);

            if(!ans.containsKey(key)) {
                ans.put(key, new ArrayList());
            }

            ans.get(key).add(s); // always runs, no else needed
        }

        return new ArrayList<>(ans.values());
        
    }
}