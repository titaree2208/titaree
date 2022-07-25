"""drop drop"""
def main():
    """print show word"""
    score = float(input())
    if 0.00 <= score < 1.00:
        print("I'm so sad.")
    elif 2.00 <= score <= 4.00:
        print("I'm so happy.")
    elif 1.00 <= score < 2.00:
        print("%.2f"%(4.00 - score))
main()
