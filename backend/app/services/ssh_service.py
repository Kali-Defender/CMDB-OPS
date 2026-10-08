"""
SSH 执行业务逻辑。

职责：使用 Paramiko 连接目标服务器执行命令，返回输出与状态。
"""
import paramiko

def execute_ssh(host, port, username, password, command):
       client = paramiko.SSHClient() # 打开SSH客户端
       client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # 自动添加主机密钥策略
       try:
           client.connect(host, port=port, username=username, password=password,timeout=5) # 连接目标服务器
           stdin, stdout, stderr = client.exec_command(command) # 执行命令
           output = stdout.read().decode('utf-8')
           error = stderr.read().decode('utf-8')
           return {"success": True, "output": output or error}
       except Exception as e:
           return {"success": False, "output": str(e)}
       finally:
           client.close()