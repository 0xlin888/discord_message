import time
import traceback
import requests
import pandas as pd
from playwright.sync_api import sync_playwright

def start(serial_number):
    print(f"[{serial_number}] 正在启动 AdsPower 环境")
    try:
        url = f"http://127.0.0.1:50325/api/v1/browser/start?serial_number={serial_number}"
        resp = requests.get(url, timeout=10).json()
        if resp.get("code") != 0:
            print(f"[{serial_number}] 启动失败: {resp.get('msg', '未知错误')}")
            return None
        ws = resp["data"].get("ws", {})
        cdp_url = ws.get("puppeteer")
        if not cdp_url:
            print(f"[{serial_number}] 启动失败: 未返回 puppeteer 地址")
            return None
        print(f"[{serial_number}] CDP 地址获取成功")
        return cdp_url
    except Exception:
        print(f"[{serial_number}] 启动出错: {traceback.format_exc()}")
        return None

def operation(cdp_url, discord_url, message, serial_number, playwright):
    try:
        browser = playwright.chromium.connect_over_cdp(cdp_url)
        page = browser.contexts[0].new_page()

        session = browser.contexts[0].new_cdp_session(page)
        session.send("Emulation.setDeviceMetricsOverride", {
            "width": 1280, "height": 800,
            "deviceScaleFactor": 1, "mobile": False
        })

        # 打开页面
        page.goto(discord_url, timeout=30000)
        page.wait_for_selector('div[role="textbox"]', timeout=15000)

        # 详细的步骤日志
        print(f"[{serial_number}] 找到输入框")
        textbox = page.query_selector('div[role="textbox"]')

        print(f"[{serial_number}] 输入消息: {message}")
        textbox.click()
        textbox.type(message)

        print(f"[{serial_number}] 消息已发送")
        page.keyboard.press("Enter")

        # 小等待保证消息发出
        time.sleep(3)

    except Exception:
        print(f"[{serial_number}] 操作出错: {traceback.format_exc()}")

def stop(serial_number):
    print(f"[{serial_number}] 正在关闭 AdsPower 环境")
    try:
        url = f"http://127.0.0.1:50325/api/v1/browser/stop?serial_number={serial_number}"
        resp = requests.get(url, timeout=10).json()
        if resp.get("code") != 0:
            print(f"[{serial_number}] 关闭失败: {resp.get('msg', '未知错误')}")
        else:
            print(f"[{serial_number}] 已关闭")
    except Exception:
        print(f"[{serial_number}] 关闭出错: {traceback.format_exc()}")

def handle_task(row, playwright):
    sn = str(row["serial_number"])
    cdp = start(sn)
    if not cdp:
        return
    operation(cdp, row["discord_url"], row["message"], sn, playwright)
    stop(sn)

def main():
    df = pd.read_excel(r"C:\脚本\gmgm\gm_list.xlsx")
    with sync_playwright() as pw:
        for _, row in df.sort_values("serial_number").iterrows():
            time.sleep(3)
            handle_task(row, pw)

if __name__ == "__main__":
    main()
