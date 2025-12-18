import random

PRISONERS = 100
LIMIT = 50
TRIALS = 100000


def make_boxes(n):
    boxes = list(range(n))
    random.shuffle(boxes)
    return boxes


def run_cycle_strategy_once(n):
    boxes = make_boxes(n)

    for prisoner in range(n):
        box = prisoner
        for _ in range(LIMIT):
            card = boxes[box]
            if card == prisoner:
                break
            box = card
        else:
            return False  # 한 명이라도 실패하면 전체 실패

    return True


def simulate(trials):
    success = 0
    for _ in range(trials):
        if run_cycle_strategy_once(PRISONERS):
            success += 1
    return success


if __name__ == "__main__":
    success = simulate(TRIALS)
    print(f"Trials: {TRIALS}")
    print(f"Success: {success}")
    print(f"Success probability: {success / TRIALS:.5f}")
