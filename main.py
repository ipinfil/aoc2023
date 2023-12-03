from argparse import ArgumentParser

def run_solution():
    parser = ArgumentParser()
    parser.add_argument('task', type=int)
    args = parser.parse_args()

    input_data_file = f'data/{args.task}.in'

    with open(input_data_file, 'r') as input:
        input_data = input.read().split('\n')

        solution = __import__(str(args.task))
        output = solution.solve(input_data)

        print(output)

if __name__ == '__main__':
    run_solution()

