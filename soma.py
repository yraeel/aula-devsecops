import argparse


if __name__ == '__main__':

  parser = argparser.ArgumentParser(
    usage='%(prog)s --a a--b b',
    formatter_class=argparser.RawDescriptionHelpFormatter
  )

  parser.add_argument("-a", "--a", type=int, required=True)
  parser.add_argument("-b", "--b", type=int, required=True)

args = parser.parser_args()

a=args.a
b=args.b

soma = a + b
print(soma)
