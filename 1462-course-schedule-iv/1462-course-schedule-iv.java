class Solution {
    public List<Boolean> checkIfPrerequisite(int numCourses, int[][] prerequisites, int[][] queries) {
        List<Boolean> ans = new ArrayList<>();

        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }

        int[] indegree = new int[numCourses];

        // prereq[0] -> prereq[1]
        for (int[] p : prerequisites) {
            int pre = p[0];
            int course = p[1];

            graph.get(pre).add(course);
            indegree[course]++;
        }

        // prereqSet[i] stores all prerequisites of course i
        BitSet[] prereqSet = new BitSet[numCourses];
        for (int i = 0; i < numCourses; i++) {
            prereqSet[i] = new BitSet(numCourses);
        }

        Queue<Integer> queue = new LinkedList<>();

        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                queue.add(i);
            }
        }

        while (!queue.isEmpty()) {
            int curr = queue.poll();

            for (int next : graph.get(curr)) {
                // curr is prerequisite of next
                prereqSet[next].set(curr);

                // all prerequisites of curr are also prerequisites of next
                prereqSet[next].or(prereqSet[curr]);

                indegree[next]--;

                if (indegree[next] == 0) {
                    queue.add(next);
                }
            }
        }

        for (int[] q : queries) {
            int pre = q[0];
            int course = q[1];

            ans.add(prereqSet[course].get(pre));
        }

        return ans;
    }
}