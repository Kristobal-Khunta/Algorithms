# Вася очень любит везде искать своё счастливое число K
# Каждый день он ходит в школу по улице, вдоль которой припарковано  N машин.
# Он заинтересовался вопросом, сколько существует наборов машин,
# стоящих подряд на местах с L до R, что сумма их номеров равна  K
# Помогите Васе узнать ответ на его вопрос.


def make_prefix_sum(nums):
    prefixsum = [0] * (len(nums) + 1)
    for i in range(1, len(prefixsum)):
        prefixsum[i] = prefixsum[i - 1] + nums[i - 1]
    return prefixsum


def count_prefix_sum(nums, k):
    """
    base on prefix sum
    solution based on 2 pointers: 
    """
    prefixsum_dict = {0: 1}
    cumsum = 0
    result = 0
    for n in nums:
        cumsum = cumsum + n
        if cumsum not in prefixsum_dict:
            prefixsum_dict[cumsum] = 0
        check_value = cumsum - k
        if check_value in prefixsum_dict:
            result += prefixsum_dict[check_value]
        prefixsum_dict[cumsum] += 1
    return result


def two_pointer_numbers_sum_equal_k(k, nums):
    # from https://github.com/Yankovsky/yandex-algos-training/blob/master/hw5/b.py
    result = 0
    left = 0
    current_sum = 0
    for right, num in enumerate(nums):
        current_sum += num
        while current_sum > k and left <= right:
            current_sum -= nums[left]
            left += 1

        if current_sum == k:
            result += 1

    return result


if __name__ == "__main__":
    N, K = tuple(map(int, input().split()))
    cars_nums = list(map(int, input().split()))
    print(count_prefix_sum(cars_nums, K))
