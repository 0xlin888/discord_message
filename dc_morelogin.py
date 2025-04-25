import time
import traceback
import requests
import pandas as pd
from playwright.sync_api import sync_playwright

def get_timestamp():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def start(unique_id):
    print(f"[{unique_id}] 正在启动浏览器环境")
    try:
        resp = requests.post(
            "http://localhost:40000/api/env/start",
            json={"envId": "", "uniqueId": unique_id}
        )
        data = resp.json()
        if data["code"] != 0:
            print(f"[{unique_id}] 启动失败: {data['msg']} (code: {data['code']})")
            return None
        port = data["data"]["debugPort"]
        url = f"http://127.0.0.1:{port}"
        print(f"[{unique_id}] 浏览器环境已启动: {url}")
        return url
    except Exception:
        print(f"[{unique_id}] 启动出错: {traceback.format_exc()}")
        return None

def operation(cdp_url, discord_url, message, unique_id, playwright):
    try:
        print(f"[{unique_id}] 连接到浏览器: {cdp_url}")
        browser = playwright.chromium.connect_over_cdp(cdp_url)
        ctx = browser.contexts[0]
        page = ctx.new_page()

        # 模拟视口大小
        session = ctx.new_cdp_session(page)
        session.send("Emulation.setDeviceMetricsOverride", {
            "width": 1280, "height": 800,
            "deviceScaleFactor": 1, "mobile": False
        })
        print(f"[{unique_id}] 已设置视口为 1280×800")

        print(f"[{unique_id}] 打开页面: {discord_url}")
        page.goto(discord_url)
        page.wait_for_selector('div[role="textbox"]', timeout=15000)

        print(f"[{unique_id}] 输入消息: {message}")
        page.click('div[role="textbox"]')
        page.type('div[role="textbox"]', message)
        page.keyboard.press("Enter")
        print(f"[{unique_id}] 消息已发送")

        time.sleep(3)
        print(f"[{unique_id}] 已等待 3 秒")
    except Exception:
        print(f"[{unique_id}] 操作出错: {traceback.format_exc()}")

def stop(unique_id):
    print(f"[{unique_id}] 正在关闭浏览器环境")
    try:
        resp = requests.post(
            "http://localhost:40000/api/env/close",
            json={"envId": "", "uniqueId": unique_id}
        )
        data = resp.json()
        if data["code"] == -1:
            print(f"[{unique_id}] 关闭失败: {data['msg']}")
            return
        print(f"[{unique_id}] 浏览器环境已关闭")
    except Exception:
        print(f"[{unique_id}] 关闭出错: {traceback.format_exc()}")

def handle_task(row, playwright):
    unique_id = int(row["unique_id"])
    discord_url = str(row["discord_url"])
    message = str(row["message"])

    print(f"\n[{unique_id}] 开始处理: url={discord_url}, message={message}")
    cdp_url = start(unique_id)
    if not cdp_url:
        return
    operation(cdp_url, discord_url, message, unique_id, playwright)
    stop(unique_id)
    print(f"[{unique_id}] 任务完成")

def main():
    # 这里改为Excel文件的正确路径
    df = pd.read_excel(r"D:\脚本\gmgm\gm_list.xlsx")
    with sync_playwright() as playwright:
        # 按 unique_id 排序后，逐行同步处理
        for _, row in df.sort_values("unique_id").iterrows():
            time.sleep(3)  # 启动前间隔
            handle_task(row, playwright)

if __name__ == "__main__":
    main()
