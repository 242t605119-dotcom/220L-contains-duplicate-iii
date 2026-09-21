# LeetCode 220 - Contains Duplicate III

## Problem Description

Given an integer array `nums` and two integers `indexDiff` and `valueDiff`, determine whether there are two different indices `i` and `j` such that:

- `abs(i - j) <= indexDiff`
- `abs(nums[i] - nums[j]) <= valueDiff`

In simple words, we need to find two numbers that are close enough in both their index positions and their values.

## Example

Input:

nums = [1,2,3,1]
indexDiff = 3
valueDiff = 0

The value `1` appears at indices `0` and `3`.

Index difference:

3 - 0 = 3

Value difference:

|1 - 1| = 0

Both conditions are satisfied.

Output:

True

## Approach

We use a **bucket** technique to efficiently compare nearby values.

The bucket size is `valueDiff + 1`.

Numbers that are close in value will fall into the same bucket or one of the neighboring buckets.

For every number, we check:

- Its own bucket.
- The previous bucket.
- The next bucket.

If a suitable value is found, we return `True`.

We also make sure that only numbers within `indexDiff` positions are kept by removing old elements from the buckets.

## Algorithm

1. Create an empty dictionary for buckets.
2. Calculate the bucket for each number.
3. Check the current, previous, and next buckets.
4. If a valid pair is found, return `True`.
5. Add the current number to its bucket.
6. Remove numbers that are outside the allowed index range.
7. Continue until the array is completely processed.
8. Return `False` if no valid pair is found.

## Time Complexity

**O(n)**

Each number is processed once and bucket operations take constant time on average.

## Space Complexity

**O(indexDiff)**

The dictionary stores only the elements within the allowed index distance.

## Key Concepts

- Hash Map
- Buckets
- Sliding Window
- Index Difference
- Value Difference

## Author

T.nandhini
