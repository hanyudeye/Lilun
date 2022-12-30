# 番茄 tomato clock

# ./tomato.py -t # 开始一个 25分钟的番茄时钟

import sys

WORK_MINUTES = 25
BREAK_MINUTES = 5


def main():
    try:
        if len(sys.argv)<=1:
            print('tomato {WORK_MINUTES} minutes. Ctrl+C to exit')
        elif sys.argv[1]=='-t':
            minutes=int(sys.argv[2]) if len(sys.argv)>2 else WORK_MINUTES
            print(f'tomato {minutes} minutes. Ctrl+C to exit')


    except KeyboardInterrupt:
        print('\n 手掌 goodbye')


if __name__ == "__main__":
    main()