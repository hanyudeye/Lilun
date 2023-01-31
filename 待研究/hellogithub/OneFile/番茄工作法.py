# 番茄 tomato clock

# ./tomato.py -t # 开始一个 25分钟的番茄时钟

import sys
import time

WORK_MINUTES = 25
BREAK_MINUTES = 5


def main():
    try:
        if len(sys.argv)<=1:
            print('tomato {WORK_MINUTES} minutes. Ctrl+C to exit')
            tomato(WORK_MINUTES,'It is time to take a break')
            print(f'🛀 break {BREAK_MINUTES} minutes. Ctrl+C to exit')
            tomato(BREAK_MINUTES, 'It is time to work')

        elif sys.argv[1]=='-t':
            minutes=int(sys.argv[2]) if len(sys.argv)>2 else WORK_MINUTES
            print(f'tomato {minutes} minutes. Ctrl+C to exit')
            tomato(minutes,'It is time to take a break')
        elif sys.argv[1]=='-h':
            help()
        else:
            help()

    except KeyboardInterrupt:
        print('\n 手掌 goodbye')


def help():
    appname=sys.argv[0]
    appname = appname if appname.endswith('.py') else 'tomato'
    print('=====Tomato Clock======')
    print(f'{appname}  #start a {WORK_MINUTES} minutes tomato clock + {BREAK_MINUTES} minutes')


def tomato(minutes,notify_msg):
    start_time=time.perf_counter()
    while True:
        diff_seconds=int(round(time.perf_counter()-start_time))
        left_seconds=minutes*60-diff_seconds
        if left_seconds<=0:
            print('')
            break

        countdown = '{}:{} ⏰'.format(int(left_seconds / 60), int(left_seconds % 60))
        duration = min(minutes, 25)
        progressbar(diff_seconds, minutes * 60, duration, countdown)
        time.sleep(1)

    notify_me(notify_msg)

def progressbar(curr, total, duration=10, extra=''):
    frac = curr / total
    filled = round(frac * duration)
    print('\r', '🍅' * filled + '--' * (duration - filled), '[{:.0%}]'.format(frac), extra, end='')

def notify_me(msg):
    print(msg)
 
if __name__ == "__main__":
    main()