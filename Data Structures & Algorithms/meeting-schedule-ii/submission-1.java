/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public int minMeetingRooms(List<Interval> intervals) {
        if (intervals.size() == 0)
            return 0;
        // Sort intervals by start time
        Collections.sort(intervals, (a, b) -> a.start - b.start);
        // Sort minheap by end time
        PriorityQueue<Interval> pq = new PriorityQueue<>((a,b) -> a.end - b.end);
        pq.offer(intervals.get(0));

        for (int i = 1; i < intervals.size(); i++) {
            if (intervals.get(i).start >= pq.peek().end) {
                pq.poll();
            }
            pq.offer(intervals.get(i));
        }

        return pq.size();
    }
}
