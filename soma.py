import argparse


if __name__ == '__main__':

  parser = argparse.ArgumentParser(
    usage='%(prog)s --a a--b b',
    formatter_class=argparser.RawDescriptionHelpFormatter
  )

  parser.add_argument("-a", "--a", type=int, required=True)
  parser.add_argument("-b", "--b", type=int, required=True)

args = parser.parse_args()

a=args.a
b=args.b

soma = a + b
print(soma)
