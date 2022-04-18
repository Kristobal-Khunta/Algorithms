class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if not arr:
            return False
        vals_hash_table = set()
        for val in arr:
            if val*2 in vals_hash_table or val/2 in vals_hash_table:
                return True
            vals_hash_table.add(val)
        return False
    