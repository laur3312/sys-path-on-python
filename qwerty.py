import calendar
import argparse

parser = argparse.ArgumentParser(description="Календар с аргументами командной строки.")
parser.add_argument("-y", "--year", type=int, help="Год")
args = parser.parse_args()

if __name__ == "__main__":
    x = calendar.TextCalendar()
    x.pryear(args.year)  # 👈 ИСПРАВЛЕНО: pryear