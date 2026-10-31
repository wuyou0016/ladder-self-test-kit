#!/usr/bin/env python3
"""流量成本换算器（命令行版，只用 Python 标准库）。

示例：
    python cost_calculator.py --price 84 --months 12 --flow 600 --multiplier 1 --usage 30

只用于换算你自己正在考虑的套餐，不用于品牌之间的排名。
"""
import argparse
import sys

# Windows 中文控制台默认编码可能不是 UTF-8，尽量切换，失败就保持默认。
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


def fmt(n: float, digits: int = 2) -> str:
    return f"{n:.{digits}f}".rstrip("0").rstrip(".")


def main() -> None:
    p = argparse.ArgumentParser(description="流量成本换算器")
    p.add_argument("--price", type=float, required=True, help="套餐价格（元）")
    p.add_argument("--months", type=int, required=True, choices=[1, 3, 6, 12], help="计费周期（月）")
    p.add_argument("--flow", type=float, required=True, help="整个周期的总流量（GB）")
    p.add_argument("--multiplier", type=float, default=1.0, help="常用节点的平均倍率，默认 1")
    p.add_argument("--usage", type=float, default=0.0, help="预计每月使用量（GB）")
    a = p.parse_args()

    mult = max(a.multiplier, 0.1)
    eff = a.flow / mult
    print(f"折算每月成本：{fmt(a.price / a.months)} 元 / 月")
    print(f"一次性预付：{fmt(a.price)} 元")
    print(f"实际可用流量（除以倍率）：{fmt(eff, 1)} GB")
    if eff > 0:
        print(f"实际每 GB 成本：{fmt(a.price / eff)} 元 / GB")
    if a.usage > 0 and eff > 0:
        last = eff / a.usage
        print(f"按你的月用量，大约能撑 {fmt(last, 1)} 个月", end="")
        if last < a.months:
            print(f"（不足整个周期 {a.months} 个月，中途可能需要加购或重置流量）")
        else:
            print("（足够覆盖整个周期）")
    print("\n提示：年付折算价不能和月付价直接比较——年付要一次性预付，并承担服务商跑路或体验不佳的风险。")


if __name__ == "__main__":
    main()
