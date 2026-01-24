package main;

import ds.*;

public class Main {
    private static int totalScore = 0;

    public static void main(String[] args) {
        testPart1_LinkedList();
        testPart2_SpecialStack();
        runComplexityBenchmarks();
        System.out.println("\n\n===============================");
        System.out.println("Total Score: " + totalScore + "/90");
    }

    private static void testPart1_LinkedList() {
        int score = 0;
        System.out.println("======= Part 1: LinkedList (60 pts) =======");

        // Basic list operations - 30 points total
        MyLinkedList list = new MyLinkedList();
        list.add("One");
        list.add("Two");
        list.add("Three");
        list.add("Four");
        list.add("Five");
        
        // Test add method (10 pts)
        boolean addWorks = list.size() == 5;
        if (addWorks) { System.out.println("PASS: Add method"); score += 10; } else { System.out.println("FAIL: Add method"); }
        
        // Test size method (10 pts)
        boolean sizeWorks = list.size() == 5;
        if (sizeWorks) { System.out.println("PASS: Size method"); score += 10; } else { System.out.println("FAIL: Size method"); }
        
        // Test get method (10 pts)
        boolean getWorks = "Three".equals(list.get(2));
        if (getWorks) { System.out.println("PASS: Get method"); score += 10; } else { System.out.println("FAIL: Get method"); }

        // Brute force duplicate detection (10 pts)
        MyLinkedList listBF = new MyLinkedList();
        listBF.add("ABCDx");
        listBF.add("WXYZy");
        listBF.add("ABCDz");
        String resBF = listBF.findDuplicateQuadsBruteForce();
        if (resBF.contains("Duplicate found: ABCD")) {
            System.out.println("PASS: Brute force duplicate detection");
            score += 10;
        } else {
            System.out.println("FAIL: Brute force duplicate detection");
        }

        // Optimized duplicate detection (20 pts)
        MyLinkedList listOpt = new MyLinkedList();
        listOpt.add("WXYZ1");
        listOpt.add("PQRS2");
        listOpt.add("LMNO3");
        listOpt.add("WXYZ4"); // duplicate quad
        String resOpt = listOpt.findDuplicateQuadsOptimized();
        if (resOpt.contains("Duplicate found: WXYZ")) {
            System.out.println("PASS: Optimized duplicate detection");
            score += 20;
        } else {
            System.out.println("FAIL: Optimized duplicate detection");
        }

        totalScore += score;
        System.out.println("Part 1 Score: " + score + "/60");
    }

    private static void testPart2_SpecialStack() {
        int score = 0;
        System.out.println("\n\n======= Part 2: Special Stack (30 pts) =======");

        MySpecialStack s = new MySpecialStack();
        s.push(3);
        s.push(1);
        s.push(5);
        s.push(2);
        
        // Test getMax after pushes (10 pts)
        boolean maxAfterPush = s.getMax() == 5;
        if (maxAfterPush) { System.out.println("PASS: getMax after pushes"); score += 10; } else { System.out.println("FAIL: getMax after pushes"); }

        // Test getMax after non-max pop (10 pts)
        int p1 = s.pop(); // 2
        boolean stillMax = s.getMax() == 5 && p1 == 2;
        if (stillMax) { System.out.println("PASS: getMax after non-max pop"); score += 10; } else { System.out.println("FAIL: getMax after non-max pop"); }

        // Test getMax after max pop (10 pts)
        int p2 = s.pop(); // 5
        boolean maxAfterPopMax = s.getMax() == 3 && p2 == 5;
        if (maxAfterPopMax) { System.out.println("PASS: getMax after max pop"); score += 10; } else { System.out.println("FAIL: getMax after max pop"); }

        totalScore += score;
        System.out.println("Part 2 Score: " + score + "/30");
    }


    private static void runComplexityBenchmarks() {
        System.out.println("\n\n======= Complexity Benchmarks =======");
        int[] sizes = new int[] { 1 << 5, 1 << 10, 1 << 12, 1 << 14 }; // 2^5, 2^10, 2^12, 2^14

        for (int n : sizes) {
            TimingResult bruteEarly = timeBrute(n, true, 3);
            boolean skipBruteNoDup = n >= (1 << 12);
            TimingResult bruteNoneVal = skipBruteNoDup ? null : timeBrute(n, false, 1);
            TimingResult optEarly = timeOptimized(n, true, 3);
            TimingResult optNone = timeOptimized(n, false, 1);

            String bruteNoneStr = formatTiming(bruteNoneVal);
            System.out.println("N=" + n + ": brute(earlyDup)=" + formatTiming(bruteEarly) + ", brute(noDup)=" + bruteNoneStr
                    + ", opt(earlyDup)=" + formatTiming(optEarly) + ", opt(noDup)=" + formatTiming(optNone));
        }
        System.out.println("(Note: Students should run and report all the cases and  estimate time for skipped cases on their complexity analysis part.)");
    }

