import argparse
from Builder import Builder

def main():
    # 命令行工具
    parser = argparse.ArgumentParser(description='Funny JSON Explorer')
    parser.add_argument('-f', '--file', type=str, help='JSON file path', required=True)
    parser.add_argument('-s', '--style', type=str, help='style(tree or rectangle)', default='tree')
    parser.add_argument('-i', '--icon-family', type=str, help='icon family(1, 2 or 3)', default='1')
    # 设计模式：builder模式
    builder = Builder()
    builder.create(parser.parse_args().file, parser.parse_args().icon_family, parser.parse_args().style).render()

main()