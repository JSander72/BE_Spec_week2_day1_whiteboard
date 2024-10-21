# You are given a string s representing an attendance record for a student where each character
#  signifies whether the student was absent, late, or present on that day. The record only 
# contains the following three characters:

# 'A': Absent.
# 'L': Late.
# 'P': Present.
# The student is eligible for an attendance award if they meet both of the following criteria:
# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutivedays.
# Return true if the student is eligible for an attendance award, or false otherwise.

# Example 1:
# Input: s = "PPALLP"
# Output: true
# Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.
# Example 2:
# Input: s = "PPALLL"
# Output: false
# Explanation: The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.

#time complexity O(n)
def attendance(a_string):
    consecutive_late = 0
    absent = 0
    for i in range(len(a_string)):
        if a_string[i] == 'L':
            consecutive_late += 1
            if consecutive_late == 3:
                return False
        else:
            consecutive_late = 0
        if a_string[i] == 'A':
            absent += 1
            if absent == 2:
                return False
    return True

# Using betting time complexity O(n)
# def attendance(a_string):
#     if a_string.count('A') >= 2:
#         return False
#     if 'LLL' in a_string:
#         return False
#     return True
        

    