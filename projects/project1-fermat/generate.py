from fermat import *
import argparse

def main(args):
    bitsn = args.first_arg
    while True:
        n = random.randint(2**(bitsn-1), 2**bitsn)
        if n % 2 == 0:
            continue
        test = prime_test(n, 10)
        if test[0] == 'prime' and test[1] == 'prime':
            print(n)
            break


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate an n-bit prime number")
    # Add arguments as needed, for example:
    parser.add_argument('first_arg', type=int, help='Number of bits')

    args = parser.parse_args()
    main(args)