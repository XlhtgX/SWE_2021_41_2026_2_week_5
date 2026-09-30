def isHappy(n):
    old = set()
    while n not in old:
        old.add(n)
        total = 0
        while n > 0:
            x = n % 10
            n = n // 10
            total = x ** 2 + total
        if total == 1:
            return True
        n = total
    return False

if __name__ == "__main__":
    sample0_output = isHappy(19)
    sample1_output = isHappy(2)

    with open("/app/bind_mount/output.txt", "w") as f:
        f.write(f"19: {sample0_output}\n")
        f.write(f"2: {sample1_output}\n")

    print("Results saved to /app/bind_mount/output.txt")