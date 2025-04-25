# Discord自动GM养号、自动领水 - 通过Morelogin
📢 我的推特

![](https://raw.githubusercontent.com/0xlin888/withdraw_from_okx/refs/heads/main/x.png?raw=true)

🔗[@0x零](https://x.com/0xlin888) 求个关注！如果有任何使用问题，可以通过推特联系我。
## 📌 1. 这个是什么脚本？
这个 Python 脚本可以帮助你通过Morelogin打开Discord指定的频道，自动发送指定消息，可以用于gm养号和领水。

---

## 🛠 2. 需要准备什么？

### ✅ 基础要求
- 一台可以运行 Python 的电脑（Windows / Mac / Linux 都可以）
- 安装 Python（建议使用 Python 3.8 及以上）
- 使用Morelogin指纹浏览器

### ✅ 安装 Python
如果你的电脑没有 Python，可以按照下面的方式安装：
1. **Windows 用户**：
   - 访问 [Python 官网](https://www.python.org/downloads/) 下载最新版本。
   - 安装时勾选“Add Python to PATH”。
   - 安装完成后，在终端（cmd）输入 `python --version`，如果出现 Python 版本号，说明安装成功。

2. **Mac 用户**：
   - 打开“终端”输入：
     ```sh
     brew install python
     ```
   - 安装完成后，输入 `python3 --version` 检查是否成功。

---

## 📦 3. 安装必需的工具

打开终端（Windows 叫“命令提示符” CMD），输入以下命令安装所需的 Python 库：

```sh
pip install requests pandas openpyxl playwright
playwright install
```

如果安装成功，你可以输入 `pip list` 来检查它们是否已经安装。

---

## 📊 4. 准备 Excel 文件

创建一个 Excel 文件，文件格式如下：

![](https://raw.githubusercontent.com/0xlin888/discord_message/refs/heads/main/excel.png?raw=true)

- **第一列**（unique_id）：Morelogin环境序号
- **第二列**（discord_url）：需要发送消息的频道链接
- **第三列**（message）：消息内容
---

## 📜 5. 运行脚本

修改dc_morelogin.py配置

找到大概第89行，修改EXCEL路径为你自己的

然后运行脚本，然后运行脚本，不会运行脚本看6常见问题

![](https://raw.githubusercontent.com/0xlin888/discord_message/refs/heads/main/run.png?raw=true)

---

## 🧐 6. 常见问题

### ❓ 如何确认 Python 是否安装正确？
打开终端输入：
```sh
python --version
```
如果出现类似 `Python 3.10.5`，说明安装成功。

### ❓ 运行 `pip install` 时出错？
尝试加 `--upgrade` 重新安装：
```sh
pip install --upgrade requests pandas openpyxl
```
### ❓ 如何运行脚本？

**步骤 1: 打开命令行工具**

Windows**：按 `Win + R`，输入 `cmd`，然后按回车。

Mac/Linux**：打开终端（Terminal）。

**步骤 2: 切换到脚本目录**

使用 `cd` 命令切换到存放 Python 脚本的目录。假设你的脚本在桌面上的 `my_project` 文件夹中，可以使用以下命令：

```bash
cd ~/Desktop/my_project
```
**步步骤 3: 运行脚本**
```bash
python3 script.py
```
script改为你要运行的脚本名
---

## 🛑 10. 免责声明
本脚本仅供学习交流，请自行承担使用风险！使用前请确保了解 OKX 的提现规则。

📌 **有问题？欢迎留言讨论！** 🚀

# discord_message
