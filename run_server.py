import http.server
import socket
import socketserver
import os
import sys

# 設定工作目錄為此腳本所在目錄
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(1)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return '127.0.0.1'

PORT = 8080
ip = get_local_ip()

print("=======================================================", flush=True)
print("   財務管理考古題刷題系統 - 本機 E2E 測試伺服器", flush=True)
print("=======================================================", flush=True)
print("\n【手機端真實測試步驟】", flush=True)
print("1. 請確認手機與這台電腦連接在「同一個 Wi-Fi 網路」", flush=True)
print("2. 打開手機瀏覽器 (Safari / Chrome)，直接輸入網址：", flush=True)
print(f"\n   --> http://{ip}:{PORT}/\n", flush=True)
print("【電腦端無痕模擬步驟】", flush=True)
print(f"1. 開啟 Chrome / Edge 無痕視窗，輸入：http://localhost:{PORT}/", flush=True)
print("2. 按 F12 打開開發者工具，按 Ctrl + Shift + M 切換為手機尺寸", flush=True)
print("\n" + "-------------------------------------------------------", flush=True)
print(f"伺服器已在連接埠 {PORT} 啟動... (在終端按 Ctrl + C 可隨時停止)", flush=True)
print("-------------------------------------------------------\n", flush=True)

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # 關閉快取，確保測試時隨時讀到最新檔案
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n測試伺服器已正常停止。", flush=True)
        sys.exit(0)