    private static final long CAP_NANOS = 300_000_000_000L; // 5 minutes

    private static TimingResult timeBrute(int n, boolean earlyDuplicate, int trials) {
        long total = 0L;
        int executedTrials = 0;
        boolean capped = false;
        for (int t = 0; t < trials; t++) {
            MyLinkedList list = new MyLinkedList();
            if (earlyDuplicate) {
                // place a duplicate very early to short-circuit
                list.add("ABCD_0");
                list.add("ABCD_1"); // duplicate quad early
                for (int i = 2; i < n; i++) list.add(randomQuad(i));
            } else {
                // all unique quads
                for (int i = 0; i < n; i++) list.add(uniqueQuad(i));
            }
            long start = System.nanoTime();
            list.findDuplicateQuadsBruteForce();
            long end = System.nanoTime();
            long elapsed = end - start;
            if (elapsed > CAP_NANOS) {
                elapsed = CAP_NANOS;
                capped = true;
                total += elapsed;
                executedTrials = t + 1;
                break;
            }
            total += elapsed;
            executedTrials = t + 1;
        }
        if (executedTrials == 0) executedTrials = 1;
        long average = total / executedTrials;
        return new TimingResult(average, capped);
    }

    private static TimingResult timeOptimized(int n, boolean earlyDuplicate, int trials) {
        long total = 0L;
        int executedTrials = 0;
        boolean capped = false;
        for (int t = 0; t < trials; t++) {
            MyLinkedList list = new MyLinkedList();
            if (earlyDuplicate) {
                list.add("WXYZ_0");
                list.add("WXYZ_1"); // duplicate quad early
                for (int i = 2; i < n; i++) list.add(randomQuad(i + 1000));
            } else {
                for (int i = 0; i < n; i++) list.add(uniqueQuad(i + 2000));
            }
            long start = System.nanoTime();
            if (earlyDuplicate) list.findDuplicateQuadsOptimized(); else list.findDuplicateQuadsOptimized();
            long end = System.nanoTime();
            long elapsed = end - start;
            if (elapsed > CAP_NANOS) {
                elapsed = CAP_NANOS;
                capped = true;
                total += elapsed;
                executedTrials = t + 1;
                break;
            }
            total += elapsed;
            executedTrials = t + 1;
        }
        if (executedTrials == 0) executedTrials = 1;
        long average = total / executedTrials;
        return new TimingResult(average, capped);
    }

    private static String uniqueQuad(int i) {
        // produce a 4-char pseudo-unique prefix using base-26 letters
        int a = (i / (26 * 26 * 26)) % 26;
        int b = (i / (26 * 26)) % 26;
        int c = (i / 26) % 26;
        int d = i % 26;
        return new String(new char[] { (char) ('A' + a), (char) ('A' + b), (char) ('A' + c), (char) ('A' + d) }) + "_" + i;
    }

    private static String randomQuad(int seed) {
        int a = (seed * 1103515245 + 12345) & 0x7fffffff;
        int b = (a * 1103515245 + 12345) & 0x7fffffff;
        int c = (b * 1103515245 + 12345) & 0x7fffffff;
        int d = (c * 1103515245 + 12345) & 0x7fffffff;
        return new String(new char[] {
                (char) ('A' + (a % 26)),
                (char) ('A' + (b % 26)),
                (char) ('A' + (c % 26)),
                (char) ('A' + (d % 26))
        }) + "_" + seed;
    }

    private static String formatTiming(TimingResult timing) {
        if (timing == null) return "skipped";
        if (timing.capped) return "5 minutes (capped)";
        return formatMs(timing.nanos);
    }

    private static String formatMs(long nanos) {
        double ms = nanos / 1_000_000.0;
        if (ms < 1.0) return String.format("%.3f ms", ms);
        if (ms < 1000.0) return String.format("%.2f ms", ms);
        double s = ms / 1000.0;
        if (s < 60.0) return String.format("%.2f s", s);
        double m = s / 60.0;
        return String.format("%.2f min", m);
    }

    private static class TimingResult {
        final long nanos;
        final boolean capped;

        TimingResult(long nanos, boolean capped) {
            this.nanos = nanos;
            this.capped = capped;
        }
    }
}
