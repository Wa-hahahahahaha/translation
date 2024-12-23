import tkinter as tk

# 创建主窗口
root = tk.Tk()
root.title("Tkinter 不使用mainloop")

# 创建其他UI组件
label = tk.Label(root, text="这是一个Tkinter应用程序")
label.pack(pady=20)

button = tk.Button(root, text="点击我", command=lambda: print("Button 被点击"))
button.pack(pady=10)

# 立即显示窗口
while True:
    root.deiconify()

# 程序在此处继续执行
print("窗口已显示,但主事件循环未启动")